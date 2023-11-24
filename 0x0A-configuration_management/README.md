# Configuration Management
## About:
As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management. Automation plays an essential role in server configuration management. It’s the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool’s specific language and features. Automation is, in fact, the heart of configuration management for servers, and that’s why it’s common to also refer to configuration management tools as Automation Tools or IT Automation Tools.

## Tasks:
### [0. Create a file](./0-create_a_file.pp)
Using Puppet, create a file in `/tmp`.

Requirements:

* File path is `/tmp/school`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

```
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# puppet-lint --version
puppet-lint 4.2.3
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# puppet-lint 0-create_a_file.pp 
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# puppet apply 0-create_a_file.pp 
Notice: Compiled catalog for 4da059d3fcb7.ec2.internal in environment production in 0.10 seconds
Notice: /Stage[main]/Main/File[/tmp/school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Applied catalog in 0.10 seconds
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# 
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Nov 24 10:01 /tmp/school
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# cat /tmp/school
I love Puppetroot@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management#
```

### [1. Install a package](./1-install_a_package.pp)
Using Puppet, install `flask` from `pip3`.

Requirements:

* Install `flask`
* Version must be `2.1.0`

```
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# puppet apply 1-install_a_package.pp 
Notice: Compiled catalog for 4da059d3fcb7.ec2.internal in environment production in 1.51 seconds
Notice: /Stage[main]/Main/Package[flask]/ensure: created
Notice: Applied catalog in 79.69 seconds
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

### [2. Execute a command](./2-execute_a_command.pp)
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

* Must use the `exec` Puppet resource
* Must use `pkill`

Example:
Terminal #0 - starting my process

```
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# cat killmenow 
#!/bin/bash
while [[ true ]]
do
    sleep 2
done
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# ./killmenow 
```

Terminal #1 - executing my manifest

```
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management#
```

Terminal #0 - process has been terminated

```
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management# ./killmenow 
Terminated
root@4da059d3fcb7:/alx-system_engineering-devops/0x0A-configuration_management#
```
