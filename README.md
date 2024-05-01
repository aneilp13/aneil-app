# How to setup files locally 
Aneil Philbert
COMP 314 Advanced Application Design
Short Project 2

Git repo is https://github.com/aneilp13/aneil-app.git 

NB. Steps will reflect how i did it on my MacBook
Steps:
1. Extract the ZIP file
2. The folder called "mywebapp" can be placed on the desktop.
3. Navigate to the desktop, locate the "mywebapp" folder, right click on the folder and click open with terminal.
4. Next, start the virtual environemnt by typing: source avenv/bin/activate 
5. Next: python3 manage.py makemigrations 
6. Then: python3 manage.py migrate
7. To run the server: python3 manage.py runserver
8. After this visit (http://127.0.0.1:8000) for homepage and (http://127.0.0.1:8000/form/) for the form page.
9. To stop the server, you can do Ctrl+C.
   
To do it with docker, from step 6 use the following: 
1. docker build -t aneildocker 
2. docker run -p 8000:8000 -t aneildocker


Then visit localhost:8000 and localhost:8000/form
