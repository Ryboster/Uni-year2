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



The address will be replaced with the local address of the proxy, and headers will either be truncated, or replaced with your proxy's default headers. 

Besides logging, this might lead to further issues such as the inability to generate correct absolute URLs. In order to generate an absolute URL, applications will sometimes  grab the IP address 



#### Mitigation





#### Pitfall



#### Mitigation





#### Activity Log Scanners & Actors









### Personal Experience

----------------------------------------------

[link to LO]

### References

----------------------------------------------
