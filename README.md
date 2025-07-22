# Acoustic-Extinguisher-Fire
An innovative AI-based solution that classifies and helps simulate extinguishing fire through acoustic waves. This project leverages machine learning and sound classification to identify fire-prone environments such as Gasoline, Thinner, Kerosene, and LPG and predicts whether the fire can be extinguished using specific sound frequencies.
## 🔍 Overview

**Acoustic Extinguisher Fire** is a prototype project inspired by real-world acoustic fire suppression research. The system uses a trained machine learning model to predict whether a fire caused by certain elements (like LPG, Kerosene, Thinner, or Gasoline) can be extinguished using sound-based techniques.

This system can be further developed for **IoT-based smart firefighting systems**, **drone-based firefighting**, or **automated safety alerts** in hazardous environments.

---

## ✨ Features

- 🧠 **ML-Based Prediction**: Accurately predicts fire extinguishing possibility using logistic regression.
- 🔊 **Acoustic Logic Simulation**: Mimics sound-based suppression based on classified inputs.
- 💡 **Interactive UI**: Built using Flask for seamless user input and real-time output.
- 📈 **High Accuracy**: Trained on a structured dataset with key fire-causing substances.
- 🔄 **Reusable ML Model**: Exported `.joblib` model allows quick and efficient integration.

---

## 🔧 How It Works

1. User inputs binary values (0 or 1) for substances like LPG, Kerosene, Thinner, and Gasoline.
2. The Flask backend passes this data to the pre-trained ML model.
3. The model predicts whether fire caused by these elements can be extinguished using acoustic energy.
4. Output is displayed: `"Fire was extinguished"` or `"Fire was not extinguished"`.

---

## 🧰 Tech Stack

- 🐍 Python 3
- 🔮 Scikit-learn
- 🌐 Flask (Web Framework)
- 🧪 NumPy & Pandas
- 🛠️ HTML5, CSS3 (for frontend)

---

## 🧠 Model Description

The model uses **Logistic Regression** for binary classification:

- **Inputs**: Binary values representing presence (`1`) or absence (`0`) of:
  - LPG
  - Kerosene
  - Thinner
  - Gasoline

- **Output**:
  - `1` — Fire can be extinguished acoustically
  - `0` — Fire cannot be extinguished

- **Model File**: `model.joblib`  
- **Accuracy Achieved**: ~95% (example – replace with your actual accuracy)
