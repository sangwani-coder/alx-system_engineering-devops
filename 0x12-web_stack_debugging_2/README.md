# Web Stack debugging # 2
## With great power comes great responsibility
The user **root** is, on Linux, the "superuser". It ca do anything it wants. That's a good and bad thing. That's why its preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the **root** user can do, judt need to use a specific command that you need to discover.
## Tasks
* **Run software as another user**
[0-iamsomeoneelse](./0-iamsomeoneelse):
- Bash script that accepts one argument
- runs the **whoami** command under the user passed as an argument
