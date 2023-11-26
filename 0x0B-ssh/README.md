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

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0B-ssh$ ssh -v ubuntu@52.204.237.230
OpenSSH_8.9p1 Ubuntu-3ubuntu0.4, OpenSSL 3.0.2 15 Mar 2022
debug1: Reading configuration data /home/smambo/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 52.204.237.230 [52.204.237.230] port 22.
debug1: Connection established.
debug1: identity file /home/smambo/.ssh/school type 0
debug1: identity file /home/smambo/.ssh/school-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
debug1: compat_banner: match: OpenSSH_8.2p1 Ubuntu-4ubuntu0.5 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 52.204.237.230:22 as 'ubuntu'
debug1: load_hostkeys: fopen /home/smambo/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:LLqb/9Etjn0Ukr6OsAWYNPJqdznwj19IzAB9mBz+NcM
debug1: load_hostkeys: fopen /home/smambo/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: Host '52.204.237.230' is known and matches the ED25519 host key.
debug1: Found key in /home/smambo/.ssh/known_hosts:7
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: get_agent_identities: bound agent to hostkey
debug1: get_agent_identities: ssh_fetch_identitylist: agent contains no identities
debug1: Will attempt key: /home/smambo/.ssh/school RSA SHA256:SkwnC3iOzHkFctLhoeRGG6u1MDwzTF8rlOKsAjmBykU explicit
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /home/smambo/.ssh/school RSA SHA256:SkwnC3iOzHkFctLhoeRGG6u1MDwzTF8rlOKsAjmBykU explicit
debug1: Server accepts key: /home/smambo/.ssh/school RSA SHA256:SkwnC3iOzHkFctLhoeRGG6u1MDwzTF8rlOKsAjmBykU explicit
Authenticated to 52.204.237.230 ([52.204.237.230]:22) using "publickey".
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: client_input_hostkeys: searching /home/smambo/.ssh/known_hosts for 52.204.237.230 / (none)
debug1: client_input_hostkeys: searching /home/smambo/.ssh/known_hosts2 for 52.204.237.230 / (none)
debug1: client_input_hostkeys: hostkeys file /home/smambo/.ssh/known_hosts2 does not exist
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Sending environment.
debug1: channel 0: setting env LC_ADDRESS = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_NAME = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_MONETARY = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_PAPER = "en_ZA.UTF-8"
debug1: channel 0: setting env LANG = "en_GB.UTF-8"
debug1: channel 0: setting env LC_IDENTIFICATION = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_TELEPHONE = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_MEASUREMENT = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_TIME = "en_ZA.UTF-8"
debug1: channel 0: setting env LC_NUMERIC = "en_ZA.UTF-8"
debug1: client_global_hostkeys_private_confirm: server used untrusted RSA signature algorithm ssh-rsa for key 0, disregarding
debug1: update_known_hosts: known hosts file /home/smambo/.ssh/known_hosts2 does not exist
ubuntu@345454-web-01:~$
```

### 3.Let me in!
Add the SSH public key below to your server so that we can connect using the `ubuntu` user.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

