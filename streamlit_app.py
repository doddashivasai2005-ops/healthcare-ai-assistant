import streamlit as st

st.title("🏥 Healthcare AI Assistant")
st.write("Welcome!")
st.write("Enter your symptoms below.")

symptoms = st.text_input("What symptoms are you experiencing?")

if st.button("Analyze Symptoms"):

    if symptoms.strip() == "":
        st.warning("Please enter your symptoms.")

    else:
        symptoms = symptoms.lower()

        if "fever" in symptoms:
            st.info("Possible causes of fever can include infections or other conditions.")
            st.write("General information: Rest, stay hydrated, and monitor your temperature,take 12 sleep.")

        elif "cough" in symptoms:
            st.info("Cough can occur with several respiratory conditions.")
            st.write("General information: Stay hydrated and get adequate rest.")

        elif "headache" in symptoms:
            st.info("Headache can have many possible causes.")
            st.write("General information: Rest, drink enough water, and avoid excessive screen time.")

        elif "stomach pain" in symptoms:
            st.info("Stomach pain can have many possible causes.")
            st.write("General information: Stay hydrated and consider eating light foods.")

        else:
            st.warning("I don't have enough information about these symptoms.")
            st.write("Please consult a qualified medical professional for appropriate advice.")

st.divider()

st.caption("⚠️ Educational project only - This application does not provide a medical diagnosis.")
