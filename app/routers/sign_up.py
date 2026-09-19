from ..models.user import User, UserView, UserCreate
from ..core.database import get_session
from ..utilities.token_creation import create_token
from fastapi import APIRouter,Depends, HTTPException
from sqlmodel import select, Session
from ..utilities.password import hash_password, verify_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, session: Session = Depends(get_session)):

  #check if user already exists: (will return none if not found)
  existing_user = session.exec(select(User).where(User.username == user.username)).first()

  if existing_user is not None:
    raise HTTPException(status_code=409, detail="User already registered, proceed to Login!!")

  #if user is new then:
  new_user=User(
    username = user.username,
    email = user.email,
    hashed_password = hash_password(user.password)
  )

  session.add(new_user)
  session.commit()
  session.refresh(new_user)

  return {"message": "Registration Successful"}

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
  username = form.username
  password = form.password

  user = session.exec(select(User).where(User.username == form.username)).first()

  if user is None:
    raise HTTPException(status_code=401, detail="User dont exist, Register first!!")

  if  not verify_password(password, user.hashed_password):
    raise HTTPException(status_code = 401, detail="Wrong Password")

  #generate token and return that
  token = create_token(form.username)


  return {"access_token": token, "token_type": "bearer"}

  




  

  


  
