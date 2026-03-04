**Date: Wed 04 Mar 2026** <br>

# Activities



1am - Tried setting up DDNS. Researched how one even does that.

1:20am - Ok, so a DDNS is just a script that makes an API request to your DNS provider - that's how the IP is actually updated. ez-pz,

1:30am - Copied a script from the tutorial. Generated my godaddy API token,

1:40am - Completed the script, ran it, aaaaaand... Godaddy's API is paid. Fantastic! Enshittification at its finest,

1:45am - Looked into alternative DNS providers,

1:50am - Found cloudfare. Their API is seemingly free,



2:30am - Transferred my domain over to cloudflare,

2:40am - Set everything up. Website runs,

2:50am - Created an API token,



3am - Can't justify learning Cloudflare's API just for this one thing. Used AI to rewrite my script for cloudflare,

3:10am - Ran the script and it works!

3:20am - Added the script to my crontab so my website doesn't ever go down again. Finally, no more manual IP resets!

3:30am - Found two mor





3:40am - Hmm, it seems cloudflare handles SSL certs differently. I can't use ZeroSSL anymore because the CNAME record isn't being found so I can't verify that I own the domain. Looked into alternatives,





4am - Found and installed certbot,

4:10am - Generated a new SSL certificate,

4:30am - Looked into how to actually apply the cert,

4:50am - Found it! It's in my nginx.conf. Updated the path to the cert,

4:55am - Excellent! HTTPS works again,

4:56am - Tried adding certbot to cron for automatic renewal. No need. Certbot runs a systemctl process that already handles that for me.



5:10am - Looked into solving the other issue. What I had to do on godaddy before was creating an additional parallel DNS record for requests that excluded www, let's see how it's handled on Cloudflare now,

5:15am - Added a new record with root name. Doesn't work,

5:20am - Huh, so connecting to https://blazejowski.co.uk/ DOES prepend the www, but connecting to https://blazejowski.co.uk (without the slash at the end) doesn't. Interesting,

5:25am - Removed the root name DNS record to see if that's what's doing the prepending,

5:26am - No it wasn't. Apparently it was just my browser being polite. Including the slash at the end opens up a suggestion which prepends the www.

5:28am - A-ha! Turns out you have to set a "Rule" for that in the "Rules" tab,

5:30am - Excellent! They have a thing just for that! Godaddy can go bankrupt for all I care,

![](/home/snek/Desktop/portfolio/Uni-year2/assets/2026-03-04-05-28-57-image.png)



5:40am - Huzzah! Got it to work! Now http is being redirected to https, and name requests to www.name,

5:45am - Breakfast break and then off to researching using unity in github actions,



# Issues/Errors

3:30am - Found two issues. 1. `www` is now required. 2. HTTPS doesn't work,



<br>

# Next Steps

<br>

## Resources

[Quick and Dirty Dynamic DNS Using GoDaddy : 4 Steps - Instructables](https://www.instructables.com/Quick-and-Dirty-Dynamic-DNS-Using-GoDaddy/)

https://community.cloudflare.com/t/how-to-delete-www-domain-name/236611/2

<br>
