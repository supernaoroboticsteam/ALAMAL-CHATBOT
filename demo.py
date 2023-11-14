import streamlit as st
from dataclasses import dataclass
from typing import Literal

from langchain.chat_models import ChatGooglePalm
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory


st.set_page_config(
    page_title="ALAMAL",
    page_icon="🎗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help' : 'https://github.com/achraf110',
        'Report a bug' : 'https://github.com/achraf110',
        'About':"# ALAMAL, You are not alone."
    }
)
#--------------- Back end ----------
@dataclass
class Message : 
    origin: Literal["human","ai"]
    message: str

def load_css():
    with open('static/style.css',"r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)
    
# Behavior after click

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    llm_response = st.session_state.conversation.run(
        human_prompt
    )
    st.session_state.history.append(
        Message('human',human_prompt)
    )
    st.session_state.history.append(
        Message("ai",llm_response)
    )

    st.session_state.human_prompt = " "

# API LOAD PALM CHATBOT
def api():
    llm = ChatGooglePalm(
            google_api_key=st.secrets["palm_api_key"],
            temperature=0.4
            )
    return llm

#history show up 
def initilize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if "conversation" not in st.session_state:
        llm = api()
        st.session_state.conversation = ConversationChain(
            llm=llm)
        
#--------------- Front end-------------------
load_css()
initilize_session_state()

# This is the title and the initialisation of the containers 

st.title("ALAMAL this is your Chatbot assistant")
chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

# Streamlit built-in function for user interaction
with st.sidebar:
    st.sidebar.image("./static/logo.png")

    st.sidebar.markdown("---")
    header = st.sidebar.header("ALAMAL : Support When You Need It the Most")
    st.markdown("""
                **ALAMAL** offers an innovative web application with an integrated AI chatbot, tailoring its
                advice based on each patient's case. This platform combines exchange, reliable information,
                and emotional support, thereby enhancing the healing journey for cancer patients.""")
    
    # Contributors 
    st.sidebar.markdown("---")
    with st.expander('Contributors'):
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**CHAHBI Achraf**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/achraf-chahbi" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        with columns[2]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.github.com/achraf110" style="float:center">
                            <img src="./app/static/github-sign.png" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**EL JABRI Nabil**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/nabil-eljabri-77860723b/" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        with columns[2]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://github.com/drdarkfrancis" style="float:center">
                            <img src="./app/static/github-sign.png" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**LAKRARSI El Batoul**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/el-batoul-lakrarsi/" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**EL HAI Ibtissam**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/ibtissam-el-hai-9417b0197" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**BATAHI Salma**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/salma-batahi-/" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
        columns = st.columns([3,1,1])
        with columns[0]:
            st.write("**ELMIMOUNI Firdaous**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.linkedin.com/in/firdaous-elmimouni-62b737232" style="float:center">
                            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)
            
    # University drop down         
    with st.expander("University"):
        st.image("./static/uni_logo.png")
    with st.expander('Coordinator'):
        columns = st.columns([3,1])
        with columns[0]:
            st.write("**Pr.BACHIRI Mustapha**")
        with columns[1]:
            st.write("""<div style="width:100%;text-align:center;">
                            <a href="https://www.researchgate.net/profile/Mustapha-Bachiri-2" style="float:center">
                            <img src="./app/static/researchgate.png" width="22px"></img>
                            </a></div>""",unsafe_allow_html=True)

with chat_placeholder:  # chat display
    for chat in st.session_state.history:
        div = f"""
            <div class="chat-row {
                '' if chat.origin == "ai" else "row-reverse"}">
                <img class="chat-icon" src='./app/static/{"robot.png" if chat.origin == 'ai' else 'user.png '}' 
                width=32 height=32>
                <div class="chat-bubble
                {"ai-bubble" if chat.origin == 'ai' else "human-bubble"}">{chat.message}</div>
            </div>
            """
        st.markdown(div,unsafe_allow_html=True)

# Prompt behavior
with prompt_placeholder:
    cols = st.columns((6,1))
    cols[0].text_input(
        label="chat",
        value="Hello Bot",
        label_visibility="collapsed",
        key='human_prompt'
    )
    cols[1].form_submit_button(
        label="Submit",
        type='primary',
        on_click=on_click_callback
    )