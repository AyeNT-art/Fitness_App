import streamlit as st
import datetime

# Application Page Configuration
st.set_page_config(page_title="Elite Fitness Coach", page_icon="🏋️‍♂️", layout="wide")

# --- 🎨 UI COLOR FIX (စာသားနှင့် Box အရောင်များ ပြင်ဆင်ခြင်း) ---
st.markdown("""
    <style>
    /* 1. တစ်ခုလုံးကို White Background ပြောင်းခြင်း */
    .stApp {
        background-color: #ffffff !important;
    }

    /* 2. Sidebar အရောင်နှင့် စာသားများ */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
    }
    
    /* Sidebar ထဲက စာသားအားလုံးကို အမည်းရောင်ပြောင်းခြင်း */
    section[data-testid="stSidebar"] .stText, 
    section[data-testid="stSidebar"] label p {
        color: #000000 !important;
        font-weight: bold !important;
    }

    /* 3. INPUT BOXES (Name, Weight, Height) ပြင်ဆင်ခြင်း */
    div[data-baseweb="input"] {
        background-color: #ffffff !important; /* Box ကို အဖြူရောင်ထားမယ် */
        border: 2px solid #1f77b4 !important; /* အပြာရောင် ဘောင်ခတ်မယ် */
        border-radius: 10px !important;
    }

    /* Box ထဲမှာ ရိုက်မယ့်စာသားကို အမည်းရောင် အပိုင်သတ်မှတ်ခြင်း */
    input {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Number input က မြှားလေးတွေကို ပြန်ဖော်ခြင်း */
    button[title="Step up"], button[title="Step down"] {
        color: #000000 !important;
    }

    /* 4. TABS & OTHER TEXT */
    .stTabs [data-baseweb="tab"] p {
        color: #000000 !important;
    }
    h1, h2, h3, p {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️‍♂️ Elite 7-Day Fitness & Nutrition Coach")

# --- SIDEBAR: USER PROFILE ---
st.sidebar.header("User Dashboard")
# ဒီနေရာမှာ variable တွေကို သေချာသတ်မှတ်ထားပါတယ်
name = st.sidebar.text_input("Name", "Champion")
weight = st.sidebar.number_input("Weight (kg)", value=81.65)
height = st.sidebar.number_input("Height (cm)", value=162.56)

# BMI Logic
bmi = weight / ((height/100) ** 2)

# --- DYNAMIC DATE LOGIC ---
today_dt = datetime.datetime.now()
today_name = today_dt.strftime("%A") 
real_date = today_dt.strftime("%d %b %Y") 

# Data (Workout & Nutrition)
workout_data = {
    "Monday": {"focus": "Chest + Triceps", "ex": ["Bench Press – 4 × 10", "Incline Dumbbell Press – 3 × 10", "Push Ups – 3 × 15"]},
    "Tuesday": {"focus": "Back + Biceps", "ex": ["Lat Pulldown – 4 × 10", "Seated Row – 3 × 10", "Barbell Curl – 3 × 12"]},
    "Wednesday": {"focus": "Rest Day", "ex": ["Light Walking – 30 min"]},
    "Thursday": {"focus": "Legs", "ex": ["Squats – 4 × 10", "Leg Press – 3 × 12"]},
    "Friday": {"focus": "Shoulders", "ex": ["Shoulder Press – 4 × 10", "Lateral Raise – 3 × 12"]},
    "Saturday": {"focus": "Active Recovery", "ex": ["Stretching – 20 min"]},
    "Sunday": {"focus": "Rest Day", "ex": ["Full Rest 😴"]}
}

# --- MAIN DASHBOARD ---
st.write(f"### Welcome, {name}! ✨")
st.markdown(f"Today is **{today_name}** ({real_date})")

# 🛑 အရေးကြီး - Tab တွေကို အရင် Define လုပ်ရပါမယ် (NameError မတက်အောင်)
tab1, tab2, tab3 = st.tabs(["📅 Daily Workout", "🥗 Daily Nutrition", "📈 Progress Status"])

with tab1:
    plan = workout_data.get(today_name, workout_data["Monday"])
    st.subheader(f"Focus: {plan['focus']}")
    for ex in plan['ex']:
        st.checkbox(ex, key=f"ex_{ex}_{today_name}")

with tab2:
    st.subheader(f"Nutrition Plan for {today_name}")
    st.info("High Protein Diet: 1.5g per kg of bodyweight.")

with tab3:
    st.subheader("Your Body Metrics")
    st.metric(label="Calculated BMI", value=round(bmi, 2))
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Category: Normal Weight")
    else:
        st.error("Category: Overweight")

st.divider()
st.markdown("<h3 style='text-align: center; color: #1f77b4;'>\"Your only limit is you!\"</h3>", unsafe_allow_html=True)
