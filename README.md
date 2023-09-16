### MarkDownTables
Generate MarkDown Tables in Python

### Usage
Provide a list of dicts as the titles arg:
```Python
titles =  [
    {'name': 'environment', 'title': 'Environment', 'align': 'center'},
    {'name': 'company-backend-app1', 'title': 'Company Backend App1', 'align': 'center'},
     ...
]
```
And a dict containing a list of dicts as the values arg:
```Python
values = {
    'test1': [
                {'name': 'company-backend-app1', 'value': 'main'},
                {'name': 'company-backend-app2','value': 'feature-1'},
                {'name': 'company-frontend-app1','value': 'main'},
                {'name': 'company-frontend-app2','value': 'feature-2'}
             ],
    'test2': [
                {'name': 'company-backend-app1','value': 'main'},
                {'name': 'company-backend-app2','value': 'main'},
                {'name': 'company-frontend-app1','value': 'main'},
                {'name': 'company-frontend-app2','value': 'main'}
            ],
    ...
}
```

The keys from the values dict become the environment column's value and the value field is retrieved based on the column name.
        

### Example output

| Environment | Company Backend App1 | Company Backend App2 | Company Frontend App1 | Company Frontend App2 |
| :---: | :---: | :---: | :---: | :---: |
| test1 | main | feature-1 | main | feature-2 |
| test2 | main | main | main | main |
| test3 | main | main | feature-3 | main |

### Testing
pytest -v test/unit