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

`109.666.666.6 - - [19/Nov/2025:12:31:28 +0000] "GET /favicon.ico HTTP/1.1" 499 0 "https://www.blazejowski.co.uk/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0"`,

your application will always see something like this instead:

`127.0.0.1 - - [19/Nov/2025:12:31:28 +0000] "GET /favicon.ico HTTP/1.1" 499 0 "https://www.blazejowski.co.uk/" "Nginx-some-header"`

The address will be replaced with the local address of the proxy, and headers will either be truncated, or replaced with your proxy's default headers.

#### Mitigation





#### Pitfall



#### Mitigation





#### Activity Log Scanners & Actors









### Personal Experience

----------------------------------------------

[link to LO]

### References

----------------------------------------------
