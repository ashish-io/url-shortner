import string, secrets

def short_code_generator(length = 6):
  chars = string.ascii_letters + string.digits

  return ''.join(secrets.choice(chars) for _ in range(length))

  