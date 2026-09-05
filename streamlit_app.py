import streamlit as st

# Page settings
st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🏥"
)

# Title
st.title("🏥 Healthcare AI Assistant")

st.write("👋 Welcome!")
st.write("📝 Enter your symptoms below to get general health information.")

# User input
symptoms = st.text_input(
    "🔍 What symptoms are you experiencing?"
)

# Analyze button
if st.button("🔬 Analyze Symptoms"):

    if symptoms.strip() == "":
        st.warning("⚠️ Please enter your symptoms.")

    else:
        symptoms = symptoms.lower()

        # 🌡️ FEVER
        if "fever" in symptoms:

            st.subheader("🌡️ Fever Information")

            st.info(
                "🌡️ First, check your body temperature using a thermometer."
            )

            st.write(
                "📊 A temperature of **100.4°F (38°C) or higher** "
                "is generally considered a fever."
            )

            st.write("💧 Drink plenty of fluids.")
            st.write("🛌 Get adequate rest.")
            st.write("🌡️ Continue monitoring your temperature.")
            st.write("🍲 Eat light, nutritious foods if you feel able to eat.")

            st.warning(
                "⚠️ If the fever is very high, persistent, worsening, "
                "or accompanied by serious symptoms, seek medical attention."
            )

        # 🤧 COUGH
        elif "cough" in symptoms:

            st.subheader("🤧 Cough Information")

            st.info(
                "🔎 Cough can occur with several respiratory conditions."
            )

            st.write("💧 Stay hydrated.")
            st.write("🛌 Get adequate rest.")
            st.write("🚭 Avoid smoke and other respiratory irritants.")

            st.warning(
                "⚠️ Seek medical advice if the cough is severe, "
                "persistent, or associated with breathing difficulty."
            )

        # 🤕 HEADACHE
        elif "headache" in symptoms:

            st.subheader("🤕 Headache Information")

            st.info(
                "🔎 Headache can have many possible causes."
            )

            st.write("💧 Drink enough water.")
            st.write("🛌 Get adequate rest.")
            st.write("📱 Avoid excessive screen time.")
            st.write("🍽️ Avoid skipping meals.")

            st.warning(
                "⚠️ Seek medical attention for a sudden, severe, "
                "or unusual headache."
            )

        # 🤢 VOMITING
        elif "vomiting" in symptoms:

            st.subheader("🤢 Vomiting Information")

            st.info(
                "🔎 Vomiting can have several possible causes."
            )

            st.write("💧 Take small amounts of fluids frequently.")
            st.write("🛌 Get adequate rest.")
            st.write("🍚 Eat light foods when you feel able.")

            st.warning(
                "⚠️ Watch for signs of dehydration and seek medical advice "
                "if vomiting is severe or persistent."
            )

        # 💩 DIARRHEA
        elif "diarrhea" in symptoms:

            st.subheader("💩 Diarrhea Information")

            st.info(
                "🔎 Diarrhea can have several possible causes."
            )

            st.write("💧 Drink plenty of fluids.")
            st.write("🧂 Oral rehydration solutions can help replace fluids and electrolytes.")
            st.write("🛌 Get adequate rest.")

            st.warning(
                "⚠️ Seek medical advice if diarrhea is severe, persistent, "
                "or accompanied by blood or significant dehydration."
            )

        # 🤧 COLD
        elif "cold" in symptoms or "runny nose" in symptoms:

            st.subheader("🤧 Cold Information")

            st.info(
                "🔎 A cold or runny nose can occur with several respiratory infections."
            )

            st.write("💧 Drink plenty of fluids.")
            st.write("🛌 Get enough rest.")
            st.write("🧼 Wash your hands regularly.")
            st.write("😷 Avoid close contact with others if you are unwell.")

        # 😣 SORE THROAT
        elif "sore throat" in symptoms or "throat pain" in symptoms:

            st.subheader("😣 Sore Throat Information")

            st.info(
                "🔎 Sore throat can have several possible causes."
            )

            st.write("🥤 Drink comfortable-temperature fluids.")
            st.write("💧 Stay hydrated.")
            st.write("🛌 Get adequate rest.")

            st.warning(
                "⚠️ Seek medical advice if symptoms are severe or persistent."
            )

        # 😵 DIZZINESS
        elif "dizziness" in symptoms:

            st.subheader("😵 Dizziness Information")

            st.info(
                "🔎 Dizziness can have many possible causes."
            )

            st.write("🪑 Sit or lie down somewhere safe.")
            st.write("💧 Drink enough fluids.")
            st.write("🚶 Stand up slowly.")

            st.warning(
                "⚠️ If dizziness is severe, sudden, or associated with "
                "other concerning symptoms, seek medical attention."
            )

        # 😴 FATIGUE
        elif "fatigue" in symptoms or "tiredness" in symptoms:

            st.subheader("😴 Fatigue Information")

            st.info(
                "🔎 Tiredness can have many possible causes."
            )

            st.write("🛌 Maintain a regular sleep schedule.")
            st.write("🥗 Eat balanced meals.")
            st.write("💧 Stay hydrated.")
            st.write("🏃 Stay physically active when appropriate.")

            st.warning(
                "⚠️ Seek medical advice if unexplained fatigue continues."
            )

        # 🦴 JOINT PAIN
        elif "joint pain" in symptoms:

            st.subheader("🦴 Joint Pain Information")

            st.info(
                "🔎 Joint pain can have several possible causes."
            )

            st.write("🛌 Rest the affected area.")
            st.write("🚫 Avoid activities that increase the pain.")
            st.write("💧 Stay hydrated.")

            st.warning(
                "⚠️ Consider medical evaluation if pain is severe, "
                "persistent, or associated with swelling or fever."
            )

        # 💪 MUSCLE PAIN
        elif "muscle pain" in symptoms:

            st.subheader("💪 Muscle Pain Information")

            st.info(
                "🔎 Muscle pain can have several possible causes."
            )

            st.write("🛌 Get adequate rest.")
            st.write("💧 Stay hydrated.")
            st.write("🏃 Avoid strenuous activity until you feel better.")

        # 🩹 RASH
        elif "rash" in symptoms:

            st.subheader("🩹 Rash Information")

            st.info(
                "🔎 Skin rashes can have many possible causes."
            )

            st.write("🧴 Avoid known skin irritants.")
            st.write("🚫 Try not to scratch the affected area.")
            st.write("🧼 Keep the skin clean.")

            st.warning(
                "⚠️ Seek medical advice if the rash is rapidly spreading, "
                "severe, or accompanied by other concerning symptoms."
            )

        # 👁️ EYE PAIN
        elif "eye pain" in symptoms:

            st.subheader("👁️ Eye Pain Information")

            st.info(
                "🔎 Eye pain can have several possible causes."
            )

            st.write("👁️ Give your eyes adequate rest.")
            st.write("📱 Reduce excessive screen exposure.")
            st.write("🚫 Avoid rubbing your eyes.")

            st.warning(
                "⚠️ Seek medical advice for severe eye pain or vision changes."
            )

        # 👂 EAR PAIN
        elif "ear pain" in symptoms:

            st.subheader("👂 Ear Pain Information")

            st.info(
                "🔎 Ear pain can have several possible causes."
            )

            st.write("🛌 Get adequate rest.")
            st.write("🚫 Do not put objects inside the ear.")

            st.warning(
                "⚠️ Consider seeing a healthcare professional "
                "if the pain persists or is severe."
            )

        # 🦷 TOOTHACHE
        elif "toothache" in symptoms or "tooth pain" in symptoms:

            st.subheader("🦷 Toothache Information")

            st.info(
                "🔎 Tooth pain can have several possible causes."
            )

            st.write("🪥 Maintain good oral hygiene.")
            st.write("🍬 Limit sugary foods.")
            st.write("💧 Drink enough water.")

            st.warning(
                "⚠️ Persistent tooth pain should be evaluated by a dentist."
            )

        # 🚽 CONSTIPATION
        elif "constipation" in symptoms:

            st.subheader("🚽 Constipation Information")

            st.info(
                "🔎 Constipation can have several possible causes."
            )

            st.write("💧 Drink enough water.")
            st.write("🥦 Include fiber-rich foods in your diet.")
            st.write("🚶 Stay physically active when appropriate.")

        # 🤧 SNEEZING
        elif "sneezing" in symptoms:

            st.subheader("🤧 Sneezing Information")

            st.info(
                "🔎 Sneezing can occur because of allergies, infections, or irritants."
            )

            st.write("🧼 Maintain good hygiene.")
            st.write("🌳 Avoid known triggers when possible.")
            st.write("💧 Stay hydrated.")

        # ❤️ CHEST PAIN
        elif "chest pain" in symptoms:

            st.subheader("❤️ Chest Pain Information")

            st.error(
                "🚨 Chest pain can sometimes be a medical emergency."
            )

            st.write("🏥 Seek urgent medical attention, especially if chest pain is:")
            st.write("😮‍💨 Associated with difficulty breathing")
            st.write("😵 Associated with fainting or severe dizziness")
            st.write("💦 Associated with heavy sweating")
            st.write("🤢 Associated with nausea")
            st.write("💪 Spreading to the arm, shoulder, back, neck, or jaw")

        # 😮‍💨 BREATHING DIFFICULTY
        elif (
            "shortness of breath" in symptoms
            or "breathing difficulty" in symptoms
        ):

            st.subheader("😮‍💨 Breathing Difficulty")

            st.error(
                "🚨 Breathing difficulty can sometimes require urgent medical attention."
            )

            st.write("🪑 Sit upright and remain calm.")

            st.warning(
                "🏥 Seek immediate medical help if breathing difficulty "
                "is severe, sudden, or worsening."
            )

        # 🍽️ LOSS OF APPETITE
        elif "loss of appetite" in symptoms:

            st.subheader("🍽️ Loss of Appetite Information")

            st.info(
                "🔎 Loss of appetite can have many possible causes."
            )

            st.write("🍲 Try small, balanced meals.")
            st.write("💧 Stay hydrated.")
            st.write("🛌 Get adequate rest.")

            st.warning(
                "⚠️ Seek medical advice if loss of appetite continues."
            )

        # ❓ UNKNOWN SYMPTOM
        else:

            st.warning(
                "⚠️ I don't have enough information about these symptoms."
            )

            st.write("🔎 Try entering symptoms such as:")

            st.write("🌡️ Fever")
            st.write("🤧 Cough")
            st.write("🤕 Headache")
            st.write("🤢 Vomiting")
            st.write("💩 Diarrhea")
            st.write("😵 Dizziness")
            st.write("😴 Fatigue")
            st.write("🦴 Joint pain")
            st.write("🩹 Rash")

            st.write(
                "👨‍⚕️ For appropriate medical advice, "
                "consult a qualified healthcare professional."
            )

# Divider
st.divider()

# Disclaimer
st.caption(
    "⚠️ Educational project only — This application does not provide "
    "a medical diagnosis."
)
