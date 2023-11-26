## SSH
## About:
The most common way of connecting to a remote Linux server is through [SSH](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys#how-ssh-works). SSH stands for Secure Shell and provides a safe and secure way of executing commands, making changes, and configuring services remotely. When you connect through SSH, you log in using an account that exists on the remote server.

## Tasks:
### [0.Use a private key](./0-use_a_private_key)
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:

* Only use `ssh` single-character flags
* You cannot use `-l`
* You do not need to handle the case of a private key protected by a passphrase

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$ ./0-use_a_private_key 
Enter passphrase for key '/home/smambo/.ssh/school': 
ubuntu@345454-web-01:~$ exit
logout
Connection to 52.204.237.230 closed.
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$
```

### [1.Create an SSH key pair](./1-create_ssh_key_pair)
Write a Bash script that creates an RSA key pair.

Requirements:

* Name of the created private key must be `school`
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase `betty`

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$ ls
0-use_a_private_key  1-create_ssh_key_pair  README.md
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$ ./1-create_ssh_key_pair 
Generating public/private rsa key pair.
Your identification has been saved in ./school
Your public key has been saved in ./school.pub
The key fingerprint is:
SHA256:WWcAioSC3yJOZ4mpNkrK/H8ONAfe7TExu8RiayY321Q smambo@lenovo-ubuntu
The key's randomart image is:
+---[RSA 4096]----+
|.  ..   ...      |
|o .. . .   .     |
| oo.o..  o. o    |
|.+o+o o oo+o     |
|+.o. + =SB E     |
|.=  . + = =      |
|B .  o * +       |
|oo    *.=        |
|  ....oo .       |
+----[SHA256]-----+
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$ ls
0-use_a_private_key  1-create_ssh_key_pair  README.md  school  school.pub
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$
```

### [2.Client configuration file](./2-ssh_config)
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

* Your SSH client configuration must be configured to use the private key `~/.ssh/school`
* Your SSH client configuration must be configured to refuse to authenticate using a password

### 3.Let me in!
Add the SSH public key below to your server so that we can connect using the `ubuntu` user.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

