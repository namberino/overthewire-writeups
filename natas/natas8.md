This page has an input field and submit button along with a view source code link (similar to natas6)

The source code looks a bit like this:
```php
<?      

$encodedSecret = "3d3d516343746d4d6d6c315669563362";      

function encodeSecret($secret) {       
	return bin2hex(strrev(base64_encode($secret)));   
}      

if(array_key_exists("submit", $_POST)) {       
	if(encodeSecret($_POST['secret']) == $encodedSecret) {       
		print "Access granted. The password for natas9 is <censored>";       
	} else {       
	print "Wrong secret";       
	}   
}

?>
```

So the input will get put through an `encodeSecret` function and compared to `$encodedSecret`

So to get the secret passphrase, we just need to run the `$encodedSecret` variable through the `encodeSecret` function in reverse. So I whipped up a quick php script:
```php
<?

function decodeSecret($secret) {
	return base64_decode(strrev(hex2bin($secret)));
}

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

print decodeSecret($encodedSecret);

?>
```

When I run this script, I get the secret: `oubWYf2kBq`

So putting this into the input field and submitting, I get this:
```html
Access granted. The password for natas9 is Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
```