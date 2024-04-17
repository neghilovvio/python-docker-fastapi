# VIRTUAL ENV

python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt


# DOCKERFILE

docker build -t my-python-app .
docker run my-python-app
docker run --env-file env.list my-python-app


