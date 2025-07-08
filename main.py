import streamlit as st
import pandas as pd

# Title for the app
st.title('Daily Expense Tracker')

# Initialize session state for expenses if not already done
def init():
    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []

# Call the init function to set up session state
init()

# Input fields for new expense entry
expense_name = st.text_input('Expense Name')
expense_amount = st.number_input('Expense Amount', min_value=0.0, format='%.2f')

# Button to add new expenses to the list
if st.button('Add Expense'):
    new_expense = {'name': expense_name, 'amount': expense_amount}
    st.session_state.expenses.append(new_expense)
    st.success(f"Added {expense_name} of ${expense_amount}")

# Convert session expenses to DataFrame for display
expenses_df = pd.DataFrame(st.session_state['expenses'])

# Display the expenses in a table if any exist
if not expenses_df.empty:
    st.subheader('Expenses')
    st.table(expenses_df)
    total = expenses_df['amount'].sum()
    st.markdown(f"**Total Expense:** ${total:.2f}")
else:
    st.info('No expenses added yet.')