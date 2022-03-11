# Configuration Management
## Writing Puppet Manifests
Server configuration management is a solution for turning your infrastructure into a codebase, describing all processes necessary for deploying a server in a set of provisioning scripts that can be versioned and easily reused.

In this project I will be writing Puppet Manifests.
## Tasks
* **0. Create a file**
[0-create_a_file.pp](./0-create_a_file.pp): Puppet script that creates a file in */temp*.
### Requirements:
* File path is */tmp/school*
* File permission is *0744*
* File owner is *www-data*
* File group is *www-date*
* File contains *I love Puppet*
**Running the file:**
- $ puppet apply 0-create_a_file.pp
