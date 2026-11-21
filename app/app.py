import streamlit as st
import pandas as pd
import joblib
from ui import hero

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

def load_css():
    with open("app/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------
# LOAD FILES
# ---------------------------------
model = joblib.load("models/student_model.pkl")
encoders = joblib.load("models/label_encoders.pkl")

original_df = pd.read_csv("data/StudentPerformanceFactors.csv")
clean_df = pd.read_csv("data/cleaned_student_data.csv")

feature_columns = [c for c in clean_df.columns if c != "Exam_Score"]

# ---------------------------------
# SIDEBAR
# ---------------------------------


# ---------------------------------
# MAIN TITLE
# ---------------------------------
hero()
# ==========================================
# DASHBOARD SUMMARY
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Students", original_df.shape[0])

with col2:
    st.metric("Features", len(feature_columns))

with col3:
    st.metric("Model", "Random Forest")

st.markdown("<br>", unsafe_allow_html=True)

user_input = {}
# ==========================================
# INPUT SECTION
# ==========================================

st.markdown("## Student Information")
# ---------------- Academic ----------------

with st.expander("📚 Academic Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        user_input["Hours_Studied"] = st.slider(
            "Hours Studied",
            1,
            44,
            20
        )

        user_input["Attendance"] = st.slider(
            "Attendance (%)",
            60,
            100,
            80
        )

        user_input["Previous_Scores"] = st.slider(
            "Previous Scores",
            50,
            100,
            75
        )

    with col2:

        user_input["Sleep_Hours"] = st.slider(
            "Sleep Hours",
            4,
            10,
            7
        )

        user_input["Tutoring_Sessions"] = st.slider(
            "Tutoring Sessions",
            0,
            8,
            2
        )

        user_input["Physical_Activity"] = st.slider(
            "Physical Activity",
            0,
            6,
            3
        )

# ---------------- Family ----------------

with st.expander("🏠 Family & Environment"):

    c1, c2 = st.columns(2)

    with c1:

        p = st.selectbox(
            "Parental Involvement",
            encoders["Parental_Involvement"].classes_
        )
        user_input["Parental_Involvement"] = encoders[
            "Parental_Involvement"
        ].transform([p])[0]

        a = st.selectbox(
            "Access to Resources",
            encoders["Access_to_Resources"].classes_
        )
        user_input["Access_to_Resources"] = encoders[
            "Access_to_Resources"
        ].transform([a])[0]

        f = st.selectbox(
            "Family Income",
            encoders["Family_Income"].classes_
        )
        user_input["Family_Income"] = encoders[
            "Family_Income"
        ].transform([f])[0]

        pe = st.selectbox(
            "Parental Education",
            encoders["Parental_Education_Level"].classes_
        )
        user_input["Parental_Education_Level"] = encoders[
            "Parental_Education_Level"
        ].transform([pe])[0]

    with c2:

        d = st.selectbox(
            "Distance From Home",
            encoders["Distance_from_Home"].classes_
        )
        user_input["Distance_from_Home"] = encoders[
            "Distance_from_Home"
        ].transform([d])[0]

        internet = st.selectbox(
            "Internet Access",
            encoders["Internet_Access"].classes_
        )
        user_input["Internet_Access"] = encoders[
            "Internet_Access"
        ].transform([internet])[0]

        teacher = st.selectbox(
            "Teacher Quality",
            encoders["Teacher_Quality"].classes_
        )
        user_input["Teacher_Quality"] = encoders[
            "Teacher_Quality"
        ].transform([teacher])[0]

# ---------------- Personal ----------------

with st.expander("👤 Personal Information"):

    c1, c2 = st.columns(2)

    with c1:

        gender = st.selectbox(
            "Gender",
            encoders["Gender"].classes_
        )
        user_input["Gender"] = encoders["Gender"].transform([gender])[0]

        school = st.selectbox(
            "School Type",
            encoders["School_Type"].classes_
        )
        user_input["School_Type"] = encoders[
            "School_Type"
        ].transform([school])[0]

        activity = st.selectbox(
            "Extracurricular Activities",
            encoders["Extracurricular_Activities"].classes_
        )
        user_input["Extracurricular_Activities"] = encoders[
            "Extracurricular_Activities"
        ].transform([activity])[0]

    with c2:

        motivation = st.selectbox(
            "Motivation Level",
            encoders["Motivation_Level"].classes_
        )
        user_input["Motivation_Level"] = encoders[
            "Motivation_Level"
        ].transform([motivation])[0]

        peer = st.selectbox(
            "Peer Influence",
            encoders["Peer_Influence"].classes_
        )
        user_input["Peer_Influence"] = encoders[
            "Peer_Influence"
        ].transform([peer])[0]

        disability = st.selectbox(
            "Learning Disabilities",
            encoders["Learning_Disabilities"].classes_
        )
        user_input["Learning_Disabilities"] = encoders[
            "Learning_Disabilities"
        ].transform([disability])[0]

# ==========================================
# PREDICTION
# ==========================================

st.markdown("---")

if st.button("🎯 Predict Exam Score", use_container_width=True):

    # Create DataFrame
    input_df = pd.DataFrame([user_input])

    # Arrange columns exactly like training data
    input_df = input_df[feature_columns]

    # Prediction
    prediction = float(model.predict(input_df)[0])

    st.markdown("## 📊 Prediction Result")

    score_col1, score_col2 = st.columns([2, 1])

    with score_col1:
        st.metric(
            label="Predicted Exam Score",
            value=f"{prediction:.2f} / 100"
        )

    with score_col2:

        if prediction >= 90:
            st.success("🌟 Excellent")
            st.balloons()

        elif prediction >= 80:
            st.success("🔥 Very Good")

        elif prediction >= 70:
            st.info("👍 Good")

        elif prediction >= 60:
            st.warning("🙂 Average")

        else:
            st.error("⚠ Needs Improvement")

    st.progress(min(prediction / 100, 1.0))

    st.markdown("---")

    st.subheader("📋 Input Summary")

    display_df = pd.DataFrame([user_input])

    st.dataframe(
        display_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📈 Score Interpretation")

    if prediction >= 90:
        st.write("Outstanding academic performance. Keep up the excellent work!")

    elif prediction >= 80:
        st.write("Very good performance with strong academic consistency.")

    elif prediction >= 70:
        st.write("Good performance. A little more effort can improve the score further.")

    elif prediction >= 60:
        st.write("Average performance. Improving study habits and attendance may help.")

    else:
        st.write("The predicted score is low. Consider increasing study hours, attendance, and seeking academic support.")