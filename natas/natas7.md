For this page, there's a `Home` button and an `About` button. Clicking either of the button will bring us to the `index.php?page=<page_name>` page. Opening the inspector page, there's a comment giving us some hint:
```html
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

So I changed the page URL variable to `/etc/natas_webpass/natas8`: http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

This gives us the password for natas8: `a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB`