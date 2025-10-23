Hello,
I'm going to present my developer profile API,
let's get to it.
[next slide]
First off, the project is available on github, and it is also hosted on world wide web. The URLs to both are displayed here.
[next slide]
The application features both headed and headless versions.
The API is accessible by prepending the target endpoint with /api. Here is an example ofthat.
[next slide]
It is fully REST compliant. 
It transfers representations of site resources in JSON format.
Every endpoint explicitly imposes methods.
Every response includes a status code.
All requests for the same resource have a uniform identifier -it's the method that dictates the action.
The server is completely independent of the client and vice versa. The only information the client needs is the URI.
every response includes explicit information about caching permissions.
Neither the server nor the client need to be aware of whether they communicate with the end application or an intermediary.
The JSON responses include URLs to further actions to allow manipulation of resources without the knowledge of the website's architecture.
[next slide]
The application is fully documented. Including purpose, setup, directory structure, endpoints, and API.
It also includes inline comments to ease code inspection and extension.
[next slide]
It includes a simple test suite that tests the API's endpoints with GET methods.
[next slide]
The application incorporates two tables; Feedbacks, and Projects complete with a crud.
[next slide]
In future, I'd like to make this website more useful to me. 
I had quite a lot of fun developing it, and would like to see it grow some more.
I think it's a fantastic place for posting all of the things I do, and for collecting user data.
It would also be cool to integrate it into my other applications such as my electronic journal,
my video game website, or a personal blog.
