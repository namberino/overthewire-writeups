To find a file stored somewhere in the server, we need to start the search at the root directory, which is `/`. This is the *root* of the Linux filesystem. Every other directories within Linux all came from this directory or a directory that came from this directory. So we can use the `find` command for this:

```sh
find / -user bandit7 -group bandit6 -size 33c
```

However, the find command will try to access the data about every files in the server. Unless you're root, you're not going to be able to read these files and get `Permission Denied`. So what we can do is by handling the error stream of this command and redirecting it into `/dev/null`, which is kinda like a grinder, deletes everything that's thrown into it.

There's 3 streams in Linux:
```
0: stdin
1: stdout
2: stderr
```

So we can do this:

```sh
find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
```