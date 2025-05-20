import streamlit as st

st.title('Medicine and Appointment Tracker')

# Glassmorphism CSS
st.markdown(
    """
    <style>
    .glass {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Medicine Tracking
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.header('Medicine Tracking')
medicine_name = st.text_input('Medicine Name')
dosage = st.text_input('Dosage')
medicine_time = st.time_input('Time', key='medicine_time')

if st.button('Add Medicine'):
    st.write(f'Medicine: {medicine_name}, Dosage: {dosage}, Time: {medicine_time}')
st.markdown('</div>', unsafe_allow_html=True)

# Appointment Tracking
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.header('Doctor\'s Appointment Tracking')
doctor_name = st.text_input('Doctor\'s Name')
date = st.date_input('Date')
appointment_time = st.time_input('Time', key="appointment_time")
notes = st.text_area('Notes')

if st.button('Add Appointment'):
    st.write(f'Doctor: {doctor_name}, Date: {date}, Time: {appointment_time}, Notes: {notes}')
st.markdown('</div>', unsafe_allow_html=True)
