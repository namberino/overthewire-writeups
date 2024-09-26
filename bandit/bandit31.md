Level password: `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

For this, we can clone the repo using `git clone` (remember to specify port 2220):

```sh
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
```

The `README.md` specifies that we need to create a `key.txt` file and push it to the repository. If we try to push the file now, we can't because the `.gitignore` is preventing it

```sh
cat .gitignore
*.txt
```

Then we can add and push using the `-f` flag to force add:

```sh
git add -f .
git commit -m "Add key.txt"
git push -u origin master
```