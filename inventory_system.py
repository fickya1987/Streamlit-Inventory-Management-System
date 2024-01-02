from calendar import c
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import streamlit as st
import pandas as pd

# --- PAGE CONFIGS ---
st.set_page_config(
    page_title = 'Restaurant Inventory System',
    page_icon = '💻',
    layout = 'wide',
)

# --- WEBPAGE CSS ---
def css(file_name):
     with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
css("style/main.css")

col1, col2, col3 = st.columns(3)
col1.metric(label="Profit", value=5000, delta=1000)
col2.metric(label="Sales", value=5000, delta=-1000)
col3.metric(label="Expenses", value=5000, delta=0)
style_metric_cards(background_color = '#002b36', border_size_px = '5', border_color = '#586e75', border_left_color = '#ADFF2F')

def load_data():
    try:
        # Try loading the data from a CSV file
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        df = pd.DataFrame(columns=['Date', 'Sales', 'Profit', 'Expenses'])
    return df

# Function to save the DataFrame to a CSV file
def save_data(df):
    df.to_csv('your_data.csv', index=False)

# Load existing data or initialize an empty DataFrame
df = load_data()

# Title
st.title("Sales and Expenses Tracker")

# Date input
date_input = st.date_input("Select Date:", pd.to_datetime("today"))
# Text input for sales
sales_input = st.text_input("Enter Sales:", "")
# Text input for profit
profit_input = st.text_input("Enter Profit:", "")
# Text input for expenses
expenses_input = st.text_input("Enter Expenses:", "")

# Add input data to the DataFrame when the user clicks a button
if st.button("Add Data"):
    try:
        # Convert input values to appropriate data types
        sales = float(sales_input)
        profit = float(profit_input)
        expenses = float(expenses_input)

        # Create a new DataFrame with the new data and append it to the existing DataFrame
        new_data = pd.DataFrame({'Date': [date_input], 'Sales': [sales], 'Profit': [profit], 'Expenses': [expenses]})
        df = pd.concat([df, new_data], ignore_index=True)

        st.success("Data added successfully!")
    except ValueError:
        st.error("Invalid input. Please check your entries.")

# Save the DataFrame to a CSV file
save_data(df)

# Display the DataFrame
st.dataframe(df)

# --- NAVIGATION SIDEBAR ---
with st.sidebar:
    select = option_menu(
        menu_title = 'Inventory System',
        options = ['Dashboard', 'Sales', 'Expenses', 'Savings'],
        icons = [],
        default_index = 0,
    )

    