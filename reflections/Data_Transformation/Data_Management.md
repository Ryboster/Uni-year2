# What is effective data management?

## 22nd October 2025

### Abstract

Software performance is affected by many different factors. One of those factors is the way we store, organize, and transform our data. By leveraging the way our data is managed and manipulated, and by adhering to industry-standard processes, methods, and techniques, we can vastly improve the quality and performance of our software.

This article includes analyses and evaluations of different ways to store, organize, and transform data.

### Body Section

First, to get our definitions straight, what is data? And what does it mean to organize and transform it?

data is raw information without context or meaning. This includes things like numbers, letters, strings, or collections of things. It is the crudest form of information that is used by applications. An example of data could be any raw value stored by itslef or inside an array or other collection of data, e.g. `[1,4,32,11]`, `"{"animal": "dog", "name": "Terry"}"`, or `3.14159`. 

To organize data means to sort, structure, or group it in some way. For example `[1,2,3,4]`, `{"user_ID": 1, "user_name": "Terry" ...}`, or `["a", "b", "c"]`, are all examples of organized data. Without contextualizing it, we can organize it in a certain way, be it by order, association, or otherwise. 

To transform data means to alter it in some way. For example, we might want to transform the number `1` into `"1"` - This is an example of casting. Without changing the data itself, we've transformed it into something fit for different purpose. The goal of transformation is to prepare the data for a transition of some sort. For example, we might want to read an integer value from a sensor, and then print it. To do that, we'd need to transform the data from `integer` to `string`.

Applications are said to robustly manage their data when the number of transformations is minimized, data is well and sensibly organized at every step of the process, and it is stored in a fitting format (e.g. `.sqlite3` instead of `j.son` when storing large quantities of structured data)

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

In this example, we have to read and parse our `json` file everytime our user visits the page. We increase the number of I/O operations, perform unnecessary conversions between python objects and json, and increase the risk of data corruption by allowing simultaneous writing and reading. Following is an improved version of this:

```python
with open("projects.json", "r") as file:
    projects_data = json.load(file)

@app.route('/projects', methods=["GET", "POST"])
def projects():
    global projects_data

    if request.method == "GET":
        ### Eliminates unnecessary conversion. Reduces data corruption risk
        return render_template("projects.html", data=projects_data)

    elif request.method == "POST":
        new_project = json.loads(request.form["data"])
        projects_data.append(new_project)
        return "Project added successfully!"

def periodic_save():
        with open("projects.json", "w") as file:
            json.dump(projects_data, file)
```

Here, we minimized conversions by storing our temporary data in a python object, vastly reduced the number of I/O operations, and eliminated the risk of data corruption by fully controlling when our json file is being read, and written.

With this simple change in how we store and transform our data, we've already vastly improved the scalability and performance of our application, and secured it against the natural consequence of popularity (simultaneous read and write).

But, this example can still be improved further,

### Databases

Imagine you have a large `.json` file called "collaborations" for storing the projects you collaborated on. The file has multiple project items, each with a detailed description of the project, expressed in key-value pairs, e.g.

```json
{
    "Thought Police Chip": {"Date Completed": "10th Oct 2025"},
    "Pigeon Spies": {"Date Completed": "30th Sept 2025"}
}
```

Now imagine that you come up with the idea of adding individual collaborators to every collaboration item. Your json file could end up looking something like this

```json
{
    "Thought Police Chip": {"Date Completed": "10th Oct 2025", "collaborators"=["Mark Zuckerberg", "Bill Gates"]},
    "Pigeon Spies": {"Date Completed": "30th Sept 2025", "collaborators"=["Mark Zuckerberg", "Boris Johnson"]}
}
```



### Personal Experience

### References

() https://olibr.com/blog/json-vs-sql-whats-the-difference/#SQL_vs_JSON_Key_Difference
