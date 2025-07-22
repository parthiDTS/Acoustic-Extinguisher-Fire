from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load("KNN_model.pkl")

# Fuel encoding dictionary
fuel_encoding = {
    'Gasoline': 0,
    'Thinner': 1,
    'Kerosene': 2,
    'LPG': 3
}

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        SIZE = float(request.form['size'])
        FUEL = request.form['fuel']
        DISTANCE = float(request.form['distance'])
        DESIBEL = float(request.form['desibel'])
        AIRFLOW = float(request.form['airflow'])
        FREQUENCY = float(request.form['frequency'])

        FUEL_ENCODED = fuel_encoding.get(FUEL, -1)
        if FUEL_ENCODED == -1:
            return render_template('index.html', prediction="❌ Invalid fuel type.")

        input_data = np.array([[SIZE, FUEL_ENCODED, DISTANCE, DESIBEL, AIRFLOW, FREQUENCY]])
        prediction = model.predict(input_data)[0]

        result = "🔥 Fire extinguished!" if prediction == 1 else "❌ Fire NOT extinguished!"
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
