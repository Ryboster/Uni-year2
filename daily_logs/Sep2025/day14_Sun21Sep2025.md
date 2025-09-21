**Date: Sun 21 Sep 2025**<br>

# Activities

12pm - Finally managed to get into my raspberry pi 4. 

12:30pm - Connected to it via ssh. Looked at my websites.

1pm - Started analyzing the database schema of my `djalio` web app.

1:30pm - Referencing Charles' resources, I went ahead and replicated the schema in MySQL Workbench. Started upgrading it to NF3.

3pm - Upgraded my database design from UNF to NF3.

![Screenshot from 2025-09-21 15-14-37.png](../assets/29430245180b197ac1b12d7bb0701c496aaaf22b.png)

4:40pm - Started implementing the new database schema.

9:50pm - Managed to implement most of it but fell short of full rework. Will finish tomorrow.

<br>

# Issues/Errors

9:50pm - My code is incredibly spaghetti. Database structure was baked into the actual HTML and javascript. I allieviated this issue a little bit by extracting and processing the data in the backend and wrapping the output in a scalable boilerplate dictionary object that is then passed to the frontend. Now frontend doesn't really care about what's going on in the actual database as long as it gets a dictionary object with the keys `Date`, `Description`, and so on.

Another thing that also helped a lot here is storing atomic data rather than 



# Next Steps

* Finish database rework.

* Plan extensions for websites (additional endpoints).

* Consider publishing website.

* Open PR for ticket in SL.

* Spend some time on IBM learning.

* Write reflection on database upgrade.

<br>

## Resources

<br>
