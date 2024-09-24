![[base64-table.png]]

Base64 is a binary to text encoding algorithm. It transform binary data into printable characters. Each group of 6 bits are converted into a corresponding character in the Base64 table.

For this level, we could use the `base64` command with the `-d` flag to decode the text:

```sh
base64 -d data.txt
```