from sqlmodel import SQLModel, Field

class User(SQLModel, table = True):
  id: int | None = Field(default = None,primary_key = True)
  username: str
  email: str = Field(unique = True)
  hashed_password: str

class UserCreate(SQLModel):
  username: str
  email: str
  password: str

class UserView(SQLModel):
  id: int
  username: str
  email: str

