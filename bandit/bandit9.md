For filtering for human-readable strings, we could use the command `strings`, which filter for printable characters. Printable characters are usually ASCII or Unicode characters. We could also grep for the *=* signs:

```sh
strings data.txt | grep =
```