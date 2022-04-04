# Firewall
In this project I will be installing and configuring a firewall on my load-balancing server.
## Whats a firewall
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
## UFW
Uncomplicated firewall (ufw) is a simplified firewall management interface that hides the complexity of lower-level packet filtering technologies ash as _iptabbles_ and _nftables._
UFW is installed by default on Ubuntu. If it has been uninstalled for some reason, you can install it with **sudo apt install ufw**
## Project Requirements
Block all incoming traffic except ports:
- 22 (SSH)
- 443 (HTTPSSSL)
- 80 (HTTP)
## Allowing SSH Connections
By default, UFW is set to deny all incoming connections and allow all outgoing connections. Servers typically need to respond to incoming requests from outside users.
If the firewall is enabled with defualt configurations, it would deny all incoming connections. This means that we need to create rules that explicitly allow legimate incoming connections - SSH or HTTP connections, in a cloud server you should probably allow incoming SSH connections so you can connect to and manage your server.

* **To configure the server to allow incoming SSH connections use the command:**
$ sudo ufw allow ssh
or specify the port instead of the service name.:
$ sudo ufw allow 22
do the same for HTTP(port 80) and HTTPS(port 443):
$ sudo ufw allow 443
$ sudo ufw allow 80
## Enabling UFW
To enable UFW, use this command:
$ sudo ufw enable
You will receive a warning that says the command may disrupt existing SSH connections. We already set up a firewall rule that allows SSH connections, so it should be fine to continue. Respond to the prompt with _y_ and hit _ENTER_.
