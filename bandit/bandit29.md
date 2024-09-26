Level password: `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

For this, we can clone the repo using `git clone` (remember to specify port 2220):

```sh
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
```

We can list all the remote branches using `git branch -r`. Since there's no password in the production branch, we can check other branches. If we checkout the branch `dev` using git checkout, we can see that the `README.md` file contains the password.