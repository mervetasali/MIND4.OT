import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* Main background */
        .stApp {
            background-color: #f4f7fb;
        }


        /* Header */
        /* Sidebar içeriğini referans al */
section[data-testid="stSidebar"] > div {
    position: relative;
    height: 100vh;
}


/* User bilgisini sidebar'ın dibine sabitle */
.sidebar-user {
    position: absolute;
    bottom: 20px;
    left: 20px;

    color: white;
    font-size: 14px;
    font-weight: 600;
}


        /* Welcome area */
        .welcome {
            text-align: center;

            padding-top: 50px;
            padding-bottom: 40px;
        }


        .welcome h1 {
            color: #102a43;

            font-size: 42px;

            margin-bottom: 5px;
        }


        .welcome p {
            color: #627d98;

            font-size: 16px;
        }


        /* MES and MIND cards */
        .module-card {

            background-color: white;

            border: 1px solid #dce4ec;

            border-radius: 16px;

            height: 180px;

            display: flex;

            align-items: center;

            justify-content: center;

            box-shadow: 0px 4px 14px rgba(0,0,0,0.05);
        }


        .module-card h2 {
            color: #102a43;

            font-size: 28px;
        }

        /* Keep the sidebar fixed */
        section[data-testid="stSidebar"] {
            position: fixed;
            height: 100vh;
            top: 0;
            left: 0;
        }

        /* Hide the collapse/expand button for the sidebar */
        [data-testid="stSidebarCollapseButton"] {
            display: none;
        }

        /* Sidebar overview */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #12365d 0%,
        #0b2542 100%
    );

    border-right: 1px solid #17395f;
}


/* Text in sidebar */
section[data-testid="stSidebar"] * {
    color: #f4f8fc;
}


/* Sidebar header */
section[data-testid="stSidebar"] h2 {
    color: white;
    font-size: 22px;
    font-weight: 700;

    margin-bottom: 20px;
}


/* Sidebar buttons */
section[data-testid="stSidebar"] div.stButton > button {

    background-color: transparent;

    color: #eaf2fa;

    border: none;

    border-radius: 8px;

    text-align: left;

    justify-content: flex-start;

    padding-left: 16px;

    height: 44px;

    font-weight: 500;
}


/* Hover effect */
section[data-testid="stSidebar"] div.stButton > button:hover {

    background-color: rgba(255,255,255,0.10);

    color: white;
}



section[data-testid="stSidebar"] div.stButton:first-of-type > button {

    background-color: rgba(255,255,255,0.14);

    font-weight: 700;
}

        /* Card Description */
.card-description {
    text-align: center;
    color: #627d98;
    font-size: 15px;

    margin-top: 5px;
    margin-bottom: 15px;
}


/* Card buttons */
div.stButton > button {
    background-color: #0b5fa5;
    color: white;
    border: none;
    border-radius: 8px;
    height: 42px;
    font-weight: 600;
}

        </style>
        """,
        unsafe_allow_html=True
    )