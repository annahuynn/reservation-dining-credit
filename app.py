import streamlit as st
import pandas as pd

st.title("Reservation Dining Credit Prototype")

if "credits" not in st.session_state:
    st.session_state.credits = []

page = st.sidebar.selectbox(
    "Select View",
    ["Send Credit", "Recipient Wallet", "Restaurant Host"]
)

# SEND CREDIT

if page == "Send Credit":

    st.header("Send Dining Credit")

    sender = st.text_input("Sender Name")
    phone = st.text_input("Recipient Phone Number")
    amount = st.number_input("Gift Amount")

    if st.button("Send Credit"):

        credit = {
            "sender": sender,
            "phone": phone,
            "amount": amount
        }

        st.session_state.credits.append(credit)

        st.success("Dining credit sent!")

# RECIPIENT WALLET
elif page == "Recipient Wallet":

    st.header("Recipient Wallet")

    phone = st.text_input("Enter Phone Number")

    for credit in st.session_state.credits:
        if credit["phone"] == phone:

            st.write(
                f"Credit from {credit['sender']} : ${credit['amount']}"
            )

# RESTAURANT HOST
elif page == "Restaurant Host":

    st.header("Host View")

    phone = st.text_input("Reservation Phone")

    total = 0

    for credit in st.session_state.credits:
        if credit["phone"] == phone:
            total += credit["amount"]

    st.write(f"Available Dining Credit: ${total}")
