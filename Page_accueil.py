import streamlit as st
import urllib.parse


def page_accueil():

    # ============================================================
    # HERO
    # ============================================================

    st.markdown(
        """
        <div style="
            padding: 70px 0 55px 0;
            max-width: 900px;
        ">
            <div style="
                color: #66F2FF;
                font-size: 0.85rem;
                font-weight: 600;
                letter-spacing: 2px;
                margin-bottom: 18px;
            ">
                CHOCOLATE SALES
            </div>

            <h1 style="
                font-size: 3.2rem;
                line-height: 1.1;
                margin-bottom: 25px;
                color: #FBFBF9;
            ">
                Explorer la performance commerciale
                <span style="color:#66F2FF;">à travers la donnée.</span>
            </h1>

            <p style="
                font-size: 1.15rem;
                line-height: 1.7;
                color: #AAB5C4;
                max-width: 720px;
            ">
                Un dashboard interactif construit à partir de données de ventes
                afin d'explorer les performances commerciales, les produits,
                les boutiques et les clients.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # ============================================================
    # LE PROJET
    # ============================================================

    st.markdown(
        """
        <div style="padding: 35px 0 20px 0;">
            <div style="
                color:#66F2FF;
                font-size:0.75rem;
                font-weight:600;
                letter-spacing:1.5px;
                margin-bottom:10px;
            ">
                LE PROJET
            </div>

            <h2 style="
                color:#FBFBF9;
                font-size:2rem;
                margin-bottom:18px;
            ">
                De données brutes à une vision exploitable
            </h2>

            <p style="
                color:#AAB5C4;
                font-size:1rem;
                line-height:1.8;
                max-width:850px;
            ">
                L'idée de ce projet est de reproduire une problématique
                d'analyse commerciale : partir d'un volume important de
                données transactionnelles et construire un outil permettant
                de comprendre rapidement ce qui se passe dans l'activité.
            </p>

            <p style="
                color:#AAB5C4;
                font-size:1rem;
                line-height:1.8;
                max-width:850px;
            ">
                Les données permettent de croiser les ventes avec les produits,
                les boutiques et les clients afin d'obtenir différents niveaux
                de lecture de la performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ============================================================
    # PÉRIODE + DONNÉES
    # ============================================================

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown(
            """
            <div style="
                padding: 25px 0;
                border-left: 2px solid #4D9FFF;
                padding-left: 25px;
            ">
                <div style="
                    color:#AAB5C4;
                    font-size:0.8rem;
                    letter-spacing:1px;
                    margin-bottom:8px;
                ">
                    PÉRIODE ANALYSÉE
                </div>

                <div style="
                    color:#FBFBF9;
                    font-size:2rem;
                    font-weight:600;
                ">
                    01.01.2023
                    <span style="color:#66F2FF;">→</span>
                    31.12.2024
                </div>

                <div style="
                    color:#7F8B9B;
                    margin-top:8px;
                ">
                    Deux années de données de ventes
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                padding: 25px 0;
                border-left: 2px solid #B45CFF;
                padding-left: 25px;
            ">
                <div style="
                    color:#AAB5C4;
                    font-size:0.8rem;
                    letter-spacing:1px;
                    margin-bottom:8px;
                ">
                    VOLUME DE DONNÉES
                </div>

                <div style="
                    color:#FBFBF9;
                    font-size:2rem;
                    font-weight:600;
                ">
                    1 000 000
                </div>

                <div style="
                    color:#7F8B9B;
                    margin-top:8px;
                ">
                    transactions disponibles à l'analyse
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            **200**

            produits
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            **100**

            boutiques
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            **50 000**

            clients
            """,
            unsafe_allow_html=True
        )

    # ============================================================
    # STRUCTURE DE LA DONNÉE
    # ============================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="padding: 30px 0 15px 0;">
            <div style="
                color:#66F2FF;
                font-size:0.75rem;
                font-weight:600;
                letter-spacing:1.5px;
                margin-bottom:10px;
            ">
                STRUCTURE
            </div>

            <h2 style="
                color:#FBFBF9;
                font-size:2rem;
                margin-bottom:15px;
            ">
                Une donnée organisée autour des ventes
            </h2>

            <p style="
                color:#AAB5C4;
                line-height:1.7;
                max-width:750px;
            ">
                Les transactions constituent le point central du modèle.
                Elles sont reliées aux différentes dimensions permettant
                d'enrichir l'analyse.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            margin:35px 0;
            padding:30px;
            background:#111C2E;
            border-radius:12px;
            border:1px solid #26364A;
            text-align:center;
        ">

            <span style="color:#66F2FF;font-weight:600;">SALES</span>

            <span style="color:#59697D;padding:0 18px;">→</span>

            <span style="color:#FBFBF9;">PRODUCTS</span>

            <span style="color:#59697D;padding:0 18px;">·</span>

            <span style="color:#FBFBF9;">STORES</span>

            <span style="color:#59697D;padding:0 18px;">·</span>

            <span style="color:#FBFBF9;">CUSTOMERS</span>

            <span style="color:#59697D;padding:0 18px;">·</span>

            <span style="color:#FBFBF9;">CALENDAR</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ============================================================
    # PARCOURS
    # ============================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="padding: 20px 0;">
            <div style="
                color:#66F2FF;
                font-size:0.75rem;
                font-weight:600;
                letter-spacing:1.5px;
                margin-bottom:10px;
            ">
                EXPLORATION
            </div>

            <h2 style="
                color:#FBFBF9;
                font-size:2rem;
                margin-bottom:30px;
            ">
                Quatre angles de lecture
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div style="
                padding:25px;
                min-height:150px;
                background:#111C2E;
                border:1px solid #26364A;
                border-radius:12px;
            ">
                <div style="color:#4D9FFF;font-size:0.8rem;font-weight:600;">
                    01 — GLOBAL
                </div>
                <h3 style="color:#FBFBF9;">
                    Performance commerciale
                </h3>
                <p style="color:#8F9BAD;line-height:1.6;">
                    Évolution des ventes, chiffre d'affaires, coûts,
                    marge et principaux indicateurs.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                padding:25px;
                min-height:150px;
                background:#111C2E;
                border:1px solid #26364A;
                border-radius:12px;
            ">
                <div style="color:#66F2FF;font-size:0.8rem;font-weight:600;">
                    02 — PRODUITS
                </div>
                <h3 style="color:#FBFBF9;">
                    Quels produits fonctionnent ?
                </h3>
                <p style="color:#8F9BAD;line-height:1.6;">
                    Comparaison des produits, marques, catégories
                    et volumes de ventes.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div style="
                padding:25px;
                min-height:150px;
                background:#111C2E;
                border:1px solid #26364A;
                border-radius:12px;
            ">
                <div style="color:#B45CFF;font-size:0.8rem;font-weight:600;">
                    03 — BOUTIQUES
                </div>
                <h3 style="color:#FBFBF9;">
                    Où se fait la performance ?
                </h3>
                <p style="color:#8F9BAD;line-height:1.6;">
                    Analyse des performances par boutique, ville,
                    pays et type de point de vente.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                padding:25px;
                min-height:150px;
                background:#111C2E;
                border:1px solid #26364A;
                border-radius:12px;
            ">
                <div style="color:#B6FF00;font-size:0.8rem;font-weight:600;">
                    04 — CLIENTS
                </div>
                <h3 style="color:#FBFBF9;">
                    Qui achète ?
                </h3>
                <p style="color:#8F9BAD;line-height:1.6;">
                    Exploration des profils clients, de la fidélité
                    et des comportements d'achat.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ============================================================
    # ASSISTANT IA
    # ============================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            padding:35px;
            background:#111C2E;
            border:1px solid #26364A;
            border-radius:14px;
        ">

            <div style="
                color:#B45CFF;
                font-size:0.75rem;
                font-weight:600;
                letter-spacing:1.5px;
                margin-bottom:10px;
            ">
                EN PLUS
            </div>

            <h2 style="
                color:#FBFBF9;
                font-size:1.8rem;
                margin-bottom:12px;
            ">
                Interroger les données autrement
            </h2>

            <p style="
                color:#AAB5C4;
                line-height:1.7;
                max-width:750px;
                margin-bottom:0;
            ">
                L'onglet Assistant IA permet de poser des questions
                directement en langage naturel et d'obtenir une analyse
                basée sur les données disponibles dans le dashboard.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ============================================================
    # CONTACT
    # ============================================================

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            padding:20px 0 10px 0;
        ">
            <div style="
                color:#66F2FF;
                font-size:0.75rem;
                font-weight:600;
                letter-spacing:1.5px;
                margin-bottom:10px;
            ">
                CONTACT
            </div>

            <h2 style="
                color:#FBFBF9;
                font-size:1.8rem;
            ">
                Une question ou envie d'échanger ?
            </h2>

            <p style="color:#8F9BAD;">
                Vous pouvez me contacter directement depuis le dashboard.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    email = st.text_input(
        "Votre adresse email",
        placeholder="votre@email.com",
        label_visibility="visible"
    )

    message = st.text_area(
        "Message",
        placeholder="Votre message...",
        height=130
    )

    if st.button("✉  Me contacter"):

        if not message.strip():
            st.warning("Veuillez saisir un message.")

        else:
            body = message.strip()

            if email.strip():
                body += (
                    f"\n\n---\n"
                    f"Email de contact : {email.strip()}"
                )

            subject = "Contact depuis le Chocolate Sales Dashboard"

            mailto = (
                "mailto:theo.lepere@gmail.com"
                f"?subject={urllib.parse.quote(subject)}"
                f"&body={urllib.parse.quote(body)}"
            )

            st.markdown(
                f'<meta http-equiv="refresh" content="0;url={mailto}">',
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:45px 0 20px 0;
            color:#59697D;
            font-size:0.8rem;
        ">
            Chocolate Sales Dashboard · Théo Lepère
        </div>
        """,
        unsafe_allow_html=True
    )
