Level password: `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`

`nmap` allows us to scan ports and get information about them. It does this by sending packets to those ports and try to see the response. Since we need to find for a port that speaks SSL, we could try the `-sV` flag with `nmap`, which allows us to probe for services. To make this go faster, we could use the `-T` flag to speed up:

```sh
nmap -sV localhost -p 31000-32000 -T5
```

Once we got the SSL port, we could try to connect to it and using `s_client` and get the password just like the previous level.

Note: make sure to use `-ign_eof` when using `s_client` to ignore EOF character.