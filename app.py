from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


# Load the model from the pickle file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    data = request.json['data']

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
        
    
    
    prediction = model.predict(data)
    return jsonify({'prediction': prediction.tolist()})
    # return jsonify({'prediction': "Sumit Gupta"})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'

