import streamlit as st

st.set_page_config(page_title="ESG Score Calculator", page_icon="🌍", layout="centered")

st.title("🌿 ESG Score Calculator")
st.write("Answer the following questions to calculate your company's ESG score.")

# --- Environment ---
st.header("🌱 Environment")
env_questions = [
    "Does the company regularly measure and monitor its energy consumption and carbon emissions?",
    "Has the company set formal targets to reduce greenhouse gas (GHG) emissions?",
    "Does the company have a waste management or recycling program in place?"
]

# --- Social ---
st.header("🤝 Social")
social_questions = [
    "Does the company have a written policy on diversity, equity, and inclusion (DEI)?",
    "Are employees provided with regular training on workplace safety and anti-harassment?",
    "Does the company ensure fair wages and benefits for all employees, including contract or temporary staff?"
]

# --- Governance ---
st.header("🏛️ Governance")
gov_questions = [
    "Does the company have an effective whistleblower policy that protects employees who report misconduct?",
    "Are financial statements and audit reports made publicly available each year?",
    "Does the company disclose executive compensation and related-party transactions transparently?"
]

# Combine all questions
all_questions = env_questions + social_questions + gov_questions

# --- Collect responses ---
responses = []
for i, q in enumerate(all_questions, 1):
    response = st.radio(
        f"{i}. {q}",
        options=["Yes", "No"],
        index=None,
        key=f"q{i}",
        horizontal=True
    )
    if response == "Yes":
        responses.append(1)
    elif response == "No":
        responses.append(0)

# --- Calculate Score ---
if st.button("Calculate ESG Score"):
    if len(responses) < len(all_questions):
        st.warning("⚠️ Please answer all questions before calculating.")
    else:
        score = sum(responses) / len(responses) * 100

        # Determine ESG Grade
        if score > 90:
            grade = "A+"
        elif score > 80:
            grade = "A"
        elif score > 70:
            grade = "B+"
        elif score > 60:
            grade = "B"
        elif score > 50:
            grade = "C+"
        else:
            grade = "C"

        # --- Display results ---
        st.success(f"✅ **ESG Score:** {score:.2f}%")
        st.info(f"🏅 **ESG Grade:** {grade}")

        # Optional visualization
        st.progress(int(score))
        st.write("### Detailed Results")
        st.write(f"- Environment: {sum(responses[:3])}/3")
        st.write(f"- Social: {sum(responses[3:6])}/3")
        st.write(f"- Governance: {sum(responses[6:9])}/3")
