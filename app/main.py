from fastapi import Depends, FastAPI, HTTPException,Body, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import crud, models, schemas, hashing
from .database import SessionLocal, engine
from app.schemas import UserSchema, UserLoginSchema
from .auth_handler import signJWT
from app.auth_bearer import JWTBearer


# Security for API
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
models.Base.metadata.create_all(bind=engine)



# Dependency for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        
# description to be used in tags metadata       
description = """
User registration API helps you register users in database in a secure way . 🚀

## Users
You will be able to:
* **Create users**
* **Get users from DB** 
* **Update users' credentials** 
* **Delete users** 
"""   

tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users. The **SignUp** logic is also here.",
        "externalDocs": {
            "description": "Users external docs",
            "url": "https://fastapi.tiangolo.com/",
        }
    }
]

 
app = FastAPI( title="User Registration App",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)



    
        
#This is to get details of all the users available in database excluding password field.
@app.get("/users",
        tags=["User"],
        response_model = list[schemas.UserSchema],
        response_model_exclude={"password"},
        dependencies=[Depends(JWTBearer())],
        responses={}
        ) 
def get_users(db: Session = Depends(get_db),
    skip: int | None = Query(default=0, title="Query integer",description="Id of first record"),
    limit: int | None = Query(default=10, title="Query integer",description="Id of last record") 
    ): 
    """
    This endpoint will let you have exposure to all the users signed up in database .     
    """
    users =  crud.get_users(db)
    return users



#This request is used for creating a new user in database
@app.post("/user/signup", tags=["User"])
def create_user(db: Session = Depends(get_db),user: UserSchema = Body(...)):
    """
    This endpoint lets you create a new user in database. As you provide `name` , `email` , `date of birth` and
    `password` fields as `BODY()` param. This POST request will insert a new user row in databse schema. 
     
    """
    crud.create_user(db,user=user)
    return signJWT(user.email)

@app.post("/user/login", tags=["User"]) 
def read_user(user: UserLoginSchema = Body(...),db: Session=Depends(get_db)):
    """
    This endpoint will let you generate new refreshed jwt tokens for already registered users.
    incase if your token gets expired just use this request and get a new one.
     
    """
    users = crud.get_users(db)
    for ppl in users:   #ppl stands for people
        if ppl.email == user.email and hashing.verify_password(user.password, ppl.password) :
            return signJWT(ppl.email)
    return { "error": "Wrong login details!"} 



#this endpoint performs update actions for users.
@app.patch("/users/{user_id}", tags=["User"],dependencies=[Depends(JWTBearer())]) #
def update_user(user_id: str,db: Session = Depends(get_db),user: UserSchema = Body(...)):
    """
    This endpoint will let you update data of users available in db. Note that email field can't be updated 
    yet you have to provide it's value to authenticate yourself. and rest attributes will get  update in db.
     
    """
    return crud.update_user(db,user_id=user_id , user=user)



#Delete any user by using his ID
@app.delete("/users/{user_id}/del", tags=["User"])
def del_user(user_id:str, db: Session = Depends(get_db)):
    """
    delete any user by passing his ID number as integer.
     
    """
    return crud.del_user(db,user_id=user_id)



