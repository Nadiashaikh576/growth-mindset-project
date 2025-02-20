import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO

# Initialize or load data
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"challenges": [], "journal": []}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# Streamlit App Configuration
st.set_page_config(page_title="🌟 The Growth Mindset Hub: Empower, Challenge, Achieve", layout="wide")
st.title(" 🌱 Elevate Your Mindset: A Journey to Growth & Success")
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Choose a Section", ["Home", "Daily Challenge", "Interactive Quiz", "Journal & Reflections", "File Converter", "Growth Tracker"])

# Home Page
if page == "Home":
    st.header("Welcome to the Growth Mindset Hub!")
    st.image("https://media.istockphoto.com/id/1128571392/photo/self-development-motivational-words-quotes-concept.jpg?s=612x612&w=0&k=20&c=UGtd_Udk2a5jc3UiLyvYHlseKwPUZDV2J54d7FLR9Zg=", use_container_width=True)
    
    st.subheader("🌟 Why Growth Mindset?")
    st.write("A growth mindset helps you embrace challenges, learn from mistakes, and persist despite obstacles.")
    
    st.subheader("🚀 How to Develop a Growth Mindset?")
    st.write("- Set learning goals rather than performance goals.")
    st.write("- View challenges as opportunities to grow.")
    st.write("- Learn from criticism and feedback.")
    st.write("- Cultivate resilience and adaptability.")
    
    st.success("💡 'Your potential is limitless when you believe in growth.'")

# Daily Challenge Section
elif page == "Daily Challenge":
    st.header("💪 Today's Challenge")
    challenges = [
        "Write three things you are grateful for today.",
        "Reflect on a recent failure and identify the lesson learned.",
        "Challenge yourself to learn something new today.",
        "Step out of your comfort zone – try a new activity.",
        "Encourage someone with a growth mindset message."
    ]
    challenge = random.choice(challenges)
    st.subheader(f"✨ Challenge: {challenge}")
    response = st.text_area("How will you tackle this challenge?")
    
    if st.button("Submit Response"):
        data["challenges"].append({"challenge": challenge, "response": response})
        save_data(data)
        st.success("🎉 Response saved! Keep growing!")

# Quiz Section
elif page == "Interactive Quiz":
    st.header("🧠 Test Your Growth Mindset!")
    quiz_questions = [
        {"question": "What is a growth mindset?", "options": ["Fixed abilities", "Continuous learning", "Avoiding challenges"], "answer": "Continuous learning"},
        {"question": "How should you view criticism?", "options": ["Ignore it", "Use it to grow", "Take it personally"], "answer": "Use it to grow"}
    ]
    score = 0
    for q in quiz_questions:
        st.write(q["question"])
        option = st.radio("Choose an answer:", q["options"], key=q["question"])
        if option == q["answer"]:
            score += 1
    
    if st.button("Submit Quiz"):
        st.write(f"Your Score: {score}/{len(quiz_questions)}")

# Journal & Reflections
elif page == "Journal & Reflections":
    st.header("📖 Your Personal Journal")
    entry = st.text_area("Write your thoughts and reflections:")
    
    if st.button("Save Journal Entry"):
        if entry.strip():
            data["journal"].append(entry)
            save_data(data)
            st.success("📝 Journal entry saved!")
        else:
            st.error("Please enter some text before saving.")
    
    st.subheader("📜 Previous Entries")
    for i, entry in enumerate(reversed(data["journal"])):
        st.write(f"**Entry {len(data['journal']) - i}:** {entry}")

# File Converter
elif page == "File Converter":
    st.header("📂 Convert CSV & Excel Files")
    uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file:
        file_extension = os.path.splitext(uploaded_file.name)[-1].lower()
        df = pd.read_csv(uploaded_file) if file_extension == ".csv" else pd.read_excel(uploaded_file)
        st.write(df.head())
        if st.button("Convert to CSV"):
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            st.download_button("Download CSV", buffer.getvalue(), file_name="converted.csv", mime="text/csv")

# Growth Tracker
elif page == "Growth Tracker":
    st.header("📊 Your Growth Progress")
    progress_areas = {
        "Handling Challenges": ["Avoids Challenges", "Attempts Sometimes", "Seeks Challenges"],
        "Receiving Feedback": ["Ignores Feedback", "Considers Feedback", "Implements Feedback"],
        "Skill Development": ["Sticks to Comfort Zone", "Explores Occasionally", "Consistently Grows"],
        "Resilience to Failure": ["Gives Up", "Tries Again", "Adapts and Improves"],
        "Learning from Others": ["Feels Intimidated", "Observes and Learns", "Collaborates & Grows"]
    }
    progress_tracker = {area: st.selectbox(area, options) for area, options in progress_areas.items()}
    st.table(progress_tracker)
    
    st.subheader("🌱 Personalized Growth Insights")
    st.info("Consistently track your progress and make small improvements each day!")

# About the Creator Section
st.sidebar.markdown("---")
st.sidebar.title("👩‍💻 Meet the Creator")
st.sidebar.write("**Nadia Shaikh**")
st.sidebar.write("A passionate web developer, cloud computing enthusiast, and programmer.")
st.sidebar.write("- 🌐 Expertise: Next.js, Python, UI/UX ")
st.sidebar.write("- 🎓 Student at GIAIC Top Performer")
st.sidebar.write("- 🛍️ Founder of an E-commerce project")
st.sidebar.write("- 💼 Works in collaboration with our project.")
st.sidebar.markdown("---")

   