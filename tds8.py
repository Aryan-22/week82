import streamlit as st

st.header("User Input Parameters")
def user_input_features():
    a = st.number_input("enter first number")
    b = st.number_input("enter second number")
    c = st.number_input("enter third number")
    return max(a,b,c)


ans = user_input_features()
st.write(ans)
