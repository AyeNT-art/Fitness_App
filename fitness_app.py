import streamlit as st
import datetime

# Application Page Configuration
st.set_page_config(page_title="Elite Fitness Coach", page_icon="🏋️‍♂️", layout="wide")

# Professional CSS Styling (Clean White & Blue Theme)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f5f7f9;
    }
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-weight: bold;
        font-size: 16px;
        color: #4b4b4b;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #1f77b4;
    }
    /* Checkbox Styling for better visibility */
    .stCheckbox {
        background-color: #ffffff;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #e6e9ef;
        margin-bottom: 8px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
    }
    .stCheckbox p {
        color: #31333f !important;
        font-size: 15px !important;
    }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Elite 7-Day Fitness & Nutrition Coach")

# --- SIDEBAR: USER PROFILE ---
st.sidebar.header("User Dashboard")
name = st.sidebar.text_input("Name", "Champion")
weight = st.sidebar.number_input("Weight (kg)", value=81.65)
height = st.sidebar.number_input("Height (cm)", value=162.56)

# BMI Logic
bmi = weight / ((height/100) ** 2)

# --- DATABASE: YOUR PLANS ---
today = datetime.datetime.now().strftime("%A")

workout_data = {
    "Monday": {"focus": "Chest + Triceps", "ex": ["Bench Press – 4 × 10", "Incline Dumbbell Press – 3 × 10", "Push Ups – 3 × 15", "Tricep Dips – 3 × 12", "Tricep Pushdown – 3 × 12", "Cardio (Treadmill) – 15 min"]},
    "Tuesday": {"focus": "Back + Biceps", "ex": ["Lat Pulldown – 4 × 10", "Seated Row – 3 × 10", "Dumbbell Row – 3 × 10", "Barbell Curl – 3 × 12", "Hammer Curl – 3 × 12", "Cardio – 15 min"]},
    "Wednesday": {"focus": "Rest / Light Cardio", "ex": ["Walking / Cycling – 30 min", "Stretching – 10 min"]},
    "Thursday": {"focus": "Legs", "ex": ["Squats – 4 × 10", "Leg Press – 3 × 12", "Lunges – 3 × 10", "Leg Curl – 3 × 12", "Calf Raises – 3 × 15", "Cardio – 10 min"]},
    "Friday": {"focus": "Shoulders + Abs", "ex": ["Shoulder Press – 4 × 10", "Lateral Raise – 3 × 12", "Front Raise – 3 × 12", "Plank – 3 × 40 sec", "Crunch – 3 × 20", "Cardio – 15 min"]},
    "Saturday": {"focus": "Active Recovery", "ex": ["Light Cardio / Sports – 30 min"]},
    "Sunday": {"focus": "Rest Day", "ex": ["Complete Rest & Recovery 😴"]}
}

nutrition_data = {
    "Monday": {"bf": "Oatmeal 1 bowl, Boiled eggs 2, Banana 1", "lunch": "Brown rice 1 cup, Grilled chicken, Veg", "snack": "Yogurt, Almonds", "dinner": "Grilled fish, Salad, Sweet potato 1"},
    "Tuesday": {"bf": "Whole wheat bread 2, Peanut butter, Boiled eggs 2, Apple", "lunch": "Brown rice, Chicken curry (low oil), Veg", "snack": "Banana + Yogurt", "dinner": "Tuna salad, Boiled egg 1"},
    "Wednesday": {"bf": "Oatmeal, 2 Boiled eggs, Orange", "lunch": "Rice 1 cup, Grilled fish, Veg", "snack": "Nuts, Apple", "dinner": "Chicken salad, Sweet potato"},
    "Thursday": {"bf": "Whole wheat bread 2, Omelette (2 eggs), Banana", "lunch": "Brown rice, Chicken breast, Veg", "snack": "Yogurt, Almonds", "dinner": "Grilled fish, Salad"},
    "Friday": {"bf": "Oatmeal, Boiled eggs 2, Apple", "lunch": "Rice, Fish curry (low oil), Veg", "snack": "Banana + Peanuts", "dinner": "Chicken salad, Sweet potato"},
    "Saturday": {"bf": "Whole wheat bread, Peanut butter, Boiled eggs", "lunch": "Brown rice, Grilled chicken, Veg", "snack": "Yogurt, Apple", "dinner": "Tuna salad"},
    "Sunday": {"bf": "Oatmeal, Eggs 2, Banana", "lunch": "Rice, Fish/Chicken, Veg", "snack": "Nuts, Fruit", "dinner": "Chicken salad, Sweet potato"}
}

# --- MAIN DASHBOARD ---
st.write(f"### Welcome, {name}! ✨")
st.write(f"Today is **{today}**")

tab1, tab2, tab3 = st.tabs(["📅 Daily Workout", "🥗 Daily Nutrition", "📈 Progress Status"])

with tab1:
    plan = workout_data[today]
    st.subheader(f"Focus: {plan['focus']}")
    for ex in plan['ex']:
        st.checkbox(ex, key=f"ex_{ex}_{today}")

with tab2:
    nutri = nutrition_data[today]
    st.subheader(f"Meal Plan for {today}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**🍳 Breakfast:** \n {nutri['bf']}")
        st.info(f"**🍎 Snack:** \n {nutri['snack']}")
    with col2:
        st.success(f"**🍱 Lunch:** \n {nutri['lunch']}")
        st.success(f"**🥗 Dinner:** \n {nutri['dinner']}")

with tab3:
    st.subheader("Your Body Metrics")
    st.metric("Body Mass Index (BMI)", round(bmi, 2))
    
    st.divider()
    st.markdown("### ❗ Key Success Tips")
    st.markdown("- **Water:** 2.5–3 Liters Daily\n- **Sleep:** 7–8 Hours\n- **Expected:** 3–5 kg loss in 3–4 weeks")

# --- FOOTER ---
st.divider()
st.markdown("<h3 style='text-align: center; color: #1f77b4;'>\"Your only limit is you. Build the best version of yourself today!\"</h3>", unsafe_allow_html=True)
