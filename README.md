# atlasls-mental-health
RESTful API and webapp for Atlas Life Systems  

## Running Locally
1. Clone the repo!  
   <code>git clone git@github.com:stairs1/atlasls-mental-health.git</code>
2. Create a python virtual environment with python>=3.6. (Depends on what you use, I use my own aliases) 
3. Install the python dependencies  
   <code>cd atlasls-mental-health/atlas</code>  
   <code>pip install -r py_dependencies</code>  
4. Install postgres (This depends on your OS).  
   For Ubuntu: <code>sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib</code>
5. Create database named atlasdb, and user named atlasdbadmin with password atlas.  
   Switch to postgres user (OS dependent, this is for Ubuntu): <code>sudo su - postgres</code>  
   <code>psql</code>  
   <code>CREATE DATABASE atlasdb;</code>  
   <code>CREATE USER atlasdbadmin WITH PASSWORD 'atlas';</code>  
   <code>ALTER ROLE atlasdbadmin SET client_encoding TO 'utf8';</code>  
   <code>ALTER ROLE atlasdbadmin SET default_transaction_isolation TO 'read committed';</code>  
   <code>ALTER ROLE atlasdbadmin SET timezone TO 'UTC';</code>  
   <code>GRANT ALL PRIVILEGES ON DATABASE atlasdb TO atlasdbadmin;</code>  
   <code>\q</code>  
   Make sure you switch back to your normal user!
6. Install nvm from its repo: https://github.com/nvm-sh/nvm
7. Install node
   <code>nvm install 12.16.1</code>
8. Install webpack, babel, and frontend libraries  
   <code>cd frontend</code>  
   <code>npm i webpack webpack-cli --save-dev</code>  
   <code>npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev</code>  
   <code>npm i react react-dom react-router-dom --save-dev</code>  
9. Transpile frontend  
   <code>npm run dev</code>  
10. Run server!  
   <code>cd atlasls-mental-health/atlas</code>  
   <code>./manage.py runserver</code>  
   
Bonus: create superuser for Django admin  
   <code>python manage.py createsuperuser</code>


## API
| to... | http | head | body | url |
|----|------|------|------|-----|
| Register a user | POST | Content-Type: application/json | {"username": "{username}", "password": "{password}"} | api/register |
| Get a token for a user | POST | Content-Type: application/json | {"username": "{username}", "password": "{password}"} | api/token |
| Submit a survey | POST | Content-Type: application/json *and* Authorization: Token {token} | [{"question_ordinal":{ordinal},"answer":{answer}, "timestamp":"{ISO 8601}"}] | api/submit |
| Get question data (admin) | GET | Authorization: Token {token} | | api/answers |
| Get journal stubs | GET | Authorization: Token {token} | | api/journals | 
