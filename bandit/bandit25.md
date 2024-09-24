This level is a little tricky.

Each user will have a default startup shell. Since bandit26's shell is something other than `/bin/bash`, we need to figure out what it is first. We could do this by reading `/etc/passwd`, which contains information about each user. The `passwd` file have 7 fields, each separated by a colon `:`:

```
cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```

This is what each of the fields mean:
1. Username.
2. Password (an `x` indicates that the encrypted and salted password is stored in `/etc/shadow`).
3. User ID (UID). UID 0 is reserved for *root* and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
4. Group ID (GID). The primary group ID (stored in `/etc/group`).
5. User ID Info (GECOS). The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by `finger` command (user info lookup command).
6. Home directory. This is where the user will be when they login. If it doesn't exist, the user directory becomes `/`.
7. Shell. The absolute path of a command or shell.

So the shell is called `showtext`. We could check out what this executable does:

```sh
cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

This uses the `more` command on the text.txt file and exit. When we login, it executes the above script and exit. Since the text.txt is pretty small, `more` displays it without going into interactive mode. If we make the window smaller, `more` will go into interactive mode, allowing us to access vim by pressing `v`.

Once we're in vim, we could read the password by using `:r /etc/bandit_pass/bandit26`. This vim command reads the file and output the content of the file to the current file being edited in vim.