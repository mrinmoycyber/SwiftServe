# SwiftServe

## Project Goal
The goal of this project is to accurately predict food delivery times based on key factors such as the delivery partner's age, prior performance ratings, travel distance, and vehicle type. By leveraging a Long Short-Term Memory (LSTM) neural network model, this project aims to model realistic delivery scenarios by analyzing real-time and historical data. Incorporating the type of vehicle used for delivery, along with dynamic route distance calculations, allows for a nuanced prediction that reflects varying speeds and traffic conditions. Ultimately, this project seeks to optimize delivery time estimations, offering actionable insights for improving delivery efficiency and customer satisfaction in the food delivery domain.

## Features
- **Delivery Partner Information**: Customers can enter details about the delivery partner, such as age and previous ratings, to receive tailored delivery time predictions.

- **Distance Input**: Users input the total distance for the delivery, helping them understand the delivery context better.

- **Vehicle Type Selection**: Customers can select the type of vehicle (motorcycle, scooter, electric scooter, bicycle) used for delivery, allowing for more accurate time predictions based on vehicle speed.

- **Predicted Delivery Time**: The application provides customers with a predicted delivery time based on the entered information and selected vehicle type, enhancing transparency.

- **Adjusted Delivery Time**: Displays an adjusted delivery time based on the average speed of the selected vehicle, giving customers a realistic expectation of delivery duration.

- **User-Friendly Interface**: An interactive and easy-to-navigate web interface that allows customers to input their details effortlessly and receive quick responses.

- **Visual Feedback**: Clear output messages displaying predicted delivery times help customers understand the estimation process easily.

- **Error Notifications**: Informative messages alert users to any issues with their input, ensuring they can correct mistakes and resubmit their information.

## Project Structure
```plaintext
├── .gitignore
├── README.md
├── app.py
├── deliverytime.txt
├── model.pkl
├── model.py
└── rmg.png
```

## Video Output
Watch the project demo here: 

https://github.com/user-attachments/assets/51b5bfdf-e95b-446b-86fb-b5b7b54d38af

## Requirements
To run this project, ensure you have the following dependencies installed:

- `pandas`
- `numpy`
- `tensorflow`
- `scikit-learn`
- `streamlit`
- `joblib`
- `plotly`

You can install the required packages using pip:

```bash
pip install pandas numpy tensorflow scikit-learn joblib streamlit plotly
```

## Usage 
Clone the repository:
```bash
git clone https://github.com/yourusername/SwiftServe.git
```
Navigate to the project directory:
```bash
cd SwiftServe
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Prepare the dataset: 
```bash
data_file = "deliverytime.txt"
```
Run the Streamlit app:
```bash
streamlit run app.py
```
