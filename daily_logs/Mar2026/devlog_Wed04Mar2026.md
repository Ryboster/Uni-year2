**Date: Wed 04 Mar 2026** <br>

# Activities



1am - Tried setting up DDNS. Researched how one even does that.

1:20am - Ok, so a DDNS is just a script that makes an API request to your DNS provider - that's how the IP is actually updated. ez-pz,

1:30am - Copied a script from the tutorial. Generated my godaddy API token,

1:40am - Completed the script, ran it, aaaaaand... Godaddy's API is paid. Fantastic! Enshittification at its finest,



2am - Tried sett

3am - Transferred my domain over to Cloudflare,



4:20am - Installed certbot. Generated a new SSL certificate,

4:30am - Looked for where the cert is actually applied,

4:50am - Found it! It's in my nginx.conf. Updated the path to the cert,

4:55am - Excellent! HTTPS works now!

4:56am - Tried adding certbot to cron for automatic renewal. No need. Certbot runs a systemctl process that already handles that,

<br>

# Issues/Errors

<br>

# Next Steps

<br>

## Resources

[Quick and Dirty Dynamic DNS Using GoDaddy : 4 Steps - Instructables](https://www.instructables.com/Quick-and-Dirty-Dynamic-DNS-Using-GoDaddy/)

<br>
