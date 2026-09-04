import streamlit as st

st.title("🏥 Healthcare AI Assistant")
st.write("Enter your symptoms below.")

symptoms = st.text_input("What symptoms are you experiencing?")

if st.button("Analyze Symptoms"):
    if symptoms:
        symptoms = symptoms.lower()

        if "fever" in symptoms:
            st.info("Possible fever-related illness.")
            st.write("General advice: Rest, stay hydrated, and monitor your temperature.")

        elif "cough" in symptoms:
            st.info("Possible respiratory illness.")
            st.write("General advice: Stay hydrated and get adequate rest.")

        elif "headache" in symptoms:
            st.info("Possible common headache.")
            st.write("General advice: Rest and drink enough water.")

        elif "stomach pain" in symptoms:
            st.info("Possible digestive problem.")
            st.write("General advice: Drink water and eat light food.")

        else:
            st.warning("I don't have enough information about these symptoms.")
            st.write("Please consult a qualified medical professional.")
    else:
        st.warning("Please enter your symptoms.")

st.caption("⚠️ Educational project 
only - not a medical diagnosis.")
