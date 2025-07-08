import streamlit as st
import pandas as pd

# Set up the app
st.title('Daily Expense Tracker')

# Initialize session state for expenses if it doesn't exist yet
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

# Input form for an expense entry
with st.form('expense_form'):
    expense_name = st.text_input('Expense Name')
    amount = st.number_input('Amount', min_value=0.0, format="%0.2f")
    category = st.selectbox('Category', ['Food', 'Transport', 'Utilities', 'Entertainment', 'Other'])
    submitted = st.form_submit_button('Add Expense')

    if submitted:
        st.session_state.expenses.append({'name': expense_name, 'amount': amount, 'category': category})
        st.success('Expense Added!')

# Display the list of expenses
st.header('Expenses')
expenses_df = pd.DataFrame(st.session_state.expenses)
if not expenses_df.empty:
    st.dataframe(expenses_df)

    # Calculate the total expenses
    total = expenses_df['amount'].sum()
    st.write(f'Total Spent: ${total:.2f}')
else:
    st.write('No expenses added yet.')