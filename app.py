import streamlit as st
import base64

# Configuration de la page
# ------------------------------
st.set_page_config(page_title="Ines COCOSSOU – Portfolio", layout="wide")
# 🎨 Thème clair / sombre
with open("dark.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# ------------------------------
# En-tête
# ------------------------------
st.title("👩‍💻 Ines COCOSSOU")
st.subheader("Analyste de Données | Passionnée par la Data & le Développement Web")

# ------------------------------
# Section À propos
# ------------------------------
st.markdown("""
### ✨ À propos de moi
Je suis diplômée en Data Sciences, spécialité Assurance & Finance. Je suis passionnée par les projets mêlant **intelligence artificielle**, **modélisation prédictive**, et **développement web**.
""")

# ------------------------------
# Section Projets
# ------------------------------
st.markdown("""
### 📊 Projets réalisés

- **📈 Prédiction des prix boursiers (ARIMA + LSTM)**  
  Application Streamlit avec visualisation Plotly + signaux MACD
- **🏠 Analyse exploratoire des loyers à Paris**  
  Étude statistique sur la dynamique locative
- **🩺 Analyse de survie hospitalière**  
  Courbes Kaplan-Meier & analyse multivariée
""")

# ------------------------------
# Section Télécharger le CV
# ------------------------------
st.markdown("### 📄 Télécharger mon CV")
with open("data/CV_INES_COCOSSOU.pdf", "rb") as f:
    st.download_button(
        label="📥 Télécharger le CV",
        data=f,
        file_name="Ines_COCOSSOU_CV.pdf",
        mime="application/pdf"
    )

# ------------------------------
# Section Contact
# ------------------------------
st.markdown("""
### 📢 Me contacter
- 📧 Email : icocossou1998@gmail.com  
- 💼 LinkedIn : [linkedin.com/in/ines-cocossou](https://www.linkedin.com/in/ines-cocossou)  
- 💻 GitHub : [github.com/Ines8991](https://github.com/Ines8991)
""")

with st.form(key="contact_form"):
    name = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit_button = st.form_submit_button("📨 Envoyer")

    if submit_button:
        st.success("✅ Merci ! Votre message a bien été pris en compte.")
        # Cette ligne ci-dessous ne permet pas l’envoi automatique réel sans JS ou backend
        st.info("ℹ️ Pour l’envoi réel, pensez à activer le formulaire via FormSubmit.")
        st.markdown(f"""
            <form action="https://formsubmit.co/icocossou1998@gmail.com" method="POST" hidden>
                <input type="hidden" name="name" value="{name}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="message" value="{message}">
            </form>
        """, unsafe_allow_html=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("© 2025 Ines COCOSSOU | Développé avec ❤️ via Streamlit")
