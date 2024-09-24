ROT13 is a substitution cipher. Each character is shifted by 13 positions within the alphabet. So *A* would be mapped to *N* as such. For this level, we could use the `tr` command to create a translation dictionary and pipe the cat output of data.txt into that dictionary for translation:

```sh
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```