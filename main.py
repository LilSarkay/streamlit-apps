import streamlit as st
import pandas as pd

# Initialize session state to store the expenses if not already initialized
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

st.title('Daily Expense Tracker')

# Input for adding a new expense
with st.form(key='expense_form', clear_on_submit=true):
    name = st.text_input('Expense Name')
    amount = st.number_input('Amount', min_value=0.01, step=0.01)
    category = st.selectbox('Category', ['Food', 'Transport', 'Utilities', 'Other'])
    submit_button = st.form_submit_button(label='Add Expense')

# Append to session state and DataFrame
if submit_button and name and amount and category:
    st.session_state['expenses'].append({'name': name, 'amount': amount, 'category': category})

# Displaying the expenses
if st.session_state['expenses']:
    exp_df = pd.DataFrame(st.session_state['expenses'])
    st.subheader('Expenses')
    st.table(exp_df)

    # Calculate and display total
    total = exp_df['amount'].sum()
    st.write(f'Total Expenses: ${total:.2f}')
else:
    st.write('No expenses added yet.'}