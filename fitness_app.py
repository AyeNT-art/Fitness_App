import streamlit as st
import datetime

# Application Page Configuration
st.set_page_config(page_title="Elite Fitness & Nutrition", page_icon="🏋️‍♂️", layout="wide")

# Custom Styling for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stCheckbox { background: white; padding: 10px; border-radius: 8px; border: 1px solid #ddd; margin-bottom: 5px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { font-weight: bold; padding: 10px 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Elite 7-Day Fitness & Nutrition Coach")

# --- SIDEBAR: USER INPUTS ---
st.sidebar.header("Personal Profile")
name = st.sidebar.text_input("Full Name", "Champion")
weight = st.sidebar.number_input("Weight (kg)", value=81.65)
height = st.sidebar.number_input("Height (cm)", value=162.56)

# BMI Logic
bmi = weight / ((height/100) ** 2)

# --- DATABASE: WORKOUT & NUTRITION ---
today = datetime.datetime.now().strftime("%A")

# 7-Day Workout Data
workout_data = {
    "Monday": {"focus": "Chest + Triceps", "exercises": ["Bench Press – 4 × 10", "Incline Dumbbell Press – 3 × 10", "Push Ups – 3 × 15", "Tricep Dips – 3 × 12", "Tricep Pushdown – 3 × 12", "Cardio (Treadmill) – 15 min"]},
    "Tuesday": {"focus": "Back + Biceps", "exercises": ["Lat Pulldown – 4 × 10", "Seated Row – 3 × 10", "Dumbbell Row – 3 × 10", "Barbell Curl – 3 × 12", "Hammer Curl – 3 × 12", "Cardio – 15 min"]},
    "Wednesday": {"focus": "Rest / Light Cardio", "exercises": ["Walking / Cycling – 30 min", "Stretching – 10 min"]},
    "Thursday": {"focus": "Legs", "exercises": ["Squats – 4 × 10", "Leg Press – 3 × 12", "Lunges – 3 × 10", "Leg Curl – 3 × 12", "Calf Raises – 3 × 15", "Cardio – 10 min"]},
    "Friday": {"focus": "Shoulders + Abs", "exercises": ["Shoulder Press – 4 × 10", "Lateral Raise – 3 × 12", "Front Raise – 3 × 12", "Plank – 3 × 40 sec", "Crunch – 3 × 20", "Cardio – 15 min"]},
    "Saturday": {"focus": "Active Recovery", "exercises": ["Light Cardio / Sports – 30 min"]},
    "Sunday": {"focus": "Rest & Recovery", "exercises": ["Rest Day 😴", "Prepare for next week!"]}
}

# 7-Day Nutrition Data
nutrition_data = {
    "Monday": {"bf": "Oatmeal 1 bowl, Boiled eggs 2, Banana 1", "lunch": "Brown rice 1 cup, Grilled chicken, Broccoli/Veg", "snack": "Yogurt, Almonds", "dinner": "Grilled fish, Salad, Sweet potato 1"},
    "Tuesday": {"bf": "Whole wheat bread 2, Peanut butter, Boiled eggs 2, Apple", "lunch": "Brown rice, Chicken curry (low oil), Veg", "snack": "Banana + Yogurt", "dinner": "Tuna salad, Boiled egg 1"},
    "Wednesday": {"bf": "Oatmeal, 2 Boiled eggs, Orange", "lunch": "Rice 1 cup, Grilled fish, Spinach/Veg", "snack": "Nuts, Apple", "dinner": "Chicken salad, Sweet potato"},
    "Thursday": {"bf": "Whole wheat bread 2, Omelette (2 eggs), Banana", "lunch": "Brown rice, Chicken breast, Veg", "snack": "Yogurt, Almonds", "dinner": "Grilled fish, Salad"},
    "Friday": {"bf": "Oatmeal, Boiled eggs 2, Apple", "lunch": "Rice, Fish curry (low oil), Veg", "snack": "Banana + Peanuts", "dinner": "Chicken salad, Sweet potato"},
    "Saturday": {"bf": "Whole wheat bread, Peanut butter, Boiled eggs", "lunch": "Brown rice, Grilled chicken, Veg", "snack": "Yogurt, Apple", "dinner": "Tuna salad"},
    "Sunday": {"bf": "Oatmeal, Eggs 2, Banana", "lunch": "Rice, Fish/Chicken, Veg", "snack": "Nuts, Fruit", "dinner": "Chicken salad, Sweet potato"}
}

# --- MAIN DASHBOARD ---
st.write(f"### Welcome back, {name}! ✨")
st.write(f"Today is **{today}**")

tab1, tab2, tab3 = st.tabs(["🏋️‍♂️ Workout Plan", "🥗 Nutrition Plan", "📊 My Status"])

with tab1:
    today_workout = workout_data[today]
    st.header(f"Focus: {today_workout['focus']}")
    st.write("Mark your progress:")
    for ex in today_workout['exercises']:
        st.checkbox(ex, key=ex)

with tab2:
    today_nutri = nutrition_data[today]
    st.header(f"Meal Plan for {today}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🍳 Breakfast")
        st.info(today_nutri['bf'])
        st.subheader("🍎 Snack")
        st.info(today_nutri['snack'])
    with col2:
        st.subheader("🍱 Lunch")
        st.success(today_nutri['lunch'])
        st.subheader("🥗 Dinner")
        st.success(today_nutri['dinner'])
    
    st.divider()
    st.subheader("💡 Important Tips")
    st.markdown("- 💧 Drink 2.5–3L Water\n- 🍗 High Protein Focus\n- 🏋️ After workout: Banana + Protein")

with tab3:
    st.header("Body Metrics & Tips")
    st.metric("Your BMI", round(bmi, 2))
    
    st.markdown("### ❗ Success Guidelines")
    st.write("✅ Sleep 7-8 hours for recovery")
    st.write("✅ Limit sugar, fried foods, and alcohol")
    st.write("📈 Expected: 3-5 kg loss in 3-4 weeks")

# --- FOOTER ---
st.divider()
st.markdown("<h3 style='text-align: center; color: #E74C3C;'>\"Your only limit is you. Build the best version of yourself!\"</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6;'>Consistency is the key to transformation.</p>", unsafe_allow_html=True)