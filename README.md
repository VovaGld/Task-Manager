# Task Manager
___

## About Project
___
**Task Manager** is a web application for task management, developed using Django with Bootstrap for the frontend. 
It allows teams to efficiently organize work, create projects, manage tasks, and track their status.


##  Features
- **CRUD operations for Tasks, Teams, Projects**
- **Change task status**
- **Assign tasks to a user**
- **Filtering tasks by completed/uncompleted**
- **Ordering tasks by priority and/or deadline**


## [Deployed project](https://task-manager-wt16.onrender.com)
___
login:
```
user
```
password:
```
user12345
```

##  Installation and Setup
___
###  Clone the repository
```
   git clone https://github.com/VovaGld/Task-Manager.git
   cd Task-Manager
```

### Create a virtual environment and install dependencies
```
   python -m venv venv
   source venv/bin/activate  # for Linux and macOS
   venv\Scripts\activate  # for Windows
   pip install -r requirements.txt
```

### Apply migrations
```sh
   python manage.py migrate
```

### Create a superuser
To create a superuser use this command. 
Because the user table has been changed and needs an additional required field ``Position``. 
You can set your own data for the superuser in the ``.env`` file by adding the fields 
``ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_EMAIL``. 
By default it will be used ``username: admin, password: Password1, email: admin@gmail.com ``
```sh
   python manage.py add_admin_user
```


### Start the server
```sh
   python manage.py runserver
```

### Open in your browser
```
   http://127.0.0.1:8000/
```
You can create your own .env file based on .env.sample
```
cp .env.sample .env
```
And set your own environmental variables, such as:
- your postgresql connection data
- django secret key, path to settings module and hostname
- data for add_admin_user command

## Site description
___

- **Tasks**: a page with tasks for you 
- **Created tasks**: a page with tasks created by you
- **Teams**: a page with your teams
- **Projects**: a page with your projects
- **Only** the author of the **task/team/project** can change it
- You can create project if you have team **(you are author of team)**. 
If you don`t have a team and you try to create a project you will redirected to the team creation page
- You can add new **user/task type/position** using **admin panel**


