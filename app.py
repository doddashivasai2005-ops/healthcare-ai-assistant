import streamlit as st

# Title
st.title("🏥 Healthcare AI Assistant")

st.write("Welcome!")
st.write("Enter your symptoms below.")

# Get symptoms from user
symptoms = st.text_input("What symptoms are you experiencing?")

# Analyze button
if st.button("Analyze Symptoms"):

    if symptoms.strip() == "":
        st.warning("Please enter your symptoms.")

    else:
        symptoms = symptoms.lower()

        # Fever
        if "fever" in symptoms:
            st.info("Possible causes of fever can include infections or other conditions.")
            st.write(
                "General information: Rest, stay hydrated, and monitor your temperature."
            )

        # Cough
        elif "cough" in symptoms:
            st.info("Cough can occur with several respiratory conditions.")
            st.write(
                "General information: Stay hydrated and get adequate rest."
            )

        # Headache
        elif "headache" in symptoms:
            st.info("Headache can have many possible causes.")
            st.write(
                "General information: Rest, drink enough water, and avoid excessive screen time."
            )

        # Stomach pain
        elif "stomach pain" in symptoms:
            st.info("Stomach pain can have many possible causes.")
            st.write(
                "General information: Stay hydrated and consider eating light foods."
            )

        # Unknown symptoms
        else:
            st.warning(
                "I don't have enough information about these symptoms."
            )
            st.write(
                "Please consult a qualified medical professional for appropriate advice."
            )

# Disclaimer
st.divider()

st.caption(
    "⚠️ Educational project only - This application does not provide a medical diagnosis."
)
