## Hey there!
## Follow me as I tackle tasks on processes and signals
## Tasks:
### 0.What is my PID
Write a Bash script that displays its own PID.
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./0-what-is-my-pid 
20592
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 1.List your processes
Write a Bash script that displays a list of currently running processes.
Requirements:
* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./1-list_your_processes | head -50
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           2  0.0  0.0      0     0 ?        S    09:46   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [netns]
root           8  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kworker/0:0H-events_highpri]
root          10  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [mm_percpu_wq]
root          11  0.0  0.0      0     0 ?        I    09:46   0:00  \_ [rcu_tasks_kthread]
root          12  0.0  0.0      0     0 ?        I    09:46   0:00  \_ [rcu_tasks_rude_kthread]
root          13  0.0  0.0      0     0 ?        I    09:46   0:00  \_ [rcu_tasks_trace_kthread]
root          14  0.0  0.0      0     0 ?        S    09:46   0:01  \_ [ksoftirqd/0]
root          15  0.0  0.0      0     0 ?        I    09:46   0:21  \_ [rcu_preempt]
root          16  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [migration/0]
root          17  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [idle_inject/0]
root          19  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [cpuhp/0]
root          20  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [cpuhp/1]
root          21  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [idle_inject/1]
root          22  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [migration/1]
root          23  0.0  0.0      0     0 ?        S    09:46   0:01  \_ [ksoftirqd/1]
root          25  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kworker/1:0H-events_highpri]
root          26  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [cpuhp/2]
root          27  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [idle_inject/2]
root          28  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [migration/2]
root          29  0.1  0.0      0     0 ?        S    09:46   0:37  \_ [ksoftirqd/2]
root          31  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kworker/2:0H-events_highpri]
root          32  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [cpuhp/3]
root          33  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [idle_inject/3]
root          34  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [migration/3]
root          35  0.0  0.0      0     0 ?        S    09:46   0:03  \_ [ksoftirqd/3]
root          37  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kworker/3:0H-events_highpri]
root          38  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [kdevtmpfs]
root          39  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [inet_frag_wq]
root          40  0.0  0.0      0     0 ?        S    09:46   0:10  \_ [kauditd]
root          41  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [khungtaskd]
root          43  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [oom_reaper]
root          45  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [writeback]
root          46  0.2  0.0      0     0 ?        S    09:46   0:45  \_ [kcompactd0]
root          47  0.0  0.0      0     0 ?        SN   09:46   0:00  \_ [ksmd]
root          49  0.0  0.0      0     0 ?        SN   09:46   0:00  \_ [khugepaged]
root          50  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kintegrityd]
root          51  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [kblockd]
root          52  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [blkcg_punt_bio]
root          54  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [tpm_dev_wq]
root          55  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [ata_sff]
root          56  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [md]
root          57  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [edac-poller]
root          58  0.0  0.0      0     0 ?        I<   09:46   0:00  \_ [devfreq_wq]
root          59  0.0  0.0      0     0 ?        S    09:46   0:00  \_ [watchdogd]
root          60  0.0  0.0      0     0 ?        I<   09:46   0:07  \_ [kworker/1:1H-kblockd]
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 2.Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
Requirements:
* You cannot use `pgrep`
* The third line of your script must be `# shellcheck disable=SC2009`(for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./2-show_your_bash_pid 
smambo     25916  0.0  0.1  11528  4736 pts/0    Ss   17:02   0:00 bash
smambo     26672  0.0  0.0   9968  3200 pts/0    S+   17:15   0:00 bash ./2-show_your_bash_pid
smambo     26674  0.0  0.0   9076  2432 pts/0    S+   17:15   0:00 grep bash
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 3.Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
Requirements:
* You cannot use `ps`
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./3-show_your_bash_pid_made_easy 
25916 bash
27570 bash
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./3-show_your_bash_pid_made_easy 
25916 bash
27572 bash
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 4.To infinity and beyond
Write a Bash script that displays `To infinity and beyond` indefinitely.
Requirements:
* In between each iteration of the loop, add a `sleep 2`
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
You'll note that I killed the script in the above example with `Ctrl+C`.
### 5.Don't stop me now!
We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.
Write a Bash script that stops `4-to_infinity_and_beyond` process.
Requirements:
* You must use `kill`

Terminal #0

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
Terminal #1
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./5-dont_stop_me_now 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `5-dont_stop_me_now`. We can then see in terminal #0 that my process has been terminated.
### 6.Stop me if you can
Write a Bash script that stops `4-to_infinity_and_beyond` process.
Requirements:
* You cannot use `kill` or `killall`

Terminal #0

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
Terminal #1
```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./6-stop_me_if_you_can 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 7.Highlander
Write a Bash script that displays:
* `To infinity and beyond` indefinitely
* With a `sleep 2` in between each iteration
* `I am invincible!!!` when receiving a `SIGTERM` signal
Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

Terminal #0

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
^C
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```

Terminal #1

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./67-stop_me_if_you_can 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./67-stop_me_if_you_can 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./67-stop_me_if_you_can 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
### 8.Beheaded process
Write a Bash script that kills the process `7-highlander`.

Terminal #0

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```

Terminal #1

```
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./8-beheaded_process 
smambo@lenovo-ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
```
