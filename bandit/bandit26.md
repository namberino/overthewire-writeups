Level password: `s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ`

Once we're in Vim, we could set the shell option in Vim to be different shell with `:set shell=/bin/bash`. Once we have that, we can use the shell with `:shell`. Then we just use the setuid executable to grab the password:

```sh
./bandit27-do cat /etc/bandit_pass/bandit27
```