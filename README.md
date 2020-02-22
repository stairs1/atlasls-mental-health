# atlas-admin
RESTful API for ATLAS data management and admin tools.  
Registers mobile clients, collects anonymous survey data, and exposes survey information to priveliged users.  

## Usage
| to... | http | head | body | url |
|----|------|------|------|-----|
| Register a user | POST | Content-Type: application/json | {"username": "{username}", "password": "{password}"} | {api/register |
| Get a token for a user | POST | Content-Type: application/json | {"username": "{username}", "password": "{password}"} | api/token |
| Submit a survey | POST | Content-Type: application/json *and* Authorization: Token {token} | [{"question_ordinal":{ordinal},"answer":{answer}, "timestamp":"{ISO 8601}"}] | api/submit |
| Get question data (admin) | GET | Content-Type: application/json | Authorization: Token {token} | api/answers |
