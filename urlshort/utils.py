import random
import string
from .models import URL

def generate_short_url():
    characters = string.ascii_letters + string.digits
    
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        
        if not URL.objects.filter(short_url=short_url).exists():
            return short_url