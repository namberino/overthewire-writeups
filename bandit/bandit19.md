*setuid* (along with *setgid*) allows us to run executables with the permissions of the executable's owner (or group for *setgid*). They are often used to allow users on a computer system to run programs with temporarily elevated privileges to perform a specific task. While the assumed UID or GID privileges provided are not always elevated, at a minimum they are specific.

Let's see what each piece of data in `ls -la` mean, which can tell us a lot about permissions:

```sh
ls -la
drwxr-xr-x nam staff 384 B Thu Aug  8 15:49:58 2024 .
drwxr-xr-x nam staff 608 B Mon Aug  5 12:46:13 2024 ..
.rw-r--r-- nam staff  50 B Tue Jul 23 11:02:11 2024 README.md
```

The first part tells us whether it's a file or a directory, then it tells us the permission for the owner, group, and other respectively. Then it's the name of the owner user, then the name of the owner group. Then the size, then the date it was last modified. Then finally is the name.

For this level, we have execute permission for this setuid executable. So we could execute this and run the `cat` command to get the password for the next level:

```sh
./bandit20-do cat /etc/bandit_pass/bandit20
```