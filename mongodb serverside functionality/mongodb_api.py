""" 
this is my generated token  
uoOAdhzMsm9fEzXmmsZD7d1V8ZuILT1CALepa2AtqTkSEalqsD1UWcKwoOL1XO7R

api link 
https://ap-south-1.aws.data.mongodb-api.com/app/data-zsjxl/endpoint/data/v1

"""


import requests
import json
url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-zsjxl/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "copy_ishu_example",
    "database": "copy_ishu_example",
    "dataSource": "CopyProductDetail",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'uoOAdhzMsm9fEzXmmsZD7d1V8ZuILT1CALepa2AtqTkSEalqsD1UWcKwoOL1XO7R',
  'Accept': 'application/ejson'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
