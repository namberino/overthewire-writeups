Level password: `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

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
- `SHELL`: the path of the current user’s shell
- `0`: the name of the script currently being executed
- `USER`: currently logged-in user

So to solve this level, we could just type in `$0` to enter a shell. Once we've entered a shell, we can cat the `README.txt`, which gives us the ending text.

The reason why `$0` works even though it gives us the name of the currently executing script is because the uppercase shell is an executable that I assume is using `bash -c` to execute the commands. And example of how the shell could work is this:

```
while (true)
{
  print(">> ");
  cmd = to_upper(input());
  print(execute("bash", "-c", cmd));
}
```

`-c` executes any command passed into it with bash with the script name being the shell itself. 

```sh
bash -c 'echo $0'
bash
```

So if we just pass `$0` into it, we would run the bash shell:

```sh
bash -c '$0'
bash-5.2$
```