from dotenv import load_dotenv
import os
from sergey_secret_key import SERGEY_SK

load_dotenv()

# loading every .env file in the project
api_key=os.environ.get('API_KEY1')
sk=os.getenv('SECRET_KEY')
jk=os.getenv('JOHN_KEY')
print(api_key)
print(sk)
print(jk)

print(jk.split())

