import streamlit as st
import datetime

# Application Page Configuration
st.set_page_config(page_title="Elite Fitness Coach", page_icon="🏋️‍♂️", layout="wide")

# --- THE FINAL UI FIX (FORCE LIGHT MODE) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; color: #000000 !important; }
    h1, h2, h3, h4, h5, h6, p, span, label, div { color: #000000 !important; }
    section[data-testid="stSidebar"] { background-color: #f8f9fa !important; }
    div[data-baseweb="input"] { background-color: #ffffff !important; border: 1px solid #d1d5db !important; border-radius: 8px !important; }
    input { color: #000000 !important; -webkit-text-fill-color: #000000 !important; }
    .stCheckbox { background-color: #f1f3f6 !important; padding: 15px !important; border-radius: 12px !important; border: 1px solid #d1d5db !important; margin-bottom: 10px !important; }
    .stTabs [data-baseweb="tab-list"] { background-color: #ffffff !important; }
    .stTabs [data-baseweb="tab"] p { color: #000000 !important; font-weight: bold !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #1f77b4 !important; color: #ffffff !important; }
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

# --- DYNAMIC DATE LOGIC ---
today_dt = datetime.datetime.now()
today_name = today_dt.strftime("%A") 
real_date = today_dt.strftime("%d %b %Y") 

# Data
workout_data = {
    "Monday": {"focus": "Chest + Triceps", "ex": ["Bench Press – 4 × 10", "Incline Dumbbell Press – 3 × 10", "Push Ups – 3 × 15", "Tricep Dips – 3 × 12", "Tricep Pushdown – 3 × 12", "Cardio – 15 min"]},
    "Tuesday": {"focus": "Back + Biceps", "ex": ["Lat Pulldown – 4 × 10", "Seated Row – 3 × 10", "Dumbbell Row – 3 × 10", "Barbell Curl – 3 × 12", "Hammer Curl – 3 × 12", "Cardio – 15 min"]},
    "Wednesday": {"focus": "Rest / Light Cardio", "ex": ["Walking / Cycling – 30 min", "Stretching – 10 min"]},
    "Thursday": {"focus": "Legs", "ex": ["Squats – 4 × 10", "Leg Press – 3 × 12", "Lunges – 3 × 10", "Leg Curl – 3 × 12", "Calf Raises – 3 × 15", "Cardio – 10 min"]},
    "Friday": {"focus": "Shoulders + Abs", "ex": ["Shoulder Press – 4 × 10", "Lateral Raise – 3 × 12", "Front Raise – 3 × 12", "Plank – 3 × 40 sec", "Crunch – 3 × 20", "Cardio – 15 min"]},
    "Saturday": {"focus": "Active Recovery", "ex": ["Light Cardio / Sports – 30 min"]},
    "Sunday": {"focus": "Rest Day", "ex": ["Complete Rest & Recovery 😴"]}
}

nutrition_data = {
    "Monday": {"bf": "Oatmeal, Eggs, Banana", "lunch": "Brown rice, Chicken, Veg", "snack": "Yogurt", "dinner": "Fish, Salad"},
    "Tuesday": {"bf": "Bread, PB, Eggs", "lunch": "Brown rice, Curry, Veg", "snack": "Apple", "dinner": "Tuna salad"},
    "Wednesday": {"bf": "Oatmeal, Eggs", "lunch": "Rice, Fish, Veg", "snack": "Nuts", "dinner": "Chicken salad"},
    "Thursday": {"bf": "Bread, Omelette", "lunch": "Brown rice, Chicken", "snack": "Yogurt", "dinner": "Fish, Salad"},
    "Friday": {"bf": "Oatmeal, Eggs", "lunch": "Rice, Fish curry", "snack": "Banana", "dinner": "Chicken salad"},
    "Saturday": {"bf": "Bread, PB, Eggs", "lunch": "Brown rice, Chicken", "snack": "Apple", "dinner": "Tuna salad"},
    "Sunday": {"bf": "Oatmeal, Eggs", "lunch": "Rice, Chicken, Veg", "snack": "Fruit", "dinner": "Chicken salad"}
}

# --- MAIN DASHBOARD ---
st.write(f"### Welcome, {name}! ✨")
st.markdown(f"Today is **{today_name}** ({real_date})")

# DEFINE TABS
tab1, tab2, tab3 = st.tabs(["📅 Daily Workout", "🥗 Daily Nutrition", "📈 Progress Status"])

with tab1:
    plan = workout_data.get(today_name, workout_data["Monday"])
    st.subheader(f"Focus: {plan['focus']}")
    for ex in plan['ex']:
        st.checkbox(ex, key=f"ex_{ex}_{today_name}")

with tab2:
    nutri = nutrition_data.get(today_name, nutrition_data["Monday"])
    st.subheader(f"Meal Plan for {today_name}")
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"**Breakfast:** {nutri['bf']}")
        st.info(f"**Snack:** {nutri['snack']}")
    with c2:
        st.success(f"**Lunch:** {nutri['lunch']}")
        st.success(f"**Dinner:** {nutri['dinner']}")

with tab3:
    st.subheader("Your Body Metrics")
    st.metric("Your BMI", round(bmi, 2))
    st.divider()
    st.markdown("### ❗ Key Success Tips")
    st.write("- **Water:** 2.5–3 Liters Daily")
    st.write("- **Sleep:** 7–8 Hours")

st.divider()
st.markdown("<h3 style='text-align: center; color: #1f77b4;'>\"Your only limit is you!\"</h3>", unsafe_allow_html=True)
