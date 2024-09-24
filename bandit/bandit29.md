For this, we can clone the repo using `git clone` (remember to specify port 2220):

```sh
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
```

We can list all the remote branches using `git branch -a`. Since there's no password in the production branch, we can check other branches. If we checkout the branch `dev`, we can see that the `README.md` file contains the password.