from ..models.user import User, UserView
from ..core.database import get_session
from ..utilities.token_creation import verify_token
from fastapi import APIRouter,Depends, HTTPException
from sqlmodel import select, Session

router = APIRouter()

@router.get("/user/{user_id}",response_model =  UserView)
def get_one_user(user_id: int, session:Session = Depends(get_session), current_user: User = Depends(verify_token)):

  user = session.get(User, user_id)

  if not user:
    raise HTTPException(status_code = 404, detail = "User do not exists")
  
  return user

@router.get("/test")
def test():
    return {"message": "Hello from FastAPI"}