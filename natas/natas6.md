This page has an input and a submit button, along with a view source code button. So I just clicked on the view source code button, and I found this interesting snippet of code:
```php
`<?      
include "includes/secret.inc";          

	if(array_key_exists("submit", $_POST)) {           if($secret == $_POST['secret']) {           print "Access granted. The password for natas7 is <censored>";       
		} else {           
			print "Wrong secret";       
		}
	}   
?>`
```

So this is importing something from `includes/secret.inc`, probably the passphrase to get the password. So I checked the http://natas6.natas.labs.overthewire.org/includes/secret.inc page. It was blank though. But checking the inspection page gives me this:
```html
<!--? $secret = "FOEIUWGHFEEUHOFUOIU"; ?-->
```

So I just copied the secret and entered it into the input:
```html
Access granted. The password for natas7 is jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
```