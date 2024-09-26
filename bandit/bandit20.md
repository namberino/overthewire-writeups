Level password: `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

For this, we could use `netcat` to transmit the signal to a port and also listen to the output. We could use the `-l` flag to listen and the `&` to let the process run in the background. We also use `-p` which connects to a local port, so no need to specify localhost:

```sh
echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 4444 &
```

Then we could run the given binary and connect to port `4444` to receive the password:

```sh
./suconnect 4444
```