Level password: `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

For finding lines that can only occur once, we can use the command `uniq`, which allows us to filter for repeated line and unique lines. We can use the flag `-u` or `--unique` to filter for lines that does not repeat. However, `uniq` can only filter for repeated lines that are adjacent, so before we use uniq, we need to sort first. To sort, we could just use `sort`:

```sh
sort data.txt | uniq -u
```