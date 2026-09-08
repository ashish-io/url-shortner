from fastapi import APIRouter,Depends
from ..models.link import LinkCreate, Link
from ..core.database import get_session
from sqlmodel import Session
from ..services.link_service import create_unique_short_link


router = APIRouter()

@router.post("/shortern", response_model=Link)
def create_and_store_short_code(url: LinkCreate, session: Session = Depends(get_session)):

  link = create_unique_short_link(session,url.long_url)
  return link

@router.get("/{short_code}")
def redirect_to_long_url(short_code: str, session: Session = Depends(get_session)):




 
 

 
