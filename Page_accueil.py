import streamlit as st
import urllib.parse


def page_accueil():

    st.title("Chocolate Sales Dashboard")

    st.subheader("Explorer la performance commerciale par la donnée.")

    st.write(
        "Ce projet transforme un volume important de données de ventes en "
        "indicateurs simples à explorer. L'objectif est de mettre en évidence "
        "les performances commerciales des produits, boutiques et clients."
    )

    st.divider()

    # ---------------------------------------------------------
    # LE PROJET
    # ---------------------------------------------------------

    st.header("Le projet")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Pourquoi ?")

        st.write(
            "Le projet part d'un jeu de données de ventes et reproduit une "
            "problématique proche d'un besoin d'analyse métier : fiabiliser "
            "les données, construire des indicateurs et permettre leur "
            "exploration."
        )

    with col2:
        st.subheader("Comment ?")

        st.write(
            "Les données sont stockées dans une base SQLite puis exploitées "
            "avec Python et Streamlit. Les différentes pages permettent "
            "d'aborder les données selon plusieurs angles."
        )

    st.divider()

    # ---------------------------------------------------------
    # DONNÉES
    # ---------------------------------------------------------

    st.header("Les données")

    st.write(
        "Les données couvrent deux années complètes, du 1er janvier 2023 "
        "au 31 décembre 2024."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Transactions", "1 000 000")

    with col2:
        st.metric("Produits", "200")

    with col3:
        st.metric("Boutiques", "100")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Clients", "50 000")

    with col2:
        st.metric("Période", "2023 → 2024")

    st.divider()

    # ---------------------------------------------------------
    # STRUCTURE
    # ---------------------------------------------------------

    st.header("Structure des données")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader("SALES")
        st.caption(
            "Transactions, quantités, prix, remises, chiffre d'affaires, "
            "coûts et profits."
        )

    with col2:
        st.subheader("PRODUCTS")
        st.caption(
            "Produits, marques, catégories, poids et pourcentage de cacao."
        )

    with col3:
        st.subheader("STORES")
        st.caption(
            "Boutiques, villes, pays et types de magasins."
        )

    with col4:
        st.subheader("CUSTOMERS")
        st.caption(
            "Clients, âge, genre, fidélité et date d'inscription."
        )

    with col5:
        st.subheader("CALENDAR")
        st.caption(
            "Dates, années, mois et semaines pour les analyses temporelles."
        )

    st.divider()

    # ---------------------------------------------------------
    # EXPLORATION
    # ---------------------------------------------------------

    st.header("Explorer les données")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Performance globale")

        st.write(
            "Suivre le chiffre d'affaires, les coûts, le profit, les volumes "
            "vendus et leur évolution dans le temps."
        )

        st.subheader("Produits")

        st.write(
            "Comparer les produits, marques et catégories selon leur chiffre "
            "d'affaires, leur profit ou leurs volumes de ventes."
        )

    with col2:

        st.subheader("Boutiques")

        st.write(
            "Comparer les boutiques et analyser leur performance selon leur "
            "localisation et leur chiffre d'affaires."
        )

        st.subheader("Clients")

        st.write(
            "Explorer la clientèle, la fidélité, la segmentation et la "
            "contribution des principaux clients."
        )

    st.divider()

    # ---------------------------------------------------------
    # ASSISTANT IA
    # ---------------------------------------------------------

    st.header("Assistant IA")

    st.write(
        "L'application intègre également un assistant permettant de poser "
        "des questions sur les données en langage naturel."
    )

    st.write(
        "L'objectif est de pouvoir interroger rapidement la base sans avoir "
        "à connaître sa structure ou écrire directement les requêtes."
    )

    st.divider()

    # ---------------------------------------------------------
    # CONTACT
    # ---------------------------------------------------------

    st.header("Contact")

    st.write(
        "Une question ou une remarque sur le projet ? "
        "Vous pouvez préparer un email directement depuis cette page."
    )

    email = st.text_input(
        "Votre email (facultatif)",
        placeholder="votre@email.com"
    )

    message = st.text_area(
        "Message",
        placeholder="Votre message..."
    )

    if st.button("Préparer l'email"):

        if email:
            body = (
                f"Email du visiteur : {email}\n\n"
                f"{message}"
            )
        else:
            body = message

        mailto = (
            "mailto:theo.lepere@gmail.com"
            "?subject="
            + urllib.parse.quote("Contact - Chocolate Sales Dashboard")
            + "&body="
            + urllib.parse.quote(body)
        )

        st.link_button(
            "Ouvrir mon client email",
            mailto
        )
