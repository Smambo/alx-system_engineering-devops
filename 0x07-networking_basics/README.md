## Hey there!
## Follow me as I tackle tasks on Networking Basics
## Learning Objectives:
### OSI Model
* What it is
* How many layers it has
* How it is organised
### What is a LAN?
* Typical usage
* Typical geographical size
### What is a WAN?
* Typical usage
* Typical geographical size
### What is the Internet?
* What is an IP address?
* What are the 2 types of IP address?
* What is `localhost`?
* What is a subnet?
* Why IPv6 was created?
### TCP/UDP
* What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)?
* What is the main difference between TCP and UDP?
* What is a port?
* Memorise SSH, HTTP and HTTPS port numbers
* What tool/protocol is often used to check if a device is connected to a network?

## Tasks:
### [0.OSI model](./0-OSI_model)
![What is OSI Model?](https://camo.githubusercontent.com/35ec808754a7cab36bd6d1ea5b12314c5a1f0fa426683cc50385414fb717c87f/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f3235392f414a44524e65612e6a7067)

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly
### [1.Types of network](./1-types_of_network)
![Types of network](https://camo.githubusercontent.com/8e635b0a7fb273523c88a465e9a26c5485fde823fb264804d9d2919559f867bf/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f3235392f6b62614e4541312e6a7067)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN
What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN
### [2.MAC and IP address](./2-MAC_and_IP_address)
![MAC and IP address](https://camo.githubusercontent.com/476b4b95e12d7f7b315ff10ac9bc89cff04c4888943e2ff6b37b2b77d469efb4/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f3235392f5957744b4d55722e6a7067)

Questions:

What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

### [3.UDP and TCP](./3-UDP_and_TCP)
![UDP and TCP](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231004%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231004T135034Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5395c201ec69dc49e9f4ae23eefa06ec8cd25fbc35b1282d77881352c04ae1d8)

Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:

1.  `It is a protocol that is transferring data in a slow way but surely`
2.  `It is a protocol that is transferring data in a fast way and might loss data along in the process`

Which statement is correct for the UDP box:

1.  `It is a protocol that is transferring data in a slow way but surely`
2.  `It is a protocol that is transferring data in a fast way and might loss data along in the process`

Which statement is correct for the TCP worker:

1.  `Have you received boxes x, y, z?`
2.  `May I increase the rate at which I am sending you boxes?`

### [4.TCP and UDP ports](./4-TCP_and_UDP_ports)
Write a Bash script that displays listening ports:

* That only shows listening sockets
* That shows the PID and name of the program to which each socket belongs

### [5.Is the host on the network](./5-is_the_host_on_the_network)
Write a Bash script that pings an IP address passed as an argument.

Requirements:

* Accepts a string as an argument
* Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
* Ping the IP 5 times

