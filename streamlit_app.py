import streamlit as st
import requests

API_URL = "http://localhost:8000/ticket"

st.set_page_config(
    page_title="AI Support Ticket Assistant",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 AI Support Ticket Assistant")

ticket = st.text_area(
    "Enter Support Ticket",
    height=150,
    placeholder="Example: Payment failed after entering card details"
)

if st.button("Analyze Ticket"):

    if not ticket.strip():
        st.warning("Please enter a ticket.")
        st.stop()

    with st.spinner("Analyzing..."):

        response = requests.post(
            API_URL,
            json={"ticket": ticket}
        )

        result = response.json()

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Category", result["category"])

    with col2:
        st.metric("Priority", result["priority"])

    st.subheader("Solution")

    st.write(result["solution"])

    st.subheader("Escalation")

    if result["escalate"]:
        st.error("Escalation Required")
    else:
        st.success("No Escalation Required")

    st.subheader("Assigned Team")

    st.info(result["assigned_team"])
