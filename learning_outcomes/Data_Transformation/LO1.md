# LO 1

## 22nd October 2025

### Abstract

Software performance is affected by many different factors. One of those factors is the way we store, organize, and transform data used by our applications. In this article I will analyze and evaluate the way I handled data in some of my applications.

### Body Section

First, to get our definitions straight, what is data? And what does it mean to organize and transform it?

data is raw information without context or meaning. This includes things like numbers, letters, strings, or collections of things. It is the crudest form of information that is used by applications. An example of data could be any raw value stored by itslef or inside an array or other collection of data, e.g. `[1,4,32,11]`, `"{"animal": "dog", "name": "Terry"}"`, or `3.14159`. 

To organize data means to sort, structure, or group it in some way. For example `[1,2,3,4]`, `{"user_ID": 1, "user_name": "Terry" ...}`, or `["a", "b", "c"]`, are all examples of organized data. Without contextualizing it, we can organize it in a certain way, be it by order, association, or otherwise. 

To transform data means to alter it in some way. For example, we might want to transform the number `1` into `"1"` - This is an example of casting. Without changing the data itself, we've transformed it into something fit for different purpose. The goal of transformation is to prepare the data for a transition of some sort. For example, we might want to read an integer value from a sensor, and then print it. To do that, we'd need to transform the data from `integer` to `string`.



#### So what?

The way we store, organize, and transform our data, can have a profound effect on the performance of our applications. Consider the following example:

```python
@app.route('/projects', methods=["GET", "POST"])
def projects():
    if request.method == "GET":
        with open("projects.json", "r") as file:
            data = json.load(file)
        return render_template("projects.html", data=data)
    
    elif request.method == "POST":
        new_data = request.form["data"]
        with open("projects.json", "w") as file:
            json.dump(new_data, file)
        return "Data updated!"

```

In this example, we have to read and parse a `json` file everytime our user visits the page. 



```python

with open("projects.json", "r") as file:
    projects_data = json.load(file)

@app.route('/projects', methods=["GET", "POST"])
def projects():
    global projects_data
    
    if request.method == "GET":
        # Fast access: no repeated file I/O
        return render_template("projects.html", data=projects_data)
    
    elif request.method == "POST":
        # Transform incoming data (string -> Python dict)
        new_project = json.loads(request.form["data"])
        
        # Organize: append to existing list
        projects_data.append(new_project)
        
        # Save periodically or asynchronously, not every time
        with open("projects.json", "w") as file:
            json.dump(projects_data, file, indent=2)
        
        return "Project added successfully!"

```

### Personal Experience



### References


