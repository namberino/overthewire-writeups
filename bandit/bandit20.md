For this, we could use `netcat` to transmit the signal to a port and also listen to the output. We could use the `-l` flag to listen and the `&` to let the process run in the background. We also use `-p` which connects to a local port, so no need to specify localhost. Remember to use `-n` with echo to remove the trailing characters such as carriage return or newline:

```sh
echo -n "current_level_password" | nc -l -p 1234 &
```

Then we could run the given binary and connect to port `1234` to receive the password:

```sh
./suconnect 1234
```