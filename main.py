import streamlit as st
import pandas as pd

# Title of the app
st.title('Daily Expense Tracker')

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Input fields for a new expense
date = st.date_input('Date')
description = st.text_input('Description')
amount = st.number_input('Amount', min_value=0.0, format='%f')

# Button to add the expense
if st.button('Add Expense'):
    # Append the new expense to the session state
    st.session_state.expenses.append({'Date': date, 'Description': description, 'Amount': amount})
    st.success('Expense added!')

# Convert session state expenses into a DataFrame
expenses_df = pd.DataFrame(st.session_state.expenses)

# Display the expenses
i
f not expenses_df.empty:
    st.subheader('Expenses Overview')
    st.table(expenses_df)

    # Calculate and display total expenses
total_expense = expenses_df['Amount'].sum()
    st.subheader(f'Total Expense: ${total_expense:.2f}')
else:
    st.info('No expenses added yet.')