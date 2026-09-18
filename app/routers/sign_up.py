from ..models.user import User, UserView, UserCreate
from ..core.database import get_session
from fastapi import APIRouter,Depends, HTTPException
from sqlmodel import select, Session
from ..utilities.password import hash_password, verify_password

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, session: Session = Depends(get_session)):
  new_user = User(
    username = user.username
    email = user.email
    hashed_password = hash_password(user.password)
  )

  session.add(new_user)
  session.commit()
  session.refresh(new_user)

  return {"message": "Registration Successful"}



  


  
