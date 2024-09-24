If we try to access this shell, we're put into an uppercase shell. Anything we type into this shell is uppercased, meaning we can't type any commands.

Linux has variables:
- Local variables (valid in current shell)
- Shell variables (set up by shell)
- Environment variables (valid systemwide)

These variables have uppercase names. We can use `echo $VAR_NAME` to see the variable.

Some common that are good to know are:
- `TERM`:  current terminal emulation
- `HOME`: the path to home directory of currently logged in user
- `LANG`: current locales settings
- `PATH`: directory list to be searched when executing commands
- `PWD`: pathname of the current working directory
- `SHELL` / `0`: the path of the current user’s shell
- `USER`: currently logged-in user

So to solve this level, we could just type in `$SHELL` or `$0` to enter a shell. Once we've entered a shell, we can cat the `README.txt`, which gives us the ending text.