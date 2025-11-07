# main.py
import streamlit as st

st.set_page_config(page_title="OfferSense", layout="wide")
st.title("OfferSense")

st.markdown("""
### Problem  
Many people walk into job interviews without considering **negotiation** — unsure what’s fair, what’s flexible, or what they should advocate for.  

### Solution  
**OfferSense** helps users walk into HR or recruiter interviews with confidence.  
By analyzing your **resume** and a **job description**, it provides AI-based recommendations on what to negotiate, grounded in **industry standards** and **role expectations**.
""")

st.divider()
st.subheader("Upload Your Documents")

st.write("Upload your **resume** and the **job description** for the role you’re applying to. OfferSense will analyze both to give you tailored negotiation insights.")

# Dummy file display (pretend files were uploaded)
st.write("**Resume:** Jane_Doe_Resume.pdf")
st.write("**Job Description:** Software_Engineer_JD.pdf")

st.info("Analyzing role and compensation data...")
st.success("Recommendations generated successfully!")

st.divider()
st.header("OfferSense Insights")

# Dummy analysis output (pretend it came from Bedrock or another AI model)
col1, col2 = st.columns(2)
with col1:
    st.metric("Estimated Market Range", "$92,000 – $108,000")
    st.metric("Industry Benchmark Level", "Mid-Level Engineer")
with col2:
    st.metric("Negotiation Flexibility", "High")
    st.metric("Equity Offering Typical Range", "0.03% – 0.10%")

st.markdown("""
#### Suggested Negotiation Topics
Based on the job description and your background, these areas are likely negotiable:
- **Base Salary:** The offer may be 5–10% below market median for your experience level. Consider referencing benchmark data.
- **Signing Bonus:** Many similar roles include $5k–$10k signing bonuses — worth asking about if not included.
- **Equity:** If the company is early-stage or growth-phase, equity value may be negotiable.
- **Remote Flexibility / Hybrid Schedule:** Increasingly common in tech firms — ask about 2–3 remote days per week.
- **Professional Development Budget:** Often $1k–$3k per year for courses, certifications, or conferences.
""")

st.divider()
st.header("Sample Interview Dialogue")

st.markdown("""
**HR:** “Our offer is for $95,000 with standard benefits.”  

**You:** “Thank you — I’m really excited about this role. Based on my research and experience, I was expecting a range closer to $100k–$105k.  
Is there flexibility there?”  

**HR:** “Let me check with the hiring manager.”  

**You:** “Great — I appreciate that. Also, could we discuss professional development resources or signing bonuses?”
""")


st.divider()
st.header("Summary Recommendations")

st.markdown("""
✅ **Negotiate:** Base salary, signing bonus, equity  
⚖️ **Review:** PTO and relocation terms  
🟢 **Strong Fit:** Technical skills align closely with job description  
🔵 **Overall Readiness Score:** 9.1 / 10
""")

st.info("OfferSense helps you enter interviews with clarity, data, and confidence.")
