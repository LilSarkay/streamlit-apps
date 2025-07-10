__updated__ = "Thu Jul 10 07:07:15 UTC 2025"
import streamlit as st

def main():
    st.title('Color Picker App')
    
    # Dropdown for color selection
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'White']
    selected_color = st.selectbox('Select a color', colors)
    
    # Set the background color
    st.markdown(f"<style>body {{ background-color: {selected_color.lower()}; }}</style>", unsafe_allow_html=true)

if __name__ == '__main__':
    main()