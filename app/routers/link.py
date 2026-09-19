from ..models.user import User
from ..models.link import LinkCreate, Link
from ..core.database import get_session
from ..services.link_service import create_unique_short_link
from ..services.redis_cofig import r
from ..services.rate_limiter_serivice import rate_limiter
from ..utilities.token_creation import verify_token

from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session, select
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select


router = APIRouter()

@router.post("/link/shortern", response_model=Link)
def create_and_store_short_code(url: LinkCreate, session: Session = Depends(get_session), current_user: User = Depends(verify_token)):
  link = create_unique_short_link(session,url.long_url, current_user)
  return link

@router.get("/link/{short_code}")
def redirect_to_long_url(short_code: str, session: Session = Depends(get_session),access : None = Depends(rate_limiter(limit=10, window_seconds=60))):

  cache_key = f"url:{short_code}"

  cache_value = r.get(cache_key)


  if cache_value is not None:
    print("HITTING THE CACHE")
    return RedirectResponse(url=cache_value, status_code=302)
  
  else:
    print("HITTING THE DATABASE")
    statement = select(Link).where(Link.short_code == short_code)
    result = session.exec(statement).first()

    if result is None:
      raise HTTPException(status_code=404, detail="Link not found")
    else:
      r.set(cache_key,result.long_url, ex=3600)
      return RedirectResponse(url=result.long_url, status_code=302)
    






 
 

 
