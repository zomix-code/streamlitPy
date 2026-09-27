import streamlit as st


st.title("Calculator")


def calculate(input_text):
    try:
        return eval(input_text)
    except NameError:
        st.warning("Here a mistake in value")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None


num = st.text_input("Enter value here")

if st.button("Confirm"):
    result = calculate(num)
    

    if result is not None:
        st.success(f"Here youre number: {result}")