import requests

# Assuming 'data' contains the input data you want to predict on
data = {
    'data': [[5.1, 3.5, 1.4, 0.2]]
}

url = 'http://localhost:5000/predict'
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    prediction = result['prediction']
    print(prediction)
else:
    print("Error occurred during API call.")
