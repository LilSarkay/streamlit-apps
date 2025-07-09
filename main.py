import streamlit as st

# App title
st.title('Daily Planner')

# Initialize session state with a task list
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a task
def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ''  # Clear input field

# Function to clear all tasks
def clear_all():
    st.session_state.tasks = []

# Text input for new task
st.text_input('Enter a new task:', key='new_task', on_change=add_task)

# Display existing tasks
st.write('## Your Tasks')
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f'{i}. {task}')
else:
    st.write('No tasks added.')

# Buttons to add task and clear list
st.button('Add Task', on_click=add_task)
st.button('Clear All', on_click=clear_all)