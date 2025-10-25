# Data Optimization and Analysis in my Personal API

#### 25th October 2025

### What?

In October 2025, I have created my first ever RESTful API that I had since built a frontend for and transformed the whole application into a website for self promotion and showcasing.

Designing the application was a big undertaking as I had to ensure that it would stay relevant for as long as possible, allowing easy and time-efficient extension in the future. The databases also had to be designed with the same goal in mind.

In addition to that the data presented needed to be easily editable, so appropriate tools needed to be made.





## So what?

Designing my templates, I utilized Jinja2's blocks, which came very handy in building my 2 main base templates; `base.html` (Available at: [Personal_RESTful_API/templates/base.html at main · Ryboster/Personal_RESTful_API · GitHub](https://github.com/Ryboster/Personal_RESTful_API/blob/main/templates/base.html)), and `list_base.html` (Available at:[Personal_RESTful_API/templates/list_base.html at main · Ryboster/Personal_RESTful_API · GitHub](https://github.com/Ryboster/Personal_RESTful_API/blob/main/templates/list_base.html) ). Consider the following example:

```html
<div id="addFormContainer" class="addFormContainer" style="display:none;" onclick="this.style.display = 'none'">
        <form onclick="event.stopPropagation()" id="addForm" class="addForm" method="POST">
            <input name="_method" readonly type="hidden" value="POST">
            {% block ADD_FORM %}
            {% endblock ADD_FORM %}
            <button type="submit"> Submit </button>
        </form>
    </div>
```

Every one of my list endpoints (of which I now have 3) has to contain the forms used in CRUD operations on my database records. Since defining each form can take anywhere from 8 to 20 lines, defining all 4 forms could take up to 80 lines per template! This is a huge waste of space at the impediment of readability and maintainability as well as a huge time sink. Granted, it's not every day you add a new list template (like "Projects" or "Collaborations"), but when you do, you want it done quickly so you can focus on more important things like making sure that your Flask routes work.

Moving this definition off to a base template instead had vastly improved the efficiency of introduction of any potential extension.



Another problem I came across was providing each 





## Now what?

'Now what?' allows you to create an action plan for the future based on the previous questions.


