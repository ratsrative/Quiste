import streamlit as st
from datetime import datetime
import smtplib
import pandas as pd

# Create dataframe for storing event data
df = pd.DataFrame(columns=['event_name', 'event_date', 'event_notes'])

# SMTP setup
smtp_server = smtplib.SMTP('localhost')

def send_email(msg, receiver_email):
    # Add your own secure data for using SMTP
    sender_email = ""  # ENTER YOUR SENDER EMAIL HERE
    password = ""  # ENTER YOUR SENDER EMAIL'S PASSWORD HERE

    message = 'Subject: {}\n\n{}'.format('Garba Reminder', msg)
    smtp_server.login(sender_email, password)
    smtp_server.sendmail(sender_email, receiver_email, message)

############# Navigation between pages #############
page = st.sidebar.selectbox("Choose a page", ['Dashboard', 'Add event', 'Calendar', 'Send Email'])

# Page routing
if page == 'Dashboard':
    st.title('Upcoming Sessions and Events')
    st.table(df[df['event_date']>datetime.now()].sort_values(by='event_date'))

elif page == 'Add event':
    st.title("Add a new event")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    event_notes = st.text_area("Event Notes")

    add_event = st.button('Add event')

    if add_event:
        df = df.append({'event_name': event_name, 
                        'event_date': event_date, 
                        'event_notes': event_notes}, 
                        ignore_index=True)
        df.to_csv('events.csv')

elif page == 'Calendar':
    st.title('Calendar')
    # Display calendar with events

elif page == 'Send Email':
    st.title('Send Email')
    msg = st.text_area("Enter your message")
    receiver_email = st.text_input("Receiver Email")
    if st.button('Send Email'):
        send_email(msg, receiver_email)
        st.success('Email sent')
