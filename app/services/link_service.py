from ..utilities.short_code_generation import short_code_generator
from ..models.link import Link
from sqlalchemy.exc import IntegrityError

def create_unique_short_link(session, long_url, current_user):
  while True:

    short_code = short_code_generator()
    user_id = current_user.id
    
    link = Link(long_url=long_url, short_code=short_code, created_by=user_id)
    session.add(link)

    try:
      session.commit()
      session.refresh(link)
      return link
    except IntegrityError:
      session.rollback()



    


