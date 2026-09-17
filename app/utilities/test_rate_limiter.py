from ..services.redis_cofig import r

def is_allowed(client_id: str, limit: int, window_seconds: int) -> bool:
  key = f"ratelimit:{client_id}"

  # Step 1: increment the counter, get the new count back
  current_count = r.incr(key)  # which Redis command, on which key?

  # Step 2: if this is the first request in a fresh window, start the TTL
  if current_count == 1:
      r.expire(key, window_seconds)  # which command attaches a TTL to an existing key?

  # Step 3: check against the limit, regardless of step 2
  if current_count > limit:
      return False  # allowed or not?
  
  return True

for i in range(7):
    result = is_allowed("test_client", limit=5, window_seconds=10)
    print(f"Request {i+1}: {result}")