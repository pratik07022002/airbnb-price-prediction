# 🏠 Airbnb Price Optimisation Tool – NYC

A machine learning-based web application that predicts a suitable Airbnb listing price in New York City based on property location, minimum nights, reviews, host listings, availability, neighbourhood group, and room type.

The project provides an interactive **Streamlit interface** where users can enter property details and receive a predicted/suggested Airbnb price.

---

## 📌 Project Overview

The **Airbnb Price Optimisation Tool** uses a trained machine learning regression model to estimate the price of an Airbnb listing in New York City.

Users can provide information such as:

* Latitude and longitude
* Minimum number of nights
* Number of reviews
* Reviews per month
* Host listing count
* Availability throughout the year
* Neighbourhood group
* Room type

The application processes these inputs, encodes the categorical variables, and passes the resulting feature set to the trained machine learning model to generate a suggested price.

The project demonstrates how machine learning can be integrated into a simple web application to support **data-driven Airbnb pricing decisions**.

---

## ✨ Features

* 🏠 **Airbnb Price Prediction** – Predicts a suggested listing price based on property characteristics.
* 📍 **Location-Based Prediction** – Uses latitude, longitude, and neighbourhood group.
* 🛏️ **Room Type Selection** – Supports:

  * Entire home/apt
  * Private room
  * Shared room
* 📊 **Property & Host Information** – Considers minimum nights, reviews, host listings, and availability.
* 🤖 **Machine Learning Model** – Uses a pre-trained regression model for price prediction.
* 🖥️ **Interactive Web Interface** – Built using Streamlit.
* 💰 **Instant Price Recommendation** – Displays the predicted price in USD after clicking the prediction button.

---

## 🤖 Machine Learning Approach

The project follows a supervised machine learning approach for **regression-based price prediction**.

### Input Features

The model uses the following features:

| Feature             | Description                                |
| ------------------- | ------------------------------------------ |
| Latitude            | Geographic latitude of the Airbnb listing  |
| Longitude           | Geographic longitude of the Airbnb listing |
| Minimum Nights      | Minimum number of nights required          |
| Number of Reviews   | Total reviews received by the listing      |
| Reviews Per Month   | Average reviews received per month         |
| Host Listings Count | Number of listings managed by the host     |
| Availability        | Number of available days per year          |
| Neighbourhood Group | NYC borough/area                           |
| Room Type           | Type of Airbnb accommodation               |

### Feature Encoding

Categorical variables are converted into numerical representations before being passed to the model.

**Neighbourhood Group:**

* Brooklyn
* Manhattan
* Queens
* Bronx
* Staten Island

**Room Type:**

* Private room
* Entire home/apt
* Shared room

The encoded features are combined with the numerical features and supplied to the trained model.

### Prediction

The trained model is loaded using `joblib`:

```python
model = joblib.load("airbnb_price_model.pkl")
```

When the user clicks **Predict Price**, the application sends the input features to the model:

```python
price = model.predict(input_data)[0]
```

The predicted value is then displayed as the suggested Airbnb price.

---

## 🛠️ Technologies Used

### Programming Language

* **Python**

### Machine Learning

* **Scikit-learn**
* **Joblib**
* Regression-based machine learning model

### Data Processing

* **NumPy**

### Web Application

* **Streamlit**

### Model Deployment

* Pre-trained `.pkl` machine learning model

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/airbnb-price-optimisation.git
```

Navigate to the project directory:

```bash
cd airbnb-price-optimisation
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install streamlit numpy joblib scikit-learn
```

### 3. Make Sure the Files Are Present

The project should contain:

```text
airbnb-price-optimisation/
│
├── app.py
├── airbnb_price_model.pkl
└── README.md
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

### 5. Enter Property Details

Provide the required Airbnb information and click:

**Predict Price**

The application will display the suggested price.


## 🔮 Future Improvements

The project can be further improved by:

* 📈 Adding data visualisation and exploratory data analysis.
* 🎯 Improving prediction accuracy through hyperparameter tuning.
* 🤖 Comparing multiple regression algorithms.
* 🧹 Adding a complete automated data preprocessing pipeline.
* 📍 Integrating interactive NYC maps for location-based analysis.
* 💵 Providing recommended minimum and maximum price ranges instead of a single price.
* 📊 Showing the factors that have the greatest influence on the predicted price.
* 🗃️ Connecting the application to a live Airbnb dataset.
* 🌐 Deploying the application using Streamlit Cloud or another cloud platform.
* 🔄 Adding automatic model retraining when new Airbnb data becomes available.
* 📱 Improving the UI for mobile and responsive usage.

---

## 📂 Project Structure

```text
airbnb-price-optimisation/
│
├── app.py                    # Streamlit web application
├── airbnb_price_model.pkl    # Trained ML model
├── README.md                 # Project documentation
│
└── screenshots/              # Application screenshots
    ├── home.png
    └── prediction.png
```

---

## 🎯 Project Objective

The primary objective of this project is to demonstrate the application of **machine learning and predictive analytics to Airbnb pricing**.

By considering property characteristics, location, room type, reviews, and availability, the system provides a data-driven suggested price that can assist Airbnb hosts in making better pricing decisions.

---

