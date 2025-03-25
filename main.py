import streamlit as st
import re
import random
import string
from passlib.pwd import genword

COMMEN_PASSWORD = {"password", "123456", "password123", "qwerty", "admin", "letmein", "12345678", "abc123"}


def check_password_strength(password):
    
    score = 0
    feedback = []

    if password.lower() in COMMEN_PASSWORD:
        return 1, ["🚫 This password is too common! Choose something more unique."]
    
    

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟡 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟡 Add at least one number (0-9).")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("🟡 Include at least one special character (!@#$%^&*).")

    return score, feedback

def password_generator():
    return genword(length=12 , charset="ascii_72")

st.title("🔒 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    score , feedback = check_password_strength(password)
    print(score)

    strength_labels = {1: "⚠️ Weak", 2: "⚠️ Weak", 3: "🟠 Moderate", 4: "🟢 Strong", 5: "✅ Very Strong"}

    st.markdown(f"**Password Strength:** {strength_labels.get(score, '⚠️ Very Weak')}")
    st.progress(score / 5)

    if score < 5:
        print(score)
        st.warning("🔹 Suggestions to Improve:")

        for tip in feedback:
            st.write("-", tip)

    else:
        st.success("🎉 Your password is strong and secure!")


if st.button("Generated this password"):
    strong_password = password_generator()
    st.write(f"💡 Suggested Password : {strong_password}")