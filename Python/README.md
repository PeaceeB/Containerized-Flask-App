Local Environment

Dockerfile

```Dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster
RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5014
EXPOSE 80
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
```


Docker-Compose

```yml
version: '3.4'

services:
  db:
    image: mysql:latest
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    ports:
    - 3306:3306
    environment:
      MYSQL_DATABASE: 'blogdatabase'
      MYSQL_USER: 'root'
      MYSQL_ROOT_PASSWORD: 'root'
    volumes:
      - sqlData:/var/lib/mysql
      - "./website/data:/docker-entrypoint-initdb.d/"
    

  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5014:5000"
    volumes:
    - ./:/app/  

volumes:
  sqlData:
```