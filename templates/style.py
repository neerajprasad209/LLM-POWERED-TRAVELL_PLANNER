import streamlit as st

def apply_custom_styles():
    """Apply custom CSS and HTML styling to the Streamlit app"""
    
    # Custom CSS styling
    custom_css = """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styling */
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
        color: #ffffff !important;
        background-attachment: fixed;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Sidebar styling */

    
    .sidebar .sidebar-content {
        background: transparent;
    }
    
    /* Form styling */
    .stForm {
        background: rgba(255, 255, 255, 0.2);
        padding: 1.5rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin: 1rem 0;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        border: 2px solid transparent;
        border-radius: 10px;
        padding: 0.75rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    

    
    /* Button styling */
    .stFormSubmitButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stFormSubmitButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba(102, 126, 234, 0.4);
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    
    /* Title styling */
    .main h1 {
        color: #2d3748;
        font-weight: 700;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Subtitle styling */
    .main p {
        text-align: center;
        color: #718096;
        font-size: 1.2rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    /* Sidebar header styling */
    .sidebar h2 {
        color: white;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Sidebar labels */
    .sidebar label {
        color: white !important;
        font-weight: 500;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    /* Subheader styling */
    .main h2, .main h3 {
        color: #2d3748;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Warning and error styling */
    .stAlert {
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Animation for content */
    .main .block-container > div {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main h1 {
            font-size: 2rem;
        }
        
        .main .block-container {
            margin: 0.5rem;
            padding: 1rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    
    
    /* Floating elements effect */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    </style>
    """
    
    # Apply the CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Add floating background elements
    background_html = """
    <div style="position: fixed; top: 10%; left: 10%; width: 100px; height: 100px; 
                background: linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                border-radius: 50%; z-index: -1; animation: floating 4s ease-in-out infinite;"></div>
    
    <div style="position: fixed; top: 60%; right: 15%; width: 80px; height: 80px; 
                background: linear-gradient(45deg, rgba(240, 147, 251, 0.1), rgba(245, 87, 108, 0.1)); 
                border-radius: 50%; z-index: -1; animation: floating 3s ease-in-out infinite 1s;"></div>
    
    <div style="position: fixed; bottom: 20%; left: 20%; width: 60px; height: 60px; 
                background: linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                border-radius: 50%; z-index: -1; animation: floating 5s ease-in-out infinite 2s;"></div>
    """
    
    st.markdown(background_html, unsafe_allow_html=True)

def add_custom_header():
    """Add a custom animated header"""
    header_html = """
    <div style="text-align: center; padding: 1rem 0; margin-bottom: 2rem;">
        <div style="display: inline-block; background: linear-gradient(45deg, #667eea, #764ba2); 
                    padding: 0.5rem 1rem; border-radius: 50px; color: white; font-weight: 600;
                    box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3); animation: floating 3s ease-in-out infinite;">
            🌟 Welcome to Your AI Travel Assistant 🌟
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def add_footer():
    """Add a custom footer"""
    footer_html = """
    <div style="text-align: center; padding: 2rem 0; margin-top: 3rem; 
                border-top: 1px solid rgba(0, 0, 0, 0.1);">
        <p style="color: #ffffff; font-size: 0.9rem; margin: 0;">
            ✈️ Made with ❤️ for travelers around the world 🌍
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)