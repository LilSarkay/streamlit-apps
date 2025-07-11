# Import necessary library
import streamlit as st

# Conversion function: added error handling for unsupported conversions
def convert_units(value, from_unit, to_unit):
    try:
        if from_unit == to_unit:
            return value
        elif from_unit == "meters" and to_unit == "kilometers":
            return value / 1000
        elif from_unit == "kilometers" and to_unit == "meters":
            return value * 1000
        # Placeholder for more conversion logic
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")
        return null

# Streamlit app layout
def main():
    st.title("Unit Converter")
    value = st.number_input("Enter the value to convert")
    from_unit = st.selectbox("From unit", ["meters", "kilometers"])
    to_unit = st.selectbox("To unit", ["meters", "kilometers"])
    result = convert_units(value, from_unit, to_unit)
    if result is not null:
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()