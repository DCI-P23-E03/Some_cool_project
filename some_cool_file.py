from dotenv import load_dotenv
import os
from sergey_secret_key import SERGEY_SK,hello

load_dotenv()

# loading every .env file in the project
api_key=os.environ.get('API_KEY1')
sk=os.getenv('SECRET_KEY')
jk=os.getenv('JOHN_KEY')
ssk=SERGEY_SK
print(api_key)
print(sk)
print(jk)
print(ssk)



