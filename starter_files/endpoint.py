import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://921786b2-b01f-41e5-8b36-6383b90f8238.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '2gpLKNmbiYbE1fKzokDHEM2rZBfSOrf7'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 17,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact_cellular": 1,
            "day_of_week": 1,
            "default": 0,
            "duration": 971,
            "education_university.degree": 1,
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": 1,
            "job_blue-collar": 1,
            "loan": 1,
            "marital": 1,
            "month": 5,
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": 0,
            "previous": 1
          },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact_cellular": 1,
            "day_of_week": 1,
            "default": 0,
            "duration": 471,
            "education_university.degree": 1,
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": 1,
            "job_blue-collar": 1,
            "loan": 1,
            "marital": 1,
            "month": 5,
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": 0,
            "previous": 1
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


