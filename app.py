import streamlit as st
from modules.auth import register_user, login_user
from modules.prompt_engineering import enhance_prompt
from modules.gemini_prompt import generate_final_prompt
from modules.image_generator import generate_image
from modules.chat_store import save_chat, load_chats

st.set_page_config(page_title="AI Studio", layout="wide")

st.write("APP STARTED")

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "home"

if "images" not in st.session_state:
    st.session_state.images = []


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

/* GLOBAL */
html, body, [class*="css"]  {
    background-color: #0E1117;
    color: #ECECF1;
    font-family: 'Inter', sans-serif;
}

/* MAIN CONTAINER */
.block-container {
    padding-top: 1rem;
    max-width: 800px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #171923;
    border-right: 1px solid #2A2B32;
}

/* SIDEBAR TEXT FIX */
section[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* SIDEBAR BUTTONS */
section[data-testid="stSidebar"] button {
    background-color: transparent;
    color: #FFFFFF !important;
    border: none;
    text-align: left;
    padding: 10px;
    border-radius: 8px;
    transition: 0.2s;
}

section[data-testid="stSidebar"] button:hover {
    background-color: #2A2B32;
}

/* BUTTONS */
.stButton > button {
    background-color: #19C37D;
    color: black;
    border-radius: 8px;
    padding: 10px 16px;
    font-weight: 600;
    border: none;
    margin-top: 8px;
}

/* INPUTS */
.stTextInput>div>div>input,
.stTextArea textarea {
    background-color: #1E1F26;
    color: #FFFFFF !important;
    border: 1px solid #2A2B32;
    border-radius: 10px;
    padding: 12px;
}

/* OUTPUT (FIX GREY ISSUE) */
.stMarkdown, .stText, .stCode {
    background-color: #1E1F26 !important;
    color: #FFFFFF !important;
    opacity: 1 !important;
    padding: 14px;
    border-radius: 12px;
    border: 1px solid #2A2B32;
    margin-bottom: 12px;
    line-height: 1.6;
}

/* CODE */
pre, code {
    background-color: #111827 !important;
    color: #FFFFFF !important;
}

/* TABS */
.stTabs [data-baseweb="tab"] {
    color: #A1A1AA;
}

.stTabs [aria-selected="true"] {
    color: #19C37D !important;
    border-bottom: 2px solid #19C37D;
}

/* HEADINGS */
h1, h2, h3 {
    color: #FFFFFF !important;
}

/* REMOVE BROKEN CHAT CSS (IMPORTANT RESET) */
.stTextArea, .stButton {
    position: static !important;
    transform: none !important;
    width: auto !important;
}
            
/* FIX TITLE VISIBILITY */
h1 {
    color: #FFFFFF !important;
}

/* SCROLL */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-thumb {
    background: #2A2B32;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


if not st.session_state.user:

    st.title("🔐 AI Image Studio")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        full_name = st.text_input("Full Name")
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(username, password, full_name):
                st.success("Account created")
            else:
                st.error("Username exists")


else:
  
    st.sidebar.title("🚀 AI Studio")

    if st.sidebar.button("🆕 New Chat"):
        st.session_state.page = "home"

    if st.sidebar.button("💬 Previous Chats"):
        st.session_state.page = "chats"

    if st.sidebar.button("🖼️ My Stuff"):
        st.session_state.page = "gallery"

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()


    if st.session_state.page == "home":

        st.title("✨ AI Studio")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🖼️ Create Image"):
                st.session_state.page = "image"

            if st.button("✨ Create Prompt"):
                st.session_state.page = "prompt"

        with col2:
            if st.button("✍️ Write Anything"):
                st.session_state.page = "write"

            if st.button("📚 Help Me Learn"):
                st.session_state.page = "learn"


    elif st.session_state.page == "image":

        st.title("🖼️ Create Image")

        prompt = st.text_area("Enter prompt")

        if st.button("Generate Image"):

            enhanced = enhance_prompt(prompt)
            final_prompt = generate_final_prompt(enhanced)

            image = generate_image(final_prompt)

            if image:
                st.image(image)
                st.session_state.images.append(image)

                st.download_button("Download", image, "image.png")


    elif st.session_state.page == "prompt":

        st.title("✨ Create Prompt")

        text = st.text_area("Enter idea")

        if st.button("Generate"):
            enhanced = enhance_prompt(text)
            result = generate_final_prompt(enhanced)

            st.code(result)
            save_chat({"type": "prompt", "content": result})


    elif st.session_state.page == "write":

        st.title("✍️ Write Anything")

        text = st.text_area("Enter topic")

        if st.button("Generate"):
            result = generate_final_prompt(f"Write a story about {text}")
            st.write(result)

            save_chat({"type": "write", "content": result})


    elif st.session_state.page == "learn":

        st.title("📚 Help Me Learn")

        topic = st.text_input("Enter topic")

        if st.button("Explain"):

            prompt = f"""
Explain {topic} in structured format:

1. Definition
2. Key Concepts
3. Examples
4. Real-world use
"""

            result = generate_final_prompt(prompt)
            st.write(result)

            save_chat({"type": "learn", "content": result})


    elif st.session_state.page == "chats":

        st.title("💬 Previous Chats")

        chats = load_chats()

        for c in chats[::-1]:
            st.write(f"🔹 {c['type']}: {c['content']}")


    elif st.session_state.page == "gallery":

        st.title("🖼️ My Images")

        for img in st.session_state.images:
            st.image(img)