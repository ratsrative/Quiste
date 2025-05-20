# Import libraries
import streamlit as st
import pandas as pd
import datetime
import sqlite3 as sql

# Connect to SQLite database or create it if not exist
con = sql.connect('garba_sessions.db')

# Create tables if not exist
con.execute('CREATE TABLE IF NOT EXISTS events (title TEXT, date TEXT, note TEXT)')

def add_event(title, date, note):
    con.execute('INSERT INTO events (title, date, note) VALUES (?, ?, ?)', (title, date, note))
    con.commit()

def view_all_events():
    return pd.read_sql('SELECT * FROM events', con)

def app():
    st.title("Garba Sessions and Events")

    # Add event
    with st.form("new_event_form"):
        st.subheader("Add New Event")
        title_field = st.text_input("Event title")
        date_field = st.date_input("Event Date")
        note_field = st.text_area("Event Notes")
        submit_button = st.form_submit_button("Add Event")
        if submit_button:
            add_event(title_field, date_field, note_field)

    # View events
    st.subheader("Upcoming Events")
    events_df = view_all_events()
    st.dataframe(events_df)

    # Select a single event
    event_selectbox = st.selectbox("Select an Event to View/Update Note", events_df['title'])
    selected_event = events_df[events_df['title'] == event_selectbox].iloc[0]
    st.write("Event Date:", selected_event['date'])
    st.write("Event Note:")
    st.text_area("", value=selected_event['note'])

if __name__ == "__main__":
    app()
