import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    R = 6371  # Earth's radius in kilometers
    
    def deg_to_rad(degrees):
        return degrees * (np.pi/180)
    
    def distcalculate(lat1, lon1, lat2, lon2):
        d_lat = deg_to_rad(lat2-lat1)
        d_lon = deg_to_rad(lon2-lon1)
        a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        return R * c
    
    # Calculate distance
    data['distance'] = data.apply(lambda row: distcalculate(
        row['Restaurant_latitude'],
        row['Restaurant_longitude'],
        row['Delivery_location_latitude'],
        row['Delivery_location_longitude']
    ), axis=1)
    
    # Split data
    x = data[["Delivery_person_Age", "Delivery_person_Ratings", "distance"]]
    y = data[["Time_taken(min)"]]
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)
    
    return xtrain, xtest, ytrain, ytest

def build_and_train_model(xtrain, ytrain):
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(xtrain.shape[1], 1)),
        LSTM(64, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(np.expand_dims(xtrain, axis=-1), ytrain, batch_size=1, epochs=9)
    return model

# Prediction function
def predict_delivery_time(model, age, ratings, distance, vehicle_type):
    speed_map = {
        'motorcycle': 85,
        'scooter': 57.5,
        'electric_scooter': 47.5,
        'bicycle': 17.5
    }
    average_speed = speed_map.get(vehicle_type, 0)

    features = np.array([[age, ratings, distance]])
    predicted_time = model.predict(features)[0][0]
    
    # Adjust predicted time based on vehicle speed and Convert hours to minutes
    if average_speed > 0:
        adjusted_time = (distance / average_speed) * 60 
    else:
        adjusted_time = None 
    
    return predicted_time, adjusted_time
