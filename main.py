import streamlit as st
import pandas as pd

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

st.title('Daily Expense Tracker')

# Input fields
expense_date = st.date_input('Date')
category = st.selectbox('Category', ['Food', 'Transportation', 'Bills', 'Entertainment', 'Other'])
amount = st.number_input('Amount', min_value=0.0, format='%0.2f')

# Add Expense Button
if st.button('Add Expense'):
    st.session_state.expenses.append({'Date': expense_date, 'Category': category, 'Amount': amount})

# Expense Data Display
if st.session_state.expenses:
    st.subheader('Expenses')
    expenses_df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(expenses_df)

    # Total Expenditure Calculation
    total_expenditure = expenses_df['Amount'].sum()
    st.markdown(f'**Total Expenditure:** ${total_expenditure:.2f}')