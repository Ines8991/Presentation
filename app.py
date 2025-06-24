import streamlit as st
import base64

# ------------------------------
# Configuration de la page
# ------------------------------
st.set_page_config(page_title="Ines COCOSSOU – Portfolio", layout="wide")

# ----- CSS MODE SOMBRE/CLAIR -----
with open("style.css") as f:
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
Je suis actuellement diplomée en Data Sciences option Assurance et Finance, avec un fort intérêt pour les projets mêlant **intelligence artificielle**, **modélisation prédictive** et **développement d'applications web**.
""")

# ------------------------------
# Section Projets
# ------------------------------
st.markdown("""
### 📊 Projets réalisés

- **Prédiction des prix boursiers avec ARIMA + LSTM** : Application Streamlit interactive avec visualisation Plotly et signaux de trading MACD.
- **Analyse exploratoire des loyers à Paris** : Étude des données avec nettoyage, visualisation et insights sur la dynamique locative.
- **Survie hospitalière** : Modélisation statistique de la survie des patients via courbes de Kaplan-Meier et analyse multivariée.
""")

# ------------------------------
# Section Télécharger le CV
# ------------------------------
with open("data/CV_INES_COCOSSOU.pdf", "rb") as f:
    st.download_button(
        label="📄 Télécharger mon CV",
        data=f,
        file_name="Ines_COCOSSOU_CV.pdf",
        mime="application/pdf"
    )


# ------------------------------
# Section Contact
# ------------------------------
st.markdown("""
### 📢 Me contacter
- **Email** : icocossou98@gmail.com  
- **LinkedIn** : [linkedin.com/in/ines-cocossou](https://www.linkedin.com/in/ines-cocossou)  
- **GitHub** : [github.com/Ines8991](https://github.com/Ines8991)
""")


with st.form(key="contact_form"):
    name = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit_button = st.form_submit_button("Envoyer")

    if submit_button:
        st.success("Merci ! Votre message a bien été envoyé.")

        st.markdown(f"""
        <form action="https://formsubmit.co/{icocossou98@gmail.com}" method="POST" hidden>
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="email" value="{email}">
            <input type="hidden" name="message" value="{message}">
        </form>
        """, unsafe_allow_html=True)


# ----- FOOTER -----
st.markdown("---")
st.markdown("© 2025 Ines COCOSSOU | Par Streamlit")
