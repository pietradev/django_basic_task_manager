# Django Task Manager

## Purpose of this project
This project focuses on practicing Django basic concepts such as understanding the relationships between the urls.py, views.py, models.py, and settings.py files. 

### Understanding Models.py
This file defines the classes that will be translated into tables using the makemigrations command. 
- All classes defined receive models.Model as a parameter as Django will understand that this class is a model to be translated into a table. 
- Due to extending the Model class, all classes defined here will also inherit important methods, such as save(), delete(), and objects() - they are pivotal when we instantiate classes that are defined here.
- We can also use a special method called __str__ in which we can display any attribute from the class

### Urls.py
There are two general URL files: the first is in our project folder, and the second is in our app folder. We need to include the second file in the project's main URLs folder. In this file, we specify which function from the view will be called when a user visits a specific URL.

### Settings.py
In this file, we have the general configuration. We need to keep in mind the following:
1. Include the name of the app folder in the `INSTALLED_APPS` variable.
2. Add the directory path for the `TEMPLATES` folder to the dictionary under `TEMPLATES -> 'DIRS'` using `os.path.join(BASE_DIR, 'templates')`. 

Remember to import the `os` module!

### Understanding the CRUD
3 templates were created
**1. Main Template (/) - task_list.html:**
- If there are no tasks added, users will see the message "No task has been found! :(" on the main page.
![image](https://github.com/user-attachments/assets/801ff2a9-bb4f-4ee2-9a84-3fa390e90724)

**2. Creating a new task (/task/new/) - task_form.html:**
- When users click on Create a New Task, they will be directed to a formulary where they are prompted to add the title, description and if the task was completed (It is not completed by default)
 ![image](https://github.com/user-attachments/assets/01963d22-7cfe-427b-84cb-6912b8812d53)

- When a task is added, users are redirected to the main page and see the list of tasks
![image](https://github.com/user-attachments/assets/c7b4b72c-03b4-49dc-b8b1-4b44b311555c)

**When we have a list of tasks, users can either Edit (are directed to task_form.html) or Remove (are directed to task_confirm_delete.html)**
- Editing the task

![image](https://github.com/user-attachments/assets/78c39d17-2a18-4b11-a395-8cce81a9683c)

- Removing the task
  
![image](https://github.com/user-attachments/assets/b63914d0-a4e2-4fe0-a95b-05c6df47b43e)


**3. Removing a Task (/task/delete/task_id/) - task_confirm_delete.html:**
When users click on Remove a task, they are directed to the third template - task_confirm_delete.html. By clicking on the button to confirm the deletion, they are directed to the main page (/).
![image](https://github.com/user-attachments/assets/ee3a125e-06a0-472b-9557-4de96e368414)
