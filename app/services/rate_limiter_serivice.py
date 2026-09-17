from fastapi import Request, HTTPException
from ..services.redis_cofig import r


def is_allowed(client_id: str, limit: int, window_seconds: int) -> bool:
  key = f"ratelimit:{client_id}"
 
  current_count = r.incr(key)  
 
  if current_count == 1:
      r.expire(key, window_seconds) 
 
  if current_count > limit:
      return False  
  return True


def rate_limiter(limit: int, window_seconds: int):
    def dependency(request: Request):
        client_ip = request.client.host
        access = is_allowed(client_ip, limit, window_seconds)
        if not access:
            raise HTTPException(status_code=429, detail="Too many requests")
    return dependency


  