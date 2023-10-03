## Hey there!
## Follow me as I tackle tasks on regular expressions
## Background Context:
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ cat example.rb 
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./example.rb 127.0.0.2
127.0.0.2
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./example.rb 127.0.0.1
127.0.0.1
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./example.rb 127.0.0.a

smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$
```

## Requirements:
### General:
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
* All your regex must be built for the Oniguruma library

## Tasks:
### 0.Simply matching School
![Regex matching example](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T141609Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e20f3714365bf61cee82cf81f7d64bcffc11eee6b3f70fa0dece9939c308bb69)

Requirements:
* The regular expression must match `School`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 1.Repetition Token #0
![example0](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T141609Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c846832f3edbd4976b8c010885a0e320eb618a9d8f169820c87bfcf813cffaf)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 2.Repetition Token #1
![example1](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T141609Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea11f7132feedb2e88000eba6dcaddb5f99388d97907edccf31823f7bdcc081f)

Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 3.Repetition Token #2
![example2](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T141609Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5b7d693f9a5d8cdc50fda34a8cbec808e3ab56a33534082ad609b0b91c19394f)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 4.Repetition Token #3
![example3](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T141609Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6e8916c23b6f16c5126f28be6c3b1093047af2726de5657a0bd5ee13462a3d94)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* Your regex should not contain square brackets
### 5.Not quite HBTN yet
Requirements:
* The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 6.Call me maybe
This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.
Requirement:
* The regular expression must match a 10 digit phone number
### 7.OMG WHY ARE YOU SHOUTING?
![Capslock Meme](https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:
* The regular expression must be only matching: capital letters

