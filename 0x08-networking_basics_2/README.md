## Hey there!
## Follow me as I tackle more tasks on Networking basics

![127.0.0.1](https://github.com/Smambo/alx-system_engineering-devops/assets/113464914/00f80311-f9cf-48b0-848b-669bb138864e)


## Learning objectives:
* What is localhost/127.0.0.1?
* What is 0.0.0.0?
* What is `/etc/hosts`?
* How to display your machine's active network interfacses?

## Tasks:
### 0.Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

* `localhost` resolves to `127.0.0.2`
* `facebook.com` resolves to `8.8.8.8`.
* The checker is running on Docker, so make sure to read [this](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ ping localhost 
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.064 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.068 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.064/0.066/0.068/0.002 ms
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ ping facebook.com
PING facebook.com (102.132.100.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-01-jnb1.facebook.com (102.132.100.35): icmp_seq=1 ttl=52 time=7.13 ms
64 bytes from edge-star-mini-shv-01-jnb1.facebook.com (102.132.100.35): icmp_seq=2 ttl=52 time=5.11 ms
^C
--- facebook.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 5.112/6.119/7.126/1.007 ms
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ sudo ./0-change_your_home_IP 
[sudo] password for smambo: 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ ping localhost 
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.060 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.104 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1007ms
rtt min/avg/max/mdev = 0.060/0.082/0.104/0.022 ms
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ ping facebook.com 
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=54 time=15.2 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.238/15.238/15.238/0.000 ms
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$
```

In the above example, we can see that:

* before running the script, `localhost` resolves to `127.0.0.1` and `facebook.com` resolves to `157.240.11.35`
* after running the script, `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`

If you’re running this script on a machine that you’ll continue to use, be sure to revert `localhost` to `127.0.0.1`. Otherwise, a lot of things will stop working!
### 1.Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$ ./1-show_attached_IPs | cat -e
127.0.0.1$
192.168.1.51$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x08-networking_basics_2$
```
