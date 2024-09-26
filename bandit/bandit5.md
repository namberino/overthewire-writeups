Level password: `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

For finding a file that meets all these requirements, we can use the `find` command. Then we can use the `-exec` flag to execute a command right after we find the files. We can use the same approach as *bandit4* and look for ASCII files.

```sh
find . -type f -size 1033c ! -executable -exec file {} + | grep ASCII
```