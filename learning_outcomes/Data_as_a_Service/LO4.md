# LO4

## 12th November 2025

### Abstract

----------------------------------------------

Common software security approaches almost never have no implications to your software when implemented. They are usually vast and complex systems that in order to operate, need to transform the way your software works in some way. While there are many different kinds of security approaches, this rings true for most of them. Threats exploit how applications work, so in order to protect yourself against them, you need to change the way the application works. It's that simple.

This article will go into depth on some pitfalls and mitigations of common security approaches.



### Body Section

----------------------------------------------

### Reverse Proxy

A reverse proxy, in simple terms, is an intermediary server located between the end destination and the requester. Its task is to filter out bad requests before they can ever get to the final destination and cause some issues.

#### Pitfall

Since this is an intermediary server, any request made to the end application is technically made by this server. This means that the requester's IP and headers are invisible to the application. While your Nginx might see something like this on an incoming request: 

`109.666.666.6 - - [19/Nov/2025:12:31:28 +0000] "GET /favicon.ico HTTPS/1.1" 499 0 "https://www.blazejowski.co.uk/about" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0"`,

your application will always see something like this instead:

`127.0.0.1 - - [19/Nov/2025:12:31:28 +0000] "GET /favicon.ico HTTP/1.1" 499 0 "http://127.0.0.1/about" "Nginx-some-header"`

* The requester's address (109.666.666.6) will be replaced with the local address of the proxy (localhost),

* Headers will either be truncated or replaced with your proxy's default headers ("Mozilla/5.0 ..." -> "Nginx-some-header"),

* Protocol will be downgraded to HTTP even if the client reached out to your server via HTTPS,

* Port will be downgraded from 443 (https) to 80 (http),

* Host (`https://www.blazejowski.co.uk/about`) will be replaced with the address the proxy used to reach the server (`http://127.0.0.1/about`),

This might lead to a variety of different issues depending on what your application does and how. Some of the most common issues resulting from this particular pitfall are:

* The inability to generate correct absolute URLs,

* Downgrading connection to HTTP,

* Logging all traffic as localhost,

#### Mitigation

To mitigate this pitfall, Nginx can be set to always pass along client information as-is, without alteration. This involves creating a mimicked header package and can be accomplished using the following configuration in Nginx:

```nginx
location / {
			proxy_pass http://127.0.0.1:8000;
			proxy_set_header Host $host;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto https;
            proxy_set_header X-Real-IP $remote_addr;
		}
```

###### (Saunders D. 2020)

This way even though the request hadn't really come from host directly, the application doesn't know it and isn't concerned with it.



#### Pitfall

Proxies have their own buffer sizes. This means that even though your application might be well adjusted to receive or serve large files, you might still get issues such as:

* `413: Request Entity Too Large` error response,

* Truncated responses,

* Timeouts,

#### Mitigation

Your proxy buffer needs to be explicitally set to the largest size your application is able to receive/serve. In Nginx this can be accomplished with the following configuration options:

```nginx
client_max_body_size 50M;
proxy_buffering on;
```

In Nginx `proxy_buffering` is set to `off` by default. This can cause problems if the response is large or if the connection between NGINX and the client is slow, because it can result in increased memory usage and potentially lead to request timeouts. (Solo.io No date.)



#### Activity Log Scanners & Actors

Alongside proxies, web developers will also deploy tools that actively scan and act based on the activity logs produced by the proxy. One example of such framework is Fail2Ban. Using regular expressions, it allows you to identify and isolate certain requests made to the proxy and act on them. Following is an example of my Fail2Ban jail

```fail2ban
[nginx-403]
enabled = true
port = http,https
filter = nginx-403
logpath = /var/log/nginx/access.log
maxretry = 3
findtime = 600
bantime = 3600
action = iptables-multiport[name=nginx-403, port="http,https", protocol=tcp]


...
[Definition]
failregex = ^<HOST> - - \[.*\] "(GET|POST|HEAD|OPTIONS|PUT|DELETE).*" 403 .*
ignoreregex =
```

###### (Blazejowski G. 2025)

This jail is configured to catch all 403 responses and ban repeated offenders. If you got 403 3 times within 600 seconds, your IP is banned for a 3600 seconds.



#### Pitfall

because fail2ban uses regex to find harmful requests, if attacks suddenly change they will no longer be matched by the patterns. As such jails need to be updated on a constant ongoing basis to catch up with the evolution of cyber attacks. This can require substantial resources.



#### Mitigation

By using small, highly specialized AI models, jails can catch up with the attacks. While deploying them on an ongoing basis might be very cost-ineffective, they could be a healthy addition to maintenance breaks.





### Personal Experience

----------------------------------------------

[link to LO]

### References

Solo.io (No date.) NGINX configuration. Available at:  [NGINX Configuration: Directives, Examples, and 4 Mistakes to Avoid | Solo.io](https://www.solo.io/topics/nginx/nginx-configuration) (Accessed: 19 Nov 2025)

Saunders D. (12 Dec 2020) NGINX and X-Forwarded-For Header (XFF). Available at: [NGINX and X-Forwarded-For Header (XFF) | Loadbalancer](https://www.loadbalancer.org/blog/nginx-and-x-forwarded-for-header/) (Accessed: 19 Nov 2025)

Blazejowski G. (27 Oct 2025) Security Threats to my Server. Available at: [Uni-year2/reflections/security_threats_RESTfulAPI.md at main · Ryboster/Uni-year2 · GitHub](https://github.com/Ryboster/Uni-year2/blob/main/reflections/security_threats_RESTfulAPI.md) (Accessed 19 Nov 2025)



----------------------------------------------
