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
![Regex matching example](https://camo.githubusercontent.com/fdd104725d530df3b190671b37740b454cdbf734bd706394cee9164a416e6228/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f37382f6a7573742d6d617463682d486f6c626572746f6e2e706e67)

Requirements:
* The regular expression must match `School`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb School | cat -e
School$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "Best School" | cat -e
School$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$
```
### 1.Repetition Token #0
![example0](https://camo.githubusercontent.com/834505b002f228c3571fda84b51f89e7371fa7cd22883f51773c51602c266311/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f37382f72657065746974696f6e2d746f6b656e2d302e706e67)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 2.Repetition Token #1
![example1](https://camo.githubusercontent.com/c3b47d0d83c23ad66564afcfabdd49af02055e7bb51db15dd4624a8252915355/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f37382f72657065746974696f6e2d746f6b656e2d312e706e67)

Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 3.Repetition Token #2
![example2](https://camo.githubusercontent.com/3c6a06c4bf11d0bc652a4f195100ff4b257e9e2234c16ef2382c3737a99a3678/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f37382f72657065746974696f6e2d746f6b656e2d322e706e67)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 4.Repetition Token #3
![example3](https://camo.githubusercontent.com/84cc4ce7ff8d96d31cb420d74bb6ec8da678ea2a047413ded137b6c28e559a5e/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d73797361646d696e5f6465766f70732f37382f72657065746974696f6e2d746f6b656e2d332e706e67)

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

* Your regex should not contain square brackets
### 5.Not quite HBTN yet
Requirements:
* The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

```

```
### 6.Call me maybe
This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.
Requirement:
* The regular expression must match a 10 digit phone number

```

```
### 7.OMG WHY ARE YOU SHOUTING?
![Capslock Meme](https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:
* The regular expression must be only matching: capital letters

```

```
