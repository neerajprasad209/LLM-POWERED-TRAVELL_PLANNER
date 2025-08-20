from templates.style import apply_custom_styles, add_custom_header, add_footer
from utils.logger import get_logger
from utils.custom_exception import CustomException
from utils.common_function import stream_data
from chains.itinerary_chain import LLMModel
from core.planner import TravelPlanner
from config.path_config import LOGS_DIR, CONFIG_YAML
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

logger = get_logger(__name__)


def main():
    try:
        st.set_page_config(
            page_title="Travel Planner", 
            page_icon="✈️", 
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Apply custom styles
        apply_custom_styles()
        
        # Add custom header
        add_custom_header()

        # Sidebar form with enhanced styling
        with st.sidebar:
            st.header("🛠️ Trip Details")
            
            # Add some spacing and description
            st.markdown("---")
            st.markdown("*Fill in the details below to create your perfect itinerary*")
            
            with st.form("travel_planner_form"):
                city_input = st.text_input(
                    "🌍 Enter your city of interest:",
                    placeholder="e.g., Paris, Tokyo, New York"
                )
                interests_input = st.text_input(
                    "🎯 Enter your interests (comma-separated):",
                    placeholder="e.g., museums, food, nightlife, nature"
                )
                days_input = st.text_input(
                    "📅 Enter the number of days:",
                    placeholder="e.g., 3, 5, 7"
                )
                
                # Add some spacing
                st.markdown("<br>", unsafe_allow_html=True)
                
                submit_button = st.form_submit_button("✨ Generate Itinerary")
            
            # Add tips section in sidebar
            st.markdown("---")
            st.markdown("### 💡 Tips")
            st.info("💡 Be specific with your interests for better recommendations!")
            st.info("🎯 Try interests like: 'art galleries, local cuisine, historical sites'")

        # Main content area
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.title("✈️ AI Travel Itinerary Planner", width="stretch")
            st.markdown("### Plan your perfect trip with AI-powered recommendations")
            
            # Add some visual elements
            st.markdown("---")

        # Process form submission
        if submit_button:
            if city_input and interests_input:
                # Add loading animation
                with st.spinner(text="🔄 Creating your amazing itinerary..."):
                    planner = TravelPlanner()
                    planner.set_city(city_input)
                    planner.set_interests(interests_input)
                    planner.set_days(days_input)
                    itenary = planner.create_itinary()
                
                # Display results with better formatting
                st.success("🎉 Your itinerary is ready!")
                st.subheader("📝 Your Personalized Itinerary")
                
                # Create a container for the itinerary with custom styling
                with st.container():
                    
                    st.write_stream(stream_data(itenary))
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                
                # Add action buttons
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.button("📧 Email Itinerary", help="Email this itinerary to yourself")
                with col2:
                    st.button("📱 Share", help="Share your itinerary")
                with col3:
                    st.button("💾 Save", help="Save itinerary for later")
                    
            else:
                st.warning("⚠️ Please enter both city and interests to generate your itinerary.")
                st.info("👆 Use the sidebar form to get started!")
        
        # Add footer
        add_footer()

    except Exception as e:
        st.error(f"🚨 An error occurred: {str(e)}")
        st.info("Please try again or contact support if the issue persists.")

if __name__ == "__main__":
    main()
