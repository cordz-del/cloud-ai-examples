from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load a pre-trained model (assuming it's saved as 'model.pkl')
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
