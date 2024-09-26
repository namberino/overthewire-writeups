Level password: `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

This level is pretty simple, we just read the file `data.txt` and try to grep the word *millionth*.

```sh
cat data.txt | grep millionth
```

Alternatively, the `grep` command can also read the file:

```sh
grep millionth data.txt
```