import streamlit as st
import model  
import joblib

# Load and preprocess data
data_file = "E:\Project delivery time\deliverytime.txt" 
try:
    xtrain, xtest, ytrain, ytest = model.load_and_preprocess_data(data_file)
except Exception as e:
    st.error(f"Error loading data: {e}")

# Load the trained model from the existing pkl file
try:
    trained_model = joblib.load('model.pkl')  
except Exception as e:
    st.error(f"Error loading model: {e}")

# Create a two-column layout with different widths
col1, col2 = st.columns([3, 2]) 

# Image display in the first column
with col1:
    try:
        st.image("rmg.png", width=400, channels="RGB")  
    except Exception as e:
        st.error(f"Error loading image: {e}")

# Streamlit UI in the second column
with col2:
    st.title("SwiftServe")
    st.write("Enter details to predict delivery time.")

    # Input fields for user data
    age = st.number_input("Age of Delivery Partner", min_value=18, max_value=100, step=1, value=30)
    ratings = st.number_input("Ratings of Previous Deliveries", min_value=0.0, max_value=5.0, step=0.1, value=4.5)
    distance = st.number_input("Total Distance (km)", min_value=0.0, max_value=100.0, step=0.1, value=5.0)

    # Dropdown for vehicle type
    vehicle_type = st.selectbox("Type of Vehicle", ['motorcycle', 'scooter', 'electric_scooter', 'bicycle'])

    # Predict button
    if st.button("Predict Delivery Time"):
        try:
            predicted_time, adjusted_time = model.predict_delivery_time(trained_model, age, ratings, distance, vehicle_type)
            
            # Display predictions
            st.write(f"Predicted Delivery Time (Model Prediction): {predicted_time:.2f} minutes")
            if adjusted_time:
                st.write(f"Adjusted Delivery Time based on Vehicle Speed: {adjusted_time:.2f} minutes")
            else:
                st.write("Invalid vehicle type provided.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
