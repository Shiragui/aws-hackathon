# main.py
import streamlit as st

st.set_page_config(page_title="Interview Prep AI", layout="wide")
st.title("Interview Prep AI")
st.markdown("""
Upload your resume and job description, and the AI will generate tailored interview questions with example answers.  
This demo shows a **ready-to-use example** for practice.
""")

# Dummy uploaded files
st.subheader("Uploaded Files")
st.write("**Resume:** Jane_Doe_Resume.pdf")
st.write("**Job Description:** Software_Engineer_JD.pdf")

st.info("Generating interview questions...")
st.success("Interview questions generated!")

# Organize dummy questions by category
questions = {
    "Technical": [
        {
            "question": "Explain the difference between a REST API and GraphQL.",
            "example_answer": "REST APIs use fixed endpoints and standard HTTP methods, while GraphQL allows clients to request exactly the data they need in a single query. GraphQL can reduce over-fetching and under-fetching of data."
        },
        {
            "question": "How would you optimize a slow SQL query?",
            "example_answer": "I would start by analyzing the query execution plan, adding appropriate indexes, rewriting joins if needed, and considering caching frequent queries."
        }
    ],
    "Behavioral": [
        {
            "question": "Tell me about a time you handled a difficult project.",
            "example_answer": "In my last role, I led a project with a tight deadline and unclear requirements. I broke down tasks, held daily syncs with the team, and delivered the project on time while maintaining quality."
        },
        {
            "question": "How do you handle tight deadlines?",
            "example_answer": "I prioritize tasks, communicate early if I need help, and break large tasks into smaller milestones to track progress effectively."
        }
    ],
    "Salary Negotiation": [
        {
            "question": "How would you negotiate salary if offered?",
            "example_answer": "I would express my excitement about the role and then reference industry standards and my experience: 'I'm thrilled about this opportunity. Based on my experience and market research, I was expecting a range closer to $95k-$105k. Is there flexibility in the offer?'"
        },
        {
            "question": "What factors do you consider when evaluating a compensation package?",
            "example_answer": "I look at base salary, bonus potential, equity, benefits, PTO, and opportunities for growth. I also consider alignment with my career goals."
        }
    ]
}

# Display questions in tabs
tabs = st.tabs(list(questions.keys()))

for tab, category in zip(tabs, questions.keys()):
    with tab:
        st.subheader(f"{category} Questions")
        for i, q in enumerate(questions[category], 1):
            with st.expander(f"Q{i}: {q['question']}"):
                st.write("**Example Answer:**")
                st.write(q['example_answer'])

st.info("Use these questions to practice your interview skills. Click on each question to see a suggested response!")
