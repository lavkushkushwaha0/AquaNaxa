import streamlit as st
import random
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AquaNexa Monitor", layout="wide")

# --- FRONTEND: TITLE ---
st.title("💧 AquaNexa: Smart Water Quality Monitoring")
st.write("Real-time monitoring for Household Tanks & Taps")
st.markdown("---")

# --- BACKEND: LOGIC FUNCTIONS ---

def generate_data():
    """IoT Sensor se real-time data lane ka logic (Simulated)"""
    return {
        "pH": round(random.uniform(6.0, 9.5), 2),
        "TDS": random.randint(150, 750),
        "Turbidity": round(random.uniform(0.5, 12.0), 2)
    }

def check_safety(data):
    """Pani ki quality analyze karne ka backend logic"""
    alerts = []
    status = "SAFE"
    
    # pH Level Check
    if data["pH"] < 6.5 or data["pH"] > 8.5:
        alerts.append("🔴 pH Level Abnormal: Chemical contamination ka khatra hai.")
        status = "UNSAFE"
    
    # TDS (Tank Cleanliness) Check
    if data["TDS"] > 500:
        alerts.append("🟡 High TDS: Aapka Overhead Tank ganda hai, cleaning ki zaroorat hai.")
        status = "UNSAFE"
        
    # Turbidity (Pipeline/Mud) Check
    if data["Turbidity"] > 5.0:
        alerts.append("🟠 High Turbidity: Supply line mein mitti ya sudden contamination hai.")
        status = "UNSAFE"
        
    return status, alerts

# --- FRONTEND & BACKEND CONNECTION ---

# 1. Data generate karo
data = generate_data()

# 2. Safety status check karo
status, alerts = check_safety(data)

# 3. Display Overall Status (User-friendly Alert)
if status == "SAFE":
    st.success("### ✅ TANK STATUS: SAFE")
    st.info("Pani peene aur ghar ke kamo ke liye surakshit hai.")
else:
    st.error(f"### ⚠️ TANK STATUS: {status}")
    for a in alerts:
        st.warning(a)

st.markdown("---")

# 4. Metrics Display (Visual Gauges/Boxes)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="pH Level", value=data["pH"], delta_color="inverse")
with col2:
    st.metric(label="TDS (ppm)", value=f"{data['TDS']} mg/L")
with col3:
    st.metric(label="Turbidity (NTU)", value=f"{data['Turbidity']} NTU")

# 5. Manual Refresh Button
st.sidebar.header("Controls")
if st.sidebar.button('🔄 Refresh Sensor Reading'):
    st.rerun()

st.sidebar.markdown("---")

st.sidebar.caption("Project: AquaNexa | Smart Household Monitoring")
