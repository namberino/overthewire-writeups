Level password: `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`

Since `.bashrc` has been modified to automatically log out when we try to login. We need to be able to run command we start up the interactive shell. `ssh` allows us to do this:

```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 -t 'cat readme'
```

Normally, `ssh` will allocate a terminal only when it detects that the input is coming from a terminal (like when you use `ssh` interactively). `-t` ensures the terminal is always allocated, useful for running commands that require a terminal.