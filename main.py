import streamlit as st

# Title
st.title('Daily Planner')

# Sidebar with task input
with st.sidebar:
    st.header('Add New Task')
    task = st.text_input('Task Name')
    add_task = st.button('Add Task')
    
# Display tasks
st.header('Your Tasks')
tasks = ['Task 1', 'Task 2']
if add_task and task:
    tasks.append(task)
for t in tasks:
    st.write('- ', t)