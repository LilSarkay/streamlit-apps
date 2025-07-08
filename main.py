import streamlit as st

# Initialize session state for expenses if not already in session state
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

# Title of the app
st.title('Daily Expense Tracker')

# Input form for adding new expenses
with st.form(key='expense_form'):
    expense = st.text_input(label='Enter expense description')
    amount = st.number_input(label='Enter expense amount', min_value=0.0, format='%.2f')
    category = st.selectbox('Select Category', ('Groceries', 'Utilities', 'Entertainment', 'Miscellaneous'))
    submit_button = st.form_submit_button(label='Add Expense')

# Add expense to session state if form is submitted
if submit_button and expense and amount:
    st.session_state['expenses'].append({'description': expense, 'amount': amount, 'category': category})
    st.success(f'Added: {expense} - ${amount} under {category}')

# Display total expenses and breakdown by category
if st.session_state['expenses']:
    total = sum(exp['amount'] for exp in st.session_state['expenses'])
    st.subheader(f'Total Expenses: ${total:.2f}')

    st.subheader('Breakdown by Category:')
    for cat in set(exp['category'] for exp in st.session_state['expenses']):
        cat_total = sum(exp['amount'] for exp in st.session_state['expenses'] if exp['category'] == cat)
        st.write(f'{cat}: ${cat_total:.2f}')

    # Display all expenses
    st.subheader('All Expenses:')
    st.table(st.session_state['expenses'])