# Gogolook

# SQL database & ORM 
* sqlite3
* flask_sqlalchemy

# Spec
## request
    see spec.md
## response
```
ResponseStatusCode int
Message string
Data dict

ex:
    {
        "ResponseStatusCode": 200,
        "Message": "Success",
        "Data": {
            "result": []
        }
    } 
```

## Reference
* https://www.maxlist.xyz/2019/11/10/flask-sqlalchemy-setting/
* https://www.maxlist.xyz/2019/10/30/flask-sqlalchemy/
* https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/