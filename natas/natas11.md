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
Cookie: `data:"MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5ofnh8e354bjY%3D"`

This cookie data is derived from the `$defaultdata`. The `loadData` function will decide whether to show the password or not based on the cookie data.

The cookie data is derived from `"showpassword" => "no"` so we need to set that to "yes"

So the data cookie will get run through an xor encryption algorithm:
```
plaintext ^ key = ciphertext
```

This is vulnerable to a know-plaintext attack:
```
plaintext ^ ciphertext = key
```

So let's try xor'ing the cookie with the default data. We also need to undo any processing on those data:
1. Ciphertext need to be decoded
2. Default data need to be json encoded

```php
<?
  
$cookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5ofnh8e354bjY%3D";  
  
function xor_encrypt($in) {  
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
print xor_encrypt(base64_decode($cookie));  
  
?>  
```

This will output a key, which is `KNHL`

So running the program again, this time xor'ing the data with the key, we should get the necessary cookie data to get the password

> Note: we need to set the "showpassword" to "yes"

```php
<?
  
$data = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));  
  
function xor_encrypt($in) {  
    $key = 'KNHL';  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
print base64_encode(xor_encrypt($data));  

?>
```

And we get the `showpassword` cookie data: `MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz`

Replace the cookie data in the website and refresh the website:
```js
document.cookie = "data=MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"
```

And we get: `The password for natas12 is YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG`