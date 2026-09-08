from sqlmodel import SQLModel, Field
from datetime import datetime

class Link(SQLModel, table = True):
  id: int | None = Field(default = None, primary_key = True)
  long_url : str
  short_code: str = Field(unique = True, index = True)
  created_at: datetime = Field(default_factory=datetime.utcnow)

class LinkCreate(SQLModel):
  long_url: str
  






