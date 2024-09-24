For this, we can clone the repo using `git clone` (remember to specify port 2220):

```sh
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
```

Firstly, we can run `git log` in order to see the commits and what has been changed. We saw that one commit has a commit message saying "fix info leak". This means they probably removed the password in that commit.

We could check the modifications done in that commit by using `git show` with the hash of the commit:

```sh
git show hash_of_commit
```