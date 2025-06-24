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
st.markdown("### 📬 Me contacter")

st.markdown("""
<form action="https://formsubmit.co/icocossou1998@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Votre nom" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
    <input type="email" name="email" placeholder="Votre email" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
    <textarea name="message" placeholder="Votre message" required style="width: 100%; padding: 10px; height: 150px; margin-bottom: 10px;"></textarea>
    <button type="submit" style="
        background-color: #1E88E5;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;">
        ✉️ Envoyer le message
    </button>
</form>
""", unsafe_allow_html=True)



# ----- FOOTER -----
st.markdown("---")
st.markdown("© 2025 Ines COCOSSOU | Par Streamlit")
