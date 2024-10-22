import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Recent Projects", layout="wide")

# Custom CSS for dark theme, color scheme, Graduate font, and stylish border
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Graduate&display=swap');

    * {
        font-family: 'Graduate', cursive;
    }
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stSidebar {
        background-color: #2A2A2A;
        padding-top: 2rem;
    }
    .stSidebar .sidebar-content {
        width: 150px !important;
    }
    .sidebar-button {
        width: 100%;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        background-color: transparent;
        color: #FFFFFF;
        border: none;
        text-align: left;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .sidebar-button:hover {
        background-color: #3A3A3A;
    }
    .sidebar-button.active {
        background-color: #FF4B4B;
    }
    .title-border {
        border: none;
        height: 5px;
        background: linear-gradient(90deg, #FF4B4B, #0066CC);
        margin-bottom: 20px;
        position: relative;
    }
    .title-border::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #0066CC, #FF4B4B);
    }
    // ... (rest of your existing styles)
</style>
""", unsafe_allow_html=True)

# Function to safely load an image
def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        st.warning(f"Unable to load image: {image_path}")
        st.error(f"Error: {e}")
        return None

# Navigation
def navigation():
    with st.sidebar:
        if st.button("Recent Projects", key="Recent Projectse", help="View Recent Projects", use_container_width=True):
            st.session_state.page = "app_suite"
        if st.button("About", key="about", help="View About Page", use_container_width=True):
            st.session_state.page = "about"
    st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)

# Function to create an app tile
def create_app_tile(title, image_path, description, tech_stack, app_url):
    with st.container():
        st.markdown('<div class="app-container">', unsafe_allow_html=True)
        st.markdown(f'<p class="app-title">{title}</p>', unsafe_allow_html=True)
        
        image = load_image(image_path)
        if image:
            st.image(image, use_column_width=True)
        
        st.markdown(f'<p class="app-description" style="text-align: center;">{description}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="app-tech-stack" style="text-align: center;"><span style="color: red;">Tech Stack</span>: {tech_stack}</p>', unsafe_allow_html=True)
        
        st.markdown(f'''
            <div style="display: flex; justify-content: center; margin-top: 20px;">
                <a href="{app_url}" target="_blank" style="text-decoration: none;">
                    <button style="
                        font-family: 'Graduate', cursive;
                        background-color: #8B0000;
                        color: #FFFFFF;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        transform-style: preserve-3d;
                        perspective: 1000px;
                    ">
                        Launch {title}
                    </button>
                </a>
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)

# App Suite Page
def app_suite_page():
    st.markdown('<h1 style="font-family: \'Graduate\', cursive; color: #FFFFFF; font-size: 33px; text-align: center;">A small collection of more recent projects</h1>', unsafe_allow_html=True)
    st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)
    
    
    create_app_tile(
        "Chat SQL",
        "images/1.jpg",
        "It is a data analytics tool with the power of Large Language Models (LLMs), allowing users to query and explore their MySQL databases with intuitive, natural language conversations. Seamlessly bridge the gap between human insight and data understanding.",
        "Python, OpenAI, Streamlit, Langchain, Groq",
        "https://chatwdb.streamlit.app"
    )


# About Page
def about_page():
    st.markdown('<h1 style="font-family: \'Graduate\', cursive; color: #FFFFFF;">About</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family: 'Graduate', cursive;">
     <div style="text-align: center;">
     • Hello, I am <span style="color: #FF4B4B;">Archisman</span>, a data engineer.<br>
     • Welcome to my Recent Projects • This segment deals with the projects that are in the pipeline and yet to be released.
     </div>

    <h3 style="font-family: 'Graduate', cursive; color: #FF4B4B;">Contact Me</h3>

    I'd love to hear from you. Whether you have questions, feedback, or ideas for new applications.

    Email: ggengineerco@gmail.com
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)

# Main app logic
if 'page' not in st.session_state:
    st.session_state.page = "app_suite"

navigation()

if st.session_state.page == "app_suite":
    app_suite_page()
elif st.session_state.page == "about":
    about_page()