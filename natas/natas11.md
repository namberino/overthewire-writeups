We have a longer source code for this level:
```php
<?      

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");      

function xor_encrypt($in) {    
	$key = '<censored>';    
	$text = $in;    
	$outText = '';    
	
	// Iterate through each character    
	for($i=0;$i<strlen($text);$i++) {    
		$outText .= $text[$i] ^ $key[$i % strlen($key)];       
	}          
	
	return $outText;
}      

function loadData($def) {       
	global $_COOKIE;    
	$mydata = $def;       
	
	if(array_key_exists("data", $_COOKIE)) {
		$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);       
		
		if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
		if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
			$mydata['showpassword'] = $tempdata['showpassword'];
			$mydata['bgcolor'] = $tempdata['bgcolor'];
		}
	}
	}       
	return $mydata;   
}

function saveData($d) {
	setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);   

if(array_key_exists("bgcolor",$_REQUEST)) {
	if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
		$data['bgcolor'] = $_REQUEST['bgcolor'];       
	}   
}      

saveData($data);            

?>
```
Cookie: `data:"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"`

Let's break this down and see how we can get the password of the next level.

We need to get the correct cookie to get the password for this level. The cookie that the level gave us is derived from `$defaultdata`.

```php
`$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");`
```

The field `showpassword` is set to `no`. To get the key for the next level, we need to set this field to `yes`. That's the easy part, the hard part is the encryption.

```php
function loadData($def) {       
	global $_COOKIE;    
	$mydata = $def;       
	
	if(array_key_exists("data", $_COOKIE)) {
		$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);       
		
		if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
		if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
			$mydata['showpassword'] = $tempdata['showpassword'];
			$mydata['bgcolor'] = $tempdata['bgcolor'];
		}
	}
	}       
	return $mydata;   
}
```

This function will load in the cookie along with the `$defaultdata`. It checks to see if the cookie contains the data. If it does, then it would try to decode the data.

```php
function saveData($d) {
	setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
```

This function saves the data from the `loadData` function into the cookie. For this level, we need to somehow reverse engineer the key used in the xor operation. We could do this using the plaintext attack:

```
plaintext ^ key = ciphertext
plaintext ^ ciphertext = key
```

In this case, the plaintext is the `$defaultdata` and the ciphertext is the cookie. Since the cookie has been base64 encoded, we'll first need to decode that before running the xor algorithm to derive the key:

```php
$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D";
	 
function get_xor_key($ciphertext) {
	$plaintext = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
	$key = '';
   
	for($i = 0; $i < strlen($ciphertext); $i++) {
		$key .= $ciphertext[$i] ^ $plaintext[$i % strlen($plaintext)];
	}
 
	return $key;
}
 
 $xorKey = get_xor_key(base64_decode($cookie));
 print $xorKey;
```

The json encoding is fine to have, it makes the xor operations easier. From this, we derived the key `eDWo`. With this key, we could run the xor algorithm on a modified `$defaultdata` with the `showpassword` field set to `yes`:

```php
$plaintext = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));

function xor_encrypt($plaintext) {
	$key = "eDWo";
	$ciphertext = '';
	
	for($i = 0; $i < strlen($plaintext); $i++) {
		$ciphertext .= $plaintext[$i] ^ $key[$i % strlen($key)];
	}
	
	return $ciphertext;
}

print base64_encode(xor_encrypt($plaintext));
```

This gives us the correct cookie value. If we replace the cookie that we got with the new cookie and reload the page, we get the natas12 password: `yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`.