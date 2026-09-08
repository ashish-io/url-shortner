from ..utilities.short_code_generation import short_code_generator
from ..models.link import Link
from sqlalchemy.exc import IntegrityError

def create_unique_short_link(session, long_url):
  while True:
    short_code = short_code_generator()

    link = Link(long_url=long_url, short_code=short_code)
    session.add(link)


    try:
      session.commit()
      session.refresh(link)
      return link
    except IntegrityError:
      session.rollback()

    


