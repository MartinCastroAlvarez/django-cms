# Deployment Guide
This file contains the instructions to run the app. However, it only describes how to run the application on a Development environment and the deployment to Production is Out of Scope.

#### Red Hat Enterprise Linux
This section describes how to run the Application on RHEL.
##### Download the Application from GitHub
```bash
git clone ssh://git@github.com/MartinCastroAlvarez/malaga.git
cd malaga
```
##### Create a Virtual Environment
```bash
virtualenv -p python3 .env
```
##### Always active the Virtual Environment
```bash
source .env/bin/activate
```
##### Install the Application Dependencies
```
source .env/bin/activate
pip install -r requirements.txt
```

##### Setting Environment Variables
```bash
export MALAGA_SECRET_KEY="czw$_jir5h2n1dqun^5o#ayl3k8q5i31g=q8lh#0=egv_ec%7e"
export MALAGA_DEBUG="TRUE"
export MALAGA_DB_HOST="0.0.0.0"
export MALAGA_DB_PORT="5432"
export MALAGA_DB_PASS="beridyfycuuult"
export MALAGA_DB_USER="psql"
export MALAGA_DB_NAME="malaga_database"
```
##### Run a PostgreSQL Docker Container
```bash
docker rm -f "MalagaDatabase"
docker run -d \
    --name "MalagaDatabase" \
    -e POSTGRES_DB="${MALAGA_DB_NAME}" \
    -e POSTGRES_USER="${MALAGA_DB_USER}" \
    -e POSTGRES_PASSWORD="${MALAGA_DB_PASS}" \
    -p "5432:${MALAGA_DB_PORT}" \
    postgres
```
##### Verify the Docker is Running
```bash
docker ps | grep MalagaDatabase
```
##### Run migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
##### Run the Application locally
```bash
python3 manage.py runserver
```
##### Visit the [Site](http://127.0.0.1:8000/)
