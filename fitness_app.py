import streamlit as st
import datetime

# Application Page Configuration (Tab Name & Icon)
st.set_page_config(page_title="Elite Fitness Coach", page_icon="🏋️‍♂️", layout="wide")

# --- 🛑 ALL COLOR & DISPLAY FIXES (CSS) 🛑 ---
# This forces light mode even if the phone is in dark mode
st.markdown("""
    <style>
    /* 1. App Background - Force White */
    .stApp {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* 2. All Text (Headers, Paragraphs, Labels) - Force Black */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #000000 !important;
    }

    /* 3. FIX: Sidebar Arrow & Text visibility */
    #MainMenu, header, .stApp header {
        background-color: #ffffff !important;
    }
    .stApp [data-testid="stSidebarCollapseButton"] svg {
        fill: #000000 !important; /* Forces arrow to Black */
    }
    section[data-testid="stSidebar"] {
        background-color: #f1f3f6 !important; /* Light Gray Sidebar */
    }
    section[data-testid="stSidebar"] * {
        color: #000000 !important; /* All sidebar text Black */
    }

    /* 4. FIX: Checkbox Text Visibility (ghost text fix) */
    .stCheckbox {
        background-color: #f8f9fa !important; /* Faint gray background */
        padding: 15px !important;
        border-radius: 12px !important;
        border: 1px solid #d1d5db !important;
        margin-bottom: 10px !important;
    }
    .stCheckbox label div[data-testid="stMarkdownContainer"] p {
        color: #000000 !important; /* Text is now SOLID BLACK */
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    /* 5. Tabs Styling (Daily Workout, Nutrition) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        background-color: #f1f3f6;
        color: #000000 !important;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab"] p {
        color: #000000 !important; /* Ensure Tab Text is Black */
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #1f77b4 !important; /* Blue when selected */
        color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p {
        color: #ffffff !important;
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

# --- DATABASE & DYNAMIC DAY ---
# 1. FIX: Dynamic Date Logic (Get Real Day)
today_dt = datetime.datetime.now()
today_name = today_dt.strftime("%A") # e.g., "Monday"
real_date = today_dt.strftime("%d %b %Y") # e.g., "Monday, 27 May 2024"

# Plans remain the same
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
st.markdown(f"Today is **{today_name}** ({real_date})") # Display real day and date

tab1, tab2, tab3 = st.tabs(["📅 Daily Workout", "🥗 Daily Nutrition", "📈 Progress Status"])

with tab1:
    plan = workout_data[today_name] # Use dynamic day
    st.subheader(f"Focus: {plan['focus']}")
    st.write("Mark exercises as completed:")
    for ex in plan['ex']:
        # Unique keys ensure checkboxes work independently
        st.checkbox(ex, key=f"ex_{ex}_{today_name}") 

with tab2:
    nutri = nutrition_data[today_name] # Use dynamic day
    st.subheader(f"Meal Plan for {today_name}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**🍳 Breakfast:** \n {nutri['bf']}")
        st.info(f"**🍎 Snack:** \n {nutri['snack']}")
    with col2:
        st.success(f"**🍱 Lunch:** \n {nutri['lunch']}")
        st.success(f"**🥗 Dinner:** \n {nutri['dinner']}")

with tab3:
    st.subheader("Your Body Metrics")
    # Clean, large BMI display
    st.markdown(f"<p style='font-size: 40px; font-weight: bold; color: #1f77b4 !important;'>{round(bmi, 2)}</p>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### ❗ Key Success Tips")
    st.markdown("- **Water:** 2.5–3 Liters Daily\n- **Sleep:** 7–8 Hours\n- **Expected:** 3–5 kg loss in 3–4 weeks")

# --- FOOTER ---
st.divider()
# Motivational text remains at bottom
st.markdown("<h3 style='text-align: center; color: #1f77b4 !important;'>\"Your only limit is you. Build the best version of yourself today!\"</h3>", unsafe_allow_html=True)
