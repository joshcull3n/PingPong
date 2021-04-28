from python:3.8-slim-buster
copy . /app
workdir /app
run pip install -r requirements.txt
entrypoint [ "python" ]
cmd [ "app.py" ]