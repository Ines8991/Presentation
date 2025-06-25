import streamlit as st
import base64

# Configuration de la page
st.set_page_config(page_title="Ines COCOSSOU – Portfolio", layout="wide")

# 🌞 Application du thème clair (fixe ici)
with open("light.css") as f:
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
# Section Compétences techniques
# ------------------------------
st.markdown("""
### 🛠️ Compétences techniques

- **Analyse de données** : Python (pandas, scikit-learn, tensorflow, keras), R, Excel (VBA), PowerBI
- **Modélisation** : Régression, classification, séries temporelles (ARIMA, LSTM), clustering
- **Développement Web** : Django, Laravel, HTML, CSS, JavaScript
- **Bases de données** : SQL, NoSQL
- **Outils** : Git, Jupyter, Google Colab, VS Code
""")

# ------------------------------
# Section Expériences professionnelles
# ------------------------------
st.markdown("""
### 💼 Expériences professionnelles

#### 📌 Analyste de données – Université d’Évry (06/2023 – 10/2023)
- Analyse statistique sur les parcours étudiants en situation de Redoublement Non Autorisé (RNA)
- Clustering des étudiants pour identifier les profils à risque
- Création d'une plateforme web pour visualisation des RNA

#### 📌 Analyste en modélisation mathématique – LAMME (05/2022 – 08/2022)
- Étude mathématique des impulsions électriques dans des réseaux neuronaux biologiques
- Simulation et visualisation sous Python des dynamiques neuronales
""")

# ------------------------------
# Section Projets
# ------------------------------
st.markdown("""
### 📊 Projets réalisés

- **📈 Prédiction des prix boursiers (ARIMA + LSTM)**  
  Collecte de données financières, entraînement de modèles, visualisation interactive

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
