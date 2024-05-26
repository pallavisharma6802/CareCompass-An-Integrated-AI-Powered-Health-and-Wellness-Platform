import streamlit as st
import plotly.express as px
import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt

cred_path = "/Users/sahithsharma/Desktop/care-compass/assets/care-compass-1224f-dbd593f5314a.json"
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Error initializing Firebase Admin SDK: {e}")

# Initialize Firestore client with the specific collection path
db = firestore.client()
profile_page_ref = db.collection('care-compass').document('profile_page')

# Function to calculate BMR
def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 13.397 * weight + 4.799 * height - 5.677 * age + 88.362
    else:
        bmr = 9.247 * weight + 3.098 * height - 4.330 * age + 447.593
    return bmr

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = (weight / (height / 100) ** 2)
    return bmi

# Function to interpret BMI levels
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to calculate daily calories
def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

# Function to build nutritional values
def build_nutritional_values(weight, calories):
    protein_calories = weight * 4
    res_calories = calories - protein_calories
    carb_calories = calories / 2.
    fat_calories = calories - carb_calories - protein_calories
    res = {'Protein Calories': protein_calories, 'Carbohydrates Calories': carb_calories, 'Fat Calories': fat_calories}
    return res

# Function to extract grams from nutritional values
def extract_gram(table):
    protein_grams = table['Protein Calories'] / 4.
    carbs_grams = table['Carbohydrates Calories'] / 4.
    fat_grams = table['Fat Calories'] / 9.
    res = {'Protein Grams': protein_grams, 'Carbohydrates Grams': carbs_grams, 'Fat Grams': fat_grams}
    return res

def profile_page():
    st.empty()
    st.title("Profile Information")
# User input for profile details
    st.subheader("Enter Your details")
    name = st.text_input("Name:")
    Email = st.text_input("Email:")
    age = st.number_input("Age:", min_value=1, max_value=150)
    weight = st.number_input("Weight in KGs:", min_value=1.0, max_value=500.0, step=0.1)
    height = st.number_input("Height in Cms:", min_value=1.0, max_value=300.0, step=0.1)
    sex = st.radio("Sex:", options=["male", "female"])

    activity_level = st.selectbox(
    "Select your activity level:",
    options=["sedentary", "lightly active", "moderately active", "very active"],
    )


    profile_data = {
    'Name': name,
    'Age': age,
    'Sex': sex,
    "Weight": weight,
    "Height": height,
    "Email": Email,
    "activity_level": activity_level
    }
    # Debugging line to check data

    profile_page_ref.set(profile_data)

    # Calculate BMR, BMI, and Daily Calories
    bmr = calculate_bmr(weight, height, age, sex)
    bmi = calculate_bmi(weight, height)
    bmi_category = interpret_bmi(bmi)
    calories = calculate_daily_calories(bmr, activity_level)

    # Display BMR, BMI, and Daily Calories
    st.subheader("Your Daily Calorie Needs:")
    st.write(f"Basal Metabolic Rate (BMR): {bmr:.2f} calories")
    st.write(f"Body Mass Index (BMI): {bmi:.2f} - {bmi_category}")
    st.write(f"Daily Caloric Needs: {calories:.2f} calories")

    # Build Nutritional Values and Extract Grams
    nutritional_values = build_nutritional_values(weight, calories)
    gram_info = extract_gram(nutritional_values)
  
    st.subheader("Nutritional Information:")
    st.write(f"Protein Grams: {gram_info['Protein Grams']:.2f}g")
    st.write(f"Carbohydrates Grams: {gram_info['Carbohydrates Grams']:.2f}g")
    st.write(f"Fat Grams: {gram_info['Fat Grams']:.2f}g")

    # Bar Plot for Nutritional Information
    fig, ax = plt.subplots(figsize=(8, 6))
    nutrients = ["Protein", "Carbohydrates", "Fat"]
    values = [gram_info["Protein Grams"], gram_info["Carbohydrates Grams"], gram_info["Fat Grams"]]
    ax.bar(nutrients, values, color=["#AD88C6", "#E1AFD1", "#CDE8E5"])
    ax.set_ylabel("Grams")
    ax.set_title("Nutritional Information (Grams)")
    st.subheader("Nutritional Information (Grams):")
    st.pyplot(fig)

    # Doughnut Chart for Calorie Distribution
    labels = ["Protein", "Carbohydrates", "Fat"]
    sizes = [nutritional_values["Protein Calories"], nutritional_values["Carbohydrates Calories"], nutritional_values["Fat Calories"]]
    colors = ["#AD88C6", "#E1AFD1", "#CDE8E5"]
    explode = (0.1, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, explode=explode)
    ax.axis("equal")
    ax.set_title("Calorie Distribution")
    st.subheader("Calorie Distribution:")
    st.pyplot(fig)


