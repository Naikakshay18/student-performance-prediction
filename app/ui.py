import streamlit as st

def hero():
    st.markdown(
        """
        <div style="
            background:#1A73E8;
            padding:30px;
            border-radius:20px;
            text-align:center;
            color:white;
            margin-bottom:20px;
        ">
            <h1 style="color:white;margin:0;">
                🎓 Student Performance Predictor
            </h1>
            <p style="color:white;font-size:18px;">
                Predict academic performance using Machine Learning
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )