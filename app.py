import streamlit as st

st.title("Reservation Dining Credit Prototype")
st.write("This is a prototype showing how dining credits could attach to a reservation.")

name = st.text_input("Sender Name")
phone = st.text_input("Recipient Phone Number")
amount = st.number_input("Gift Amount")

if st.button("Send Dining Credit"):
    st.success(f"{name} sent ${amount} dining credit to {phone}")
