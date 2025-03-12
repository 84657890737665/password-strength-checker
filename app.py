# Imports 
import streamlit as st 
import re 



# Develop the Application 

st.set_page_config(page_title="Password Strength Checker" , page_icon=" 🔒 ")
st.title("🔐 Password Strength Checker") 


password = st.text_input("Enter Your Password Here..." , type="password")
feedback  = []
score = 0 

# Create Conditions 

if password:
    if len(password) >= 8:
        score += 1 
    else: 
        feedback.append(" ❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]' , password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain both Upper and Lower Cases. ")

    if re.search(r'[0-9]' , password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain at least one digit.")

    if re.search(r'[$#*-_&%!]' , password):
        score += 1 
    else: 
        feedback.append(" ❌ Password should contain a special character like($#*-_&%!).") 

    if score == 4:
        feedback.append(" ✅ Your Password is Strong! ")    
                    
    elif score == 3:
        feedback.append(" 🟡 Your Password is Moderately Strong! ")
    else:
        feedback.append(" ❌ Your Password is Weak! Try stronger Password.  ")

    if feedback:
                st.markdown("## Improvement Suggestions")
                for tip in feedback:
                    st.write(tip)
else: 
    st.info(" Plese Enter your Password to get started! ")                 
