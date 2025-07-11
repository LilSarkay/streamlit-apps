import streamlit as st

def convert_units(amount, from_unit, to_unit):
    conversion_factors = {
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('feet', 'meters'): 0.3048,
        ('meters', 'feet'): 1/0.3048,
        ('miles', 'kilometers'): 1.60934,
        ('kilometers', 'miles'): 1/1.60934,
        # Add more conversions as needed
    }
    
    factor = conversion_factors.get((from_unit, to_unit), null)
    
    if factor is null:
        st.error(f"No conversion path exists from {from_unit} to {to_unit}.")
        return null
    else:
        return amount * factor

# Streamlit app logic
def main():
    st.title('Unit Converter')
    
    amount = st.number_input('Enter the amount to convert:', value=0.0)
    from_unit = st.selectbox('From Unit:', ['meters', 'kilometers', 'feet', 'miles'])
    to_unit = st.selectbox('To Unit:', ['meters', 'kilometers', 'feet', 'miles'])
    
    converted_amount = convert_units(amount, from_unit, to_unit)
    
    if converted_amount is not null:
        st.write(f'{amount} {from_unit} is equal to {converted_amount} {to_unit}')
    else:
        st.write('Conversion failed due to invalid conversion path.')

if __name__ == '__main__':
    main()