from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model (ensure that 'model.pkl' exists in the container)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Expecting JSON payload: {"features": [feature1, feature2, ...]}
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    # Run on all available IP addresses and port 8080 (commonly used in cloud deployments)
    app.run(host='0.0.0.0', port=8080)
