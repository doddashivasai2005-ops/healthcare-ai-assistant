import streamlit as st

st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🏥"
)

st.title("🏥 Healthcare AI Assistant")
st.write("🤖 Welcome! This is an educational health-information project.")
st.write("📝 Enter your symptoms below.")

symptoms = st.text_input(
    "🔍 What symptoms are you experiencing?"
)

if st.button("🔬 Analyze Symptoms"):

    if symptoms.strip() == "":
        st.warning("⚠️ Please enter your symptoms.")

    else:
        symptoms = symptoms.lower()

        # 🌡️ FEVER
        if "fever" in symptoms:

            st.subheader("🌡️ Fever Information")

            temperature = st.number_input(
                "🌡️ Enter your temperature in °F:",
                min_value=90.0,
                max_value=110.0,
                value=98.6,
                step=0.1
            )

            st.write(f"🌡️ Your entered temperature: **{temperature}°F**")

            if temperature < 100.4:
                st.success("🟢 This reading is below the usual fever threshold.")
                st.write("💧 Stay hydrated and continue monitoring your temperature.")

            elif temperature < 102:
                st.warning("🟡 This is a fever-range temperature.")
                st.write("🛌 Get adequate rest.")
                st.write("💧 Drink plenty of fluids.")
                st.write("🌡️ Continue monitoring your temperature.")

            elif temperature < 104:
                st.error("🔴 This is a high fever.")
                st.write("💧 Maintain hydration.")
                st.write("🛌 Get adequate rest.")
                st.write("👨‍⚕️ Consider contacting a healthcare professional, especially if the fever persists or other concerning symptoms occur.")

            else:
                st.error("🚨 Very high temperature.")
                st.write("🏥 Seek urgent medical attention, particularly if there are severe or concerning symptoms.")

        # 🤧 COUGH
        elif "cough" in symptoms:

            st.subheader("🤧 Cough Information")

            st.info("🔎 Cough can occur with several respiratory conditions.")

            st.write("💧 Drink enough fluids.")
            st.write("🛌 Get adequate rest.")
            st.write("🚭 Avoid smoke and other respiratory irritants.")
            st.write("👨‍⚕️ Seek medical advice if the cough is severe, persistent, or associated with breathing difficulty.")

        # 🤕 HEADACHE
        elif "headache" in symptoms:

            st.subheader("🤕 Headache Information")

            st.info("🔎 Headaches can have many possible causes.")

            st.write("💧 Drink enough water.")
            st.write("🛌 Get adequate rest.")
            st.write("📱 Reduce excessive screen exposure.")
            st.write("🍽️ Avoid skipping meals.")
            st.write("👨‍⚕️ Seek medical attention for a sudden, severe, or unusual headache.")

        # 🤢 VOMITING
        elif "vomiting" in symptoms:

            st.subheader("🤢 Vomiting Information")

            st.info("🔎 Vomiting can have several possible causes.")

            st.write("💧 Take small, frequent amounts of fluids.")
            st.write("🛌 Rest.")
            st.write("🍚 When able to eat, choose light foods.")
            st.write("⚠️ Watch for signs of dehydration.")

        # 💩 DIARRHEA
        elif "diarrhea" in symptoms:

            st.subheader("💩 Diarrhea Information")

            st.info("🔎 Diarrhea can have several possible causes.")

            st.write("💧 Drink plenty of fluids.")
            st.write("🧂 Oral rehydration solutions can help replace lost fluids and electrolytes.")
            st.write("🛌 Get adequate rest.")
            st.write("⚠️ Seek medical advice if symptoms are severe, persistent, or accompanied by blood or significant dehydration.")

        # 🤧 COLD
        elif "cold" in symptoms or "runny nose" in symptoms:

            st.subheader("🤧 Cold Information")

            st.info("🔎 A cold or runny nose can occur with several respiratory infections.")

            st.write("💧 Drink fluids.")
            st.write("🛌 Get enough rest.")
            st.write("🧼 Wash your hands regularly.")
            st.write("😷 Consider avoiding close contact with others if you have an infectious illness.")

        # 😣 SORE THROAT
        elif "sore throat" in symptoms or "throat pain" in symptoms:

            st.subheader("😣 Sore Throat Information")

            st.info("🔎 Sore throat can have several possible causes.")

            st.write("🥤 Drink warm or comfortable-temperature fluids.")
            st.write("🛌 Get adequate rest.")
            st.write("💧 Stay hydrated.")
            st.write("👨‍⚕️ Seek medical advice if symptoms are severe or persistent.")

        # 😵 DIZZINESS
        elif "dizziness" in symptoms:

            st.subheader("😵 Dizziness Information")

            st.info("🔎 Dizziness can have many possible causes.")

            st.write("🪑 Sit or lie down somewhere safe.")
            st.write("💧 Drink enough fluids.")
            st.write("🚶 Stand up slowly.")
            st.write("⚠️ If dizziness is severe, sudden, or associated with other concerning symptoms, seek medical attention.")

        # 😴 FATIGUE
        elif "fatigue" in symptoms or "tiredness" in symptoms:

            st.subheader("😴 Fatigue Information")

            st.info("🔎 Tiredness can have many possible causes.")

            st.write("🛌 Maintain a regular sleep schedule.")
            st.write("🥗 Eat balanced meals.")
            st.write("💧 Stay hydrated.")
            st.write("🏃 Include appropriate physical activity.")
            st.write("👨‍⚕️ Seek medical advice if unexplained fatigue continues.")

        # 🦴 JOINT PAIN
        elif "joint pain" in symptoms:

            st.subheader("🦴 Joint Pain Information")

            st.info("🔎 Joint pain can have several possible causes.")

            st.write("🛌 Rest the affected area.")
            st.write("🚫 Avoid activities that significantly increase pain.")
            st.write("💧 Stay hydrated.")
            st.write("👨‍⚕️ Consider medical evaluation if pain is severe, persistent, or associated with swelling or fever.")

        # 💪 MUSCLE PAIN
        elif "muscle pain" in symptoms:

            st.subheader("💪 Muscle Pain Information")

            st.info("🔎 Muscle pain can have several possible causes.")

            st.write("🛌 Get adequate rest.")
            st.write("💧 Stay hydrated.")
            st.write("🏃 Avoid strenuous activity until you feel better.")

        # 🩹 RASH
        elif "rash" in symptoms:

            st.subheader("🩹 Rash Information")

            st.info("🔎 Skin rashes can have many possible causes.")

            st.write("🧴 Avoid known skin irritants.")
            st.write("🚫 Try not to scratch the affected area.")
            st.write("🧼 Keep the skin clean.")
            st.write("👨‍⚕️ Seek medical advice if the rash is rapidly spreading, severe, or accompanied by other concerning symptoms.")

        # 🦷 TOOTHACHE
        elif "toothache" in symptoms or "tooth pain" in symptoms:

            st.subheader("🦷 Toothache Information")

            st.info("🔎 Tooth pain can have several possible causes.")

            st.write("🪥 Maintain good oral hygiene.")
            st.write("🍬 Limit sugary foods.")
            st.write("🦷 Consider seeing a dentist for persistent tooth pain.")

        # 🚽 CONSTIPATION
        elif "constipation" in symptoms:

            st.subheader("🚽 Constipation Information")

            st.info("🔎 Constipation can have several possible causes.")

            st.write("💧 Drink enough water.")
            st.write("🥦 Include fiber-rich foods in your diet.")
            st.write("🚶 Stay physically active when appropriate.")

        # 🤧 SNEEZING
        elif "sneezing" in symptoms:

            st.subheader("🤧 Sneezing Information")

            st.info("🔎 Sneezing can occur because of allergies, infections, or irritants.")

            st.write("🧼 Maintain good hygiene.")
            st.write("🌳 Avoid known triggers when possible.")
            st.write("💧 Stay hydrated.")

        # ❤️ CHEST PAIN
        elif "chest pain" in symptoms:

            st.subheader("❤️ Chest Pain Information")

            st.error("🚨 Chest pain can sometimes be a medical emergency.")

            st.write("🏥 Seek urgent medical attention, especially if chest pain is severe, sudden, or occurs with:")
            st.write("😮‍💨 Difficulty breathing")
            st.write("😵 Fainting or severe dizziness")
            st.write("💦 Heavy sweating")
            st.write("🤢 Nausea")
            st.write("💪 Pain spreading to the arm, shoulder, back, neck, or jaw")

        # 😮‍💨 BREATHING DIFFICULTY
        elif "shortness of breath" in symptoms or "breathing difficulty" in symptoms:

            st.subheader("😮‍💨 Breathing Difficulty")

            st.error("🚨 Breathing difficulty can sometimes require urgent medical attention.")

            st.write("🪑 Sit upright and remain calm.")
            st.write("🏥 Seek immediate medical help if breathing difficulty is severe, sudden, or worsening.")

        # ❓ UNKNOWN
        else:

            st.warning("⚠️ I don't have enough information about these symptoms.")

            st.write("🔎 Try entering symptoms such as:")
            st.write("🌡️ Fever")
            st.write("🤧 Cough")
            st.write("🤕 Headache")
            st.write("🤢 Vomiting")
            st.write("💩 Diarrhea")
            st.write("😵 Dizziness")
            st.write("😴 Fatigue")
            st.write("🦴 Joint pain")

            st.write("👨‍⚕️ For appropriate medical advice, consult a qualified healthcare professional.")

st.divider()

st.caption(
    "⚠️ Educational project only — This application does not provide a medical diagnosis."
)
