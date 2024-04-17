import os

name = os.getenv('NAME', 'World')

print(f'Hello, {name}!')

# docker run -e NAME=JohnDoe my-python-app 
# docker run --env-file env.list my-python-app 

