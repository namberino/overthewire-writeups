For this, we can clone the repo using `git clone` (remember to specify port 2220):

```sh
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
```

We can check the tags using `git tag`. Tagging in git allows us to tag specific points in a repository’s history as being important. This is often used to mark release point. There's a tag called `secret`. If we use `git show` to show this tag, we can see the password:

```sh
git show secret
```