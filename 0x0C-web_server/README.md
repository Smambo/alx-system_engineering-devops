## 0x0C. Web Servers
## About:
![image](https://github.com/Smambo/alx-system_engineering-devops/assets/113464914/e33c8ccb-fd03-4ff7-a441-cfb04746e192)

* Clients are the typical web user's internet-connected devices (for example, your computer connected to your Wi-Fi, or your phone connected to your mobile network) and web-accessing software available on those devices (usually a web browser like Firefox or Chrome).

* Servers are computers that store webpages, sites, or apps. When a client device wants to access a webpage, a copy of the webpage is downloaded from the server onto the client machine to be displayed in the user's web browser.

## Tasks:
### [0. Transfer a file to your server](./0-transfer_file)
Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username `scp` connects with
  4. The path to the SSH private key that `scp` uses
* Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
* `scp` must transfer the file to the user home directory `~/`
* Strict host key checking must be disabled when using `scp`

### [1. Install nginx web server](./1-install_nginx_web_server)
Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install `nginx` on your `web-01`
* server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
* You can’t use `systemctl` for restarting `nginx`

Server terminal:

```
ubuntu@345454-web-01:~$ ./1-install_nginx_web_server > /dev/null 2>&1
ubuntu@345454-web-01:~$ 
ubuntu@345454-web-01:~$ curl localhost
Hello World!
ubuntu@345454-web-01:~$
```

Local terminal:

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$ curl 52.204.237.230/
Hello World!
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$ curl -sI 52.204.237.230/
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 28 Nov 2023 15:14:55 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Tue, 28 Nov 2023 15:13:47 GMT
Connection: keep-alive
ETag: "656603ab-d"
Accept-Ranges: bytes

smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$
```

### [2. Setup a domain name](./2-setup_a_domain_name)

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$ cat 2-setup_a_domain_name 
smambodev.tech
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$ 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$ dig smambodev.tech

; <<>> DiG 9.18.18-0ubuntu0.22.04.1-Ubuntu <<>> smambodev.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 20273
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;smambodev.tech.			IN	A

;; AUTHORITY SECTION:
tech.			3600	IN	SOA	ns0.centralnic.net. hostmaster.centralnic.net. 362995 900 1800 6048000 3600

;; Query time: 123 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Tue Nov 28 18:07:55 SAST 2023
;; MSG SIZE  rcvd: 108

smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x0C-web_server$
```
### [3. Redirection](./3-redirection)
Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:

* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### [4. Not found page 404](./4-not_found_page_404)
Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:

* The page must return an HTTP 404 error code
* The page must contain the string `Ceci n'est pas une page`
* Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

