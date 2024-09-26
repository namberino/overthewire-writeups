Since `.bashrc` has been modified to automatically log out when we try to login. We need to be able to run command we start up the interactive shell. `ssh` allows us to do this:

```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```