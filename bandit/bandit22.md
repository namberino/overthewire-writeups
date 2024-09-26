Level password: `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

Same first part here. But now, the script for bandit23 is different:

```sh
cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

So this is grabbing the username of the current user, hashing the name and remove some delimiters to create a target `/tmp/` filename. What we could do is run that hash command but with the name *bandit23* so that we could get the `/tmp/` filename for bandit23. That's where the password of bandit23 is copied to:

```sh
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
```

Then grep the `/tmp/` file for the password.