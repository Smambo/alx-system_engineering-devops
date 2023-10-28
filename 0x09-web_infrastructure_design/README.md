# Web infrastructure design
![image](https://github.com/Smambo/alx-system_engineering-devops/assets/113464914/5ac7849d-b373-4a2c-af51-25855635cda2)

# Tasks:
### [0. Simple web stack](./0-simple_web_stack)
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29).

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:

* You must use:
  * 1 server
  * 1 web server (Nginx)
  * 1 application server
  * 1 application files (your code base)
  * 1 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
Requirements:

* You must add:
  * 2 servers
  * 1 web server (Nginx)
  * 1 application server
  * 1 load-balancer (HAproxy)
  * 1 set of application files (your code base)
  * 1 database (MySQL)

### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

* You must add:
  * 3 firewalls
  * 1 SSL certificate to serve `www.foobar.com` over HTTPS
  * 3 monitoring clients (data collector for Sumologic or other monitoring services)

### [3.Scale up](./3-scale_up)
Readme

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

Requirements:

* You must add:
  * 1 server
  * 1 load-balancer (HAproxy) configured as cluster with the other one
  * Split components (web server, application server, database) with their own server

