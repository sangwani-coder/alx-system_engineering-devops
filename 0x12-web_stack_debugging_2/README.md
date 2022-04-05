# Web Stack debugging # 2
## With great power comes great responsibility
The user **root** is, on Linux, the "superuser". It ca do anything it wants. That's a good and bad thing. That's why its preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the **root** user can do, judt need to use a specific command that you need to discover.
## Tasks
* **Run software as another user**
[0-iamsomeoneelse](./0-iamsomeoneelse):
- Bash script that accepts one argument
- runs the **whoami** command under the user passed as an argument

* **1. Run Nginx as Nginx**
[1-run_nginx_as_nginx](1-run_nginx_as_nginx): Bash script that fixes a web server to run Nginx listening on port '8080' as 'nginx' user.

* **7 lines of less**
[100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less): Bash script that fixes a web server to run Nginx listening on port '8080' as the 'nginx' user.
