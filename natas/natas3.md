Opening the inspect tool, we see there's nothing on this page. There is this rather suspicious comment though:

```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```

So that got me thinking about search engine. I decided to look up how websites tell search engines which file to index and which to avoid. Turns out that is done via a file called `robots.txt`, so I tried look at the `robots.txt` file: http://natas3.natas.labs.overthewire.org/robots.txt

```txt
User-agent: *
Disallow: /s3cr3t/
```

So this file is telling the search engine to ignore the `/s3cr3t/` directory, so I checked it out and found there's a `users.txt` file in there, inside that file is the password for natas4