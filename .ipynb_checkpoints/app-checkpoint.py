import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Ines COCOSSOU - Profil", layout="wide")
st.title("👩‍💻 Ines COCOSSOU")
st.subheader("Data Analyst - Finance, Assurance et Santé")

# --- Informations de contact
col1, col2 = st.columns(2)
with col1:
    st.write("📧 Email : icocossou1998@gmail.com")
    st.write("📞 Téléphone : +33 07 78 13 68 93")
with col2:
    st.write("📍 Localisation : France")
    st.write("🌐 GitHub : [Ines8991](https://github.com/Ines8991)")

st.markdown("---")

# --- Expériences professionnelles
st.header("💼 Expériences professionnelles")
st.markdown("""
**🔹 Analyste de données (stagiaire)**  
Université d’Évry – Direction de la Donnée, de l’Analyse et du Conseil (06/2023 – 10/2023)  
- Analyse multivariée sur les cas de redoublement non autorisé (RNA)  
- Clustering, prédiction avec modèles supervisés  
- Déploiement d'une app de visualisation et recommandation

**🔹 Analyste en modélisation mathématique (stagiaire)**  
Laboratoire de Mathématiques et de Modélisation d’Évry (05/2022 – 08/2022)  
- Étude des impulsions dans les réseaux neuronaux  
- Simulations et modélisation en Python
""")

st.markdown("---")

# --- Projets
st.header("📊 Projets personnels")
st.markdown("""
**📈 Prévision boursière avec ARIMA + LSTM**  
- Modèles de séries temporelles sur des données Yahoo Finance  
- Modélisation, prédiction et visualisation interactive  
- Interface Streamlit déployée

👉 [Voir sur GitHub](https://github.com/Ines8991/Prevision_Arima_Lstm)
""")

st.markdown("---")

# --- Compétences
st.header("🧰 Compétences techniques")
st.markdown("""
- **Python** : pandas, scikit-learn, TensorFlow, Keras, PyTorch  
- **R**, **Power BI**, **Excel**, **Tableau**  
- **SQL**, NoSQL, **Git**  
- **Web** : Django, Laravel, HTML/CSS
""")

# --- Langues et qualités
st.header("🌐 Langues & qualités")
st.markdown("""
- 🇫🇷 Français : langue maternelle  
- 🇬🇧 Anglais : niveau intermédiaire  
- 💡 Autonomie, curiosité, rigueur, esprit d'analyse
""")

# --- Footer
st.markdown("---")
st.markdown("© 2025 Ines COCOSSOU | CV interactif Streamlit")
