# Apache CGI for [pug](https://pugjs.org/) and [jade](http://jade-lang.com)

A simple dynamic compiler for pug that uses Apache's CGIs. It will interpret anything ending in .pug and return it as html. 

# Installation

Copy pug.cgi to a shared library location. I generally stick mine in 

``` bash
/usr/lib/cgi-bin/
```

Be sure to add +x to it so it can be ran as a script

``` bash
chmod +x pug.cgi
```

From there edit your apache.conf (typically in /etc/apache2) and add these lines:

``` 
<Directory "/usr/lib/cgi-bin">
  AllowOverride None
  Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
  Order allow,deny
  Allow from all
<Directory>

AddHandler pugpage .pug
AddHandler pugpage .jade
Action pugpage /cgi-bin/pug.cgi
```

Restart apache and you should now be able to interpret pug files. I like to add index.pug as a recognized DirectoryIndex in my virtualhosts, here's an example:

```
<VirtualHost *:80>
  ServerName example.com
  ServerAlias example.com *.example.com
  DocumentRoot /var/www
  DirectoryIndex index.pug index.jade index.html
  <Directory "/var/www">
    AllowOverride All
    Options FollowSymLinks
    Allow from All
    Options +ExecCGI
  </Directory>
</VirtualHost>
```

# Performance

Performance isn't tremendously great simply because it has to initialize on every render. This adds a good 300ms to your page response time. Not terrible for development, but if you're running this on production servers I'd hide it behind varnish or nginx set up as a reverse proxy to cache the pages. 

# TODO

Currently fails non-gracefully (just shows an error page if a page wasn't interpreted correctly). I gotta set it up to display errors. 
