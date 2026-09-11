import streamlit as st
import urllib.parse


def page_accueil():

    st.title("Chocolate Sales Dashboard")

    st.markdown("""
    ## Transformer les données de ventes en informations exploitables

    Ce projet est un dashboard BI développé avec Python, SQL et Streamlit
    autour d'un jeu de données de ventes de chocolat.

    L'objectif est de partir de données transactionnelles et de construire
    un outil permettant d'explorer la performance commerciale, les produits,
    les boutiques et les clients.
    """)

    st.subheader("Le projet en quelques chiffres")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Période", "2023 → 2024")

    with col2:
        st.metric("Transactions", "1 000 000")

    with col3:
        st.metric("Produits", "200")

    with col4:
        st.metric("Boutiques", "100")

    with col5:
        st.metric("Clients", "50 000")

    st.subheader("La démarche")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 1. Structurer la donnée

        Les données sont organisées dans une base SQLite relationnelle
        regroupant les ventes, produits, boutiques, clients et calendrier.

        ### 2. Exploiter la donnée

        Les données sont interrogées en SQL et transformées afin de
        produire les indicateurs nécessaires à l'analyse.
        """)

    with col2:
        st.markdown("""
        ### 3. Restituer l'information

        Les résultats sont présentés sous forme de KPI, tableaux et
        visualisations interactives.

        ### 4. Interroger les données avec l'IA

        Un assistant permet également de poser des questions en langage
        naturel et d'obtenir des analyses directement à partir des données.
        """)

    st.subheader("Explorer le dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Vue globale**  
        Chiffre d'affaires, coûts, marge, ventes et évolution.

        **Produits**  
        Catégories, marques, classements et performances.
        """)

    with col2:
        st.markdown("""
        **Boutiques**  
        Performance des points de vente et répartition géographique.

        **Clients**  
        Fidélisation, segmentation et principaux clients.
        """)

    st.subheader("Technologies")

    st.markdown(
        "Python · SQL / SQLite · Pandas · Streamlit · Matplotlib · OpenAI API"
    )

    st.divider()

    st.subheader("Une question ou envie d'échanger ?")

    email = st.text_input(
        "Votre adresse email (facultatif)",
        placeholder="vous@exemple.com"
    )

    message = st.text_area(
        "Votre message",
        placeholder="Votre message..."
    )

    if st.button("✉ Me contacter"):

        if not message.strip():
            st.warning("Veuillez saisir un message.")
        else:
            body = f"{message.strip()}"

            if email.strip():
                body += f"\n\n---\nEmail de contact : {email.strip()}"

            mailto = (
                "mailto:theo.lepere@gmail.com"
                "?subject="
                + urllib.parse.quote("Contact depuis le Chocolate Sales Dashboard")
                + "&body="
                + urllib.parse.quote(body)
            )

            st.markdown(
                f'<meta http-equiv="refresh" content="0; url={mailto}">',
                unsafe_allow_html=True
            )
