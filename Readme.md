Welcome to library management API:

Let's talk about several MarkUps about this API: 
Requests that can be performed in this API are:

For Users Management:
1. Get Request to get details of all users: This endpoint will let you have exposure to all the users signed up users in database . just provide skip and limit values as query parameters to filter out number of records that you want to see. and API GET request will handle the rest for you. but make sure you authenticate yourself first in API otherwise you won't be authorized to use it
2. Post Request for Creation of User: This endpoint lets you create a new user in database. As you provide name , email , date of birth and password fields as BODY() param. This POST request will insert a new user row in databse schema.
3. Post Request for logging in of User: This endpoint is to get refreshed tokens for registered users.
4. Patch Request for updating users' details: This endpoint will let you update data of users available in db. Note that email field can't be updated yet you have to provide it's value to authenticate yourself. and rest attributes will get update in db.
5. DELETE Request for deletion of User: delete any user by passing his/her ID.


Tech-Stack that has been used in it contains:
Database: Sqlite3 database has been used in creation of this project. It's a relational database which stores 
data in tabular format. It's suitable for small scale projects or projects that are in still development.
Framework:  FastAPI is used in creation of this project.
Security: JWT token based Authentication provides this API a very secured interface. Token gets expired after a while
hence user has to get new one. This makes chances of data leaking very less.





API documentation link for this project: https://documenter.getpostman.com/view/24975779/2s8YzZPJiz#intro

Schema diagram : https://drive.google.com/file/d/1QJWcwW0u_tpqC9zFpPo85kdgKHR50eVx/view?usp=sharing

