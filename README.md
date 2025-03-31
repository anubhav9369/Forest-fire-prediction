# 🔥 Forest Fire Prediction System
A Machine Learning-based web application to predict forest fire severity using real-time weather conditions.

## 📖 Project Overview
The **Forest Fire Prediction System** uses **K-Means Clustering** to classify fire risk into **Low, Medium, and High severity levels** based on environmental factors like temperature, wind speed, and humidity. 

✅ **Real-time prediction** based on user inputs  
✅ **Web-based frontend** for easy access    

## ✨ Features
✔ **Predict Fire Risk** based on environmental factors  
✔ **Professional UI** with React.js    
✔ **Flask-based API** for backend processing  

## 🛠️ Tech Stack
**Frontend:** React.js, HTML, CSS  
**Backend:** Flask, Python  
**Machine Learning:** Scikit-Learn (K-Means Clustering)  

## ⚙️ Installation Guide
Follow these steps to set up the project locally.

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/yourusername/forest_fire_prediction.git
cd forest_fire_prediction

## Backend
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt  # Install dependencies
python app.py  # Start Flask server

## Frontend
cd ../frontend
npm install  # Install dependencies
npm start  # Start React frontend

