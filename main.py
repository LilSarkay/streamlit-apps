__updated__ = "Wed Jul  9 10:49:38 UTC 2025"
import streamlit as st

# Title of the app
st.title('Daily Planner')

# Initialize the session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Input for a new task
task = st.text_input('Enter a task')

# Add task button
def add_task():
    if task:
        st.session_state.tasks.append(task)

st.button('Add Task', on_click=add_task)

# Clear all tasks
def clear_tasks():
    st.session_state.tasks.clear()

st.button('Clear All', on_click=clear_tasks)

# Display the list of tasks
if st.session_state.tasks:
    st.write('Your tasks:')
    for i, t in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {t}")