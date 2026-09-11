from fastapi import APIRouter,Depends,HTTPException
from ..models.link import LinkCreate, Link
from ..core.database import get_session
from sqlmodel import Session, select
from ..services.link_service import create_unique_short_link
from fastapi.responses import RedirectResponse
from ..services.redis_cofig import r


router = APIRouter()

@router.post("/shortern", response_model=Link)
def create_and_store_short_code(url: LinkCreate, session: Session = Depends(get_session)):
  link = create_unique_short_link(session,url.long_url)
  return link

@router.get("/{short_code}")
def redirect_to_long_url(short_code: str, session: Session = Depends(get_session)):

  cache_key = short_code

  cache_value = r.get(cache_key)


  if cache_key:
    return RedirectResponse(url=cache_value, status_code=302)
  else:

    statement = select(Link).where(Link.short_code == short_code)
    result = session.exec(statement).first()

    if result is None:
      raise HTTPException(status_code=404, detail="Link not found")
    else:
      r.set(cache_key,result.long_url, ex=3600)
      return RedirectResponse(url=result.long_url, status_code=302)
    






 
 

 
