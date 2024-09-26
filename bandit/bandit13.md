Level password: `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

SSH contains these step when initiating connection:
- Client initiates connection with server
- Server sends back a public key
- Server and client negotiate parameters and open a secure channel
- User can login
- Each packets that the user sends will be encrypted using the public key and the server can decrypt it using its private key

Since we have the private RSA login key. We could use the identity flag of ssh `-i` to read the key and authenticate:

```sh
ssh -i sshkey.private bandit14@localhost -p 2220
```