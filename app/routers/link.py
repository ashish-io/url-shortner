from fastapi import APIRouter,Depends,HTTPException
from ..models.link import LinkCreate, Link
from ..core.database import get_session
from sqlmodel import Session, select
from ..services.link_service import create_unique_short_link
from fastapi.responses import RedirectResponse




router = APIRouter()

@router.post("/shortern", response_model=Link)


def create_and_store_short_code(url: LinkCreate, session: Session = Depends(get_session)):

  link = create_unique_short_link(session,url.long_url)
  return link

@router.get("/{short_code}")
def redirect_to_long_url(short_code: str, session: Session = Depends(get_session)):
  statement = select(Link).where(Link.short_code == short_code)
  result = session.exec(statement).first()

  if result is None:
    raise HTTPException(status_code=404, detail="Link not found")
  else:
    return RedirectResponse(url=result.long_url, status_code=302)
  






 
 

 
