"""
Streamlit + shadcn Template App
Main entry point for the application
"""
import streamlit as st
from streamlit_shadcn_ui import card, progress, accordion, badges, button, input, textarea
from st_pages import Page, show_pages, add_page_title

# Configure the page
st.set_page_config(
    page_title="Streamlit + shadcn Template",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure pages
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/settings.py", "Settings", "⚙️"),
    ]
)

# Add page title
add_page_title()

# Main content
st.markdown("## Welcome to the Streamlit + shadcn Template! 👋")
st.markdown("This template demonstrates various shadcn-ui components integrated with Streamlit.")

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Progress Indicators")
    st.markdown("Track your progress with beautiful progress bars:")
    
    # Progress bars
    progress(value=25, text="Getting Started", key="progress1")
    progress(value=50, text="In Progress", key="progress2")
    progress(value=75, text="Almost Done", key="progress3")
    progress(value=100, text="Completed", key="progress4")

with col2:
    st.markdown("### 🎯 Quick Stats")
    
    # Create some stat cards using badges
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    with stats_col1:
        st.metric("Total Projects", "12", "+2")
    with stats_col2:
        st.metric("Active Users", "1,234", "+54")
    with stats_col3:
        st.metric("Completion Rate", "87%", "+5%")

st.markdown("---")

# Accordion section
st.markdown("### 📚 Feature Information")

accordion_items = [
    {
        "title": "What is this template?",
        "content": "This is a production-ready template combining Streamlit with shadcn-ui components for building beautiful data applications."
    },
    {
        "title": "Key Features",
        "content": "✅ Multi-page navigation\n✅ shadcn-ui components\n✅ Responsive layout\n✅ Easy to customize"
    },
    {
        "title": "Getting Started",
        "content": "1. Install dependencies: pip install -r requirements.txt\n2. Run the app: streamlit run app.py\n3. Start building!"
    }
]

for item in accordion_items:
    with st.expander(item["title"]):
        st.markdown(item["content"])

st.markdown("---")

# Interactive section
st.markdown("### 🎨 Try it out!")

form_col1, form_col2 = st.columns(2)

with form_col1:
    st.markdown("#### Quick Form")
    with st.form("quick_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success(f"Thanks {name}! Your message has been received.")

with form_col2:
    st.markdown("#### Component Examples")
    
    # Button examples
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("Primary", type="primary"):
            st.toast("Primary button clicked!")
    with col_btn2:
        if st.button("Secondary"):
            st.toast("Secondary button clicked!")
    with col_btn3:
        if st.button("Outline", type="secondary"):
            st.toast("Outline button clicked!")
    
    st.markdown("---")
    
    # Select boxes
    option = st.selectbox(
        "Choose an option",
        ["Option 1", "Option 2", "Option 3"]
    )
    
    # Slider
    value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Selected value: {value}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; padding: 20px;'>
        Built with ❤️ using Streamlit + shadcn-ui
    </div>
    """,
    unsafe_allow_html=True
)
