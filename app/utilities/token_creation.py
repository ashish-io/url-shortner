from fastapi.security import OAuth2PasswordBearer
from ..core.config import settings
from ..core.database import get_session
from ..models.user import User
from ..core.config import settings
import jwt
from fastapi import HTTPException, Depends
from sqlmodel import Session, select
from datetime import datetime, timedelta

ALGORITHM = "HS256"
TOKEN_EXPIRY_TIME = 30

token_extractor = OAuth2PasswordBearer(tokenUrl="/login")

def create_token(username: str):

  payload = {
    "sub": username,
     "exp": datetime.utcnow() + timedelta(minutes = TOKEN_EXPIRY_TIME)
  }

  token = jwt.encode(payload, settings.secret_key, ALGORITHM)

  return token

def verify_token(token: str = Depends(token_extractor), session: Session = Depends(get_session)):
  try:
    payload = jwt.decode(token, settings.secret_key, ALGORITHM)
    username = payload.get("sub")

    if username is None:
      raise HTTPException(status_code=401, detail="Invalid Token")
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")
  except jwt.InvalidTokenError:
    raise HTTPException(status_code=401, detail="Invalid Token")
  
  
  user = session.exec(select(User).where(User.username == username)).first()
  if not user:
    raise HTTPException(status_code=401, detail="User not found")

  return user