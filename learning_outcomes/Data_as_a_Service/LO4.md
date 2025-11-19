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

To mitigate this pitfall, Nginx can be set to always pass along client information as-is, without alteration.

```nginx
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header Host $host;
```

#### Pitfall

Proxies have their own limits on the size of requests made. This means that even though your application might be well adjusted to receive or serve large files, you might still get issues such as:

* `413: Request Entity Too Large` error response,

* Truncated responses,

* Timeouts,

#### Mitigation

As such, your proxy's buffer needs to be explicitally set to the largest size your application is able to receive/serve:

```nginx
client_max_body_size 50M;
```

Or proxy bufferring might need to be turned on for data streams:

```nginx
proxy_buffering off;
```







#### Activity Log Scanners & Actors









### Personal Experience

----------------------------------------------

[link to LO]

### References

----------------------------------------------
