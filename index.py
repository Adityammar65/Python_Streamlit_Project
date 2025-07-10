import streamlit as st

info=st.toggle("You can toggle this")

st.markdown(
    """
    # This is a testing code using streamlit framework
    Greetings everyone!
    """
)

if info:
    st.markdown(
        """
        # My name is Ammar
        I am a student in University of Amikom Yogyakarta
        """
    )
