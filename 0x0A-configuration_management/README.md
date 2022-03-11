# Configuration Management

* Server configuration management is a solution for turning your infrastructure into a codebase, describing all processes necessary for deploying a server in a set of provisioning scripts that can be versioned and easily reused.

## Writing Puppet Manifests
* Puppet is a popular configuration management tool capable of managing complex infrastructure in a transparent way, using a master server to orchestrate the configuration of the nodes.

* In this project I will Puppet manifests that must pass *puppet-lint* version 2.1.1 without any errors.

* The first line of my Puppet Manifest will be a comment explaining what the Puppet manifest is about.(i.e. # Install package).

In this project I will be writing Puppet Manifests.

## Tasks

* **0. Create a file**
[0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest that creates a file in */temp*.
### Requirements:
* File path is */tmp/school*
* File permission is *0744*
* File owner is *www-data*
* File group is *www-date*
* File contains *I love Puppet*

* **1. Install a package**
[1-install_a_package.pp](./1-install_a_package.pp): Puppet manifest to install:
* puppet-lint
* Version 2.5.0

* **2. Execute a command**
[2-execute_A_command](./2-execute_a_command): Puppet manifest that kills a process name killmenow.
* using the exec Puppet resource
* using pkill command
