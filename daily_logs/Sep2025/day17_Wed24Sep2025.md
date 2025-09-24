**Date: Wed 24 Sep 2025**<br>

# Activities

4:30am - Wakey wakey.

5am - Got to work on solving the navigation problem on my site. First, I need a `base` template that the `diaries` template extends. Then, I need to broaden (add another thing to) the context with the all the endpoints from the registry.

5:30am - Added the `base.html` template. extended my `diaries.html` template with it. Added a `populate_endpoints.js` script to my `base.html` for populating the navbar. Now onto contextualizing the registry.

6am - Added a new class `Registry_Reader` for reading the registry and generating context objects on behalf of other classes.

```python
class Registry_Reader(CRUD):
    def __init__(self):
        super().__init__()
        self.CONTEXT_REGISTRY = {}
        
    def ReadRegistry(self):
        registry = self.Read_DB(self.REGISTRY_DB_FILENAME, "All_Logs")        
        for record in registry:
            self.CONTEXT_REGISTRY[record[0]] = {}
            self.CONTEXT_REGISTRY[record[0]]["Filename"] = record[1]
            self.CONTEXT_REGISTRY[record[0]]["Name"] = record[2]
            self.CONTEXT_REGISTRY[record[0]]["Template"] = record[3]
```

6:30am - `Registry_Reader` now inherits from `CRUD`, and higher level classes like `Diary` (a class responsible for rendering `diaries` saved in the database) inherit from `Registry_Reader`. All constants relating to the databases are now saved in the `CRUD` and inherited by other classes. This makes the code a lot more maintainable.

```python
class CRUD():
    def __init__(self):
        self.DB_EXTENSION = ".sqlite3"
        self.DATABASES_ROOT_DIR = "Databases"
        self.REGISTRY_DB_FILENAME = "Registry"
        self.createDatabases()
        self.initializeDatabases()
```

7am - Successfuly contextualized the registry and passed it over to `base.html`. Got to work on `populate_endpoints.js` script to populate the navbar with endpoints to different logs.

7:20am - Researched collapsibles.

7:30am - Breakfast break.

8:30am - Back to researching collapsibles and figuring out how they work.







# Issues/Errors

<br>

# Next Steps

<br>

## Resources

[Django extends Tag](https://www.w3schools.com/django/django_tags_extends.php)

[How do I check if an array includes a value in JavaScript? - Stack Overflow](https://stackoverflow.com/questions/237104/how-do-i-check-if-an-array-includes-a-value-in-javascript)

[JavaScript Array push() Method](https://www.w3schools.com/jsref/jsref_push.asp)

[How To Create a Collapsible](https://www.w3schools.com/howto/howto_js_collapsible.asp)




<br>

### base.html

```html
<!DOCTYPE html>
<head>
    {% load static %}
    {{ registry|json_script:"registry"}}

    {% block head %}
    {% endblock head %}
    <script src="{% static 'moods/js/populate_endpoints.js' %}"></script>
</head>

<body>
    {% block body_precontent %}
    {% endblock body_precontent %}

    <div id="background" class="background">
        <div id="navbar" class="navbar" style="display: flex; flex-direction: column;"> 

        </div> 
        <div id="pageContent" class="pageContent">
            <ul id="pageContentList" class="pageContentList">
            </ul>
        </div>
        <div id="filler" class="filler"> 
        </div>
    </div>
    
    {% block body_postcontent %}
    {% endblock body_postcontent %}
</body>

<footer>
    {% block footer %}
    {% endblock footer %}
</footer>
</html>
```
