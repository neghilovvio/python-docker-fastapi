# DOCKER BUILD
docker build -t fastapi-app .  

# DOCKERFILE
docker run -p 80:80 fastapi-app
docker run -p 80:80 -v $(pwd):/code fastapi-app

# DOCKER COMPOSE
docker compose up --build
docker compose up