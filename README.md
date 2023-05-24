# python-htmx-poc
First try of HTMX with a Python app

A simple search bar that searchs a hardcoded list of todo items based on [this](https://testdriven.io/blog/flask-htmx-tailwind/) tutorial but without using Tailwind.

## Search bar function:
    - uses HTMX to send a POST request with the search term entered. 
    - Search Term is compared to todo.id, todo.title and todo.completed
    - any matches being appended to the returned array that targets #todo-results `tbody` in index.html template. 
    - Each element in the array is then transformed into an HTML `tr` in the todo.html template.
    - All the rows are rendered as `tr `within `table tbody` index.htm template.
    - A dynamic front end without any JS!
## Styling:
    - CSS to style the table and search bar in a similar fashion to the tutorial example but without using tailwind.
    
## Installing:
   ### Make a local clone of the repo
    - $ git clone 
   ### Install Python if required
    - $ npm i python3
   ### Install and run virtual environment
    - $ npm i virtualenv
    - $ python3 -m venv venv
    - $ source <path to venv>/Scripts/activate    # if using windows
        OR
    - $ source <path to venv>/bin/activate    # if using POSIX
   ### Instal Flask if not already installed:
    - (venv)$ pip install Flask==2.1.1 Flask-Assets==2.0
   ### Run the app and view in localHost:5000
    - $ python app.py
