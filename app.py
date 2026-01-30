"""
Streamlit + shadcn Template App
Main entry point for the application
"""
import streamlit as st
from streamlit_shadcn_ui import progress, badges, metric_card

# Configure the page
st.set_page_config(
    page_title="Streamlit + shadcn Template",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page title
st.title("🏠 Home")

# Main content
st.markdown("## Welcome to the Streamlit + shadcn Template! 👋")
st.markdown("This template demonstrates various shadcn-ui components integrated with Streamlit.")

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Progress Indicators")
    st.markdown("Track your progress with beautiful progress bars:")
    
    # Progress bars with labels
    st.write("Getting Started (25%)")
    progress(data=25, key="progress1")
    
    st.write("In Progress (50%)")
    progress(data=50, key="progress2")
    
    st.write("Almost Done (75%)")
    progress(data=75, key="progress3")
    
    st.write("Completed (100%)")
    progress(data=100, key="progress4")

with col2:
    st.markdown("### 🎯 Quick Stats")
    
    # Create metric cards
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        metric_card(
            title="Total Projects",
            content="12",
            description="Active projects",
            key="metric1"
        )
        
    with metric_col2:
        metric_card(
            title="Completion Rate",
            content="87%",
            description="Tasks completed",
            key="metric2"
        )
    
    # Standard Streamlit metrics
    st.metric("Active Users", "1,234", "+54")

st.markdown("---")

# Card components section
st.markdown("### 🎴 Card Components")

card_col1, card_col2, card_col3 = st.columns(3)

with card_col1:
    with st.container(border=True):
        st.markdown("#### 🚀 Getting Started")
        st.markdown("Learn how to use this template")
        st.markdown("- Install dependencies")
        st.markdown("- Run the app")
        st.markdown("- Customize it!")

with card_col2:
    with st.container(border=True):
        st.markdown("#### 📚 Documentation")
        st.markdown("Comprehensive guides and API references")
        st.markdown("- Component library")
        st.markdown("- Best practices")
        st.markdown("- Examples")

with card_col3:
    with st.container(border=True):
        st.markdown("#### 🤝 Community")
        st.markdown("Join our growing community")
        st.markdown("- Forums")
        st.markdown("- Discord")
        st.markdown("- GitHub")

st.markdown("---")

# Accordion section
st.markdown("### 📚 Feature Information")

with st.expander("What is this template?"):
    st.markdown("This is a production-ready template combining Streamlit with shadcn-ui components for building beautiful data applications.")

with st.expander("Key Features"):
    st.markdown("""
    - ✅ Multi-page navigation
    - ✅ shadcn-ui components
    - ✅ Responsive layout
    - ✅ Easy to customize
    """)

with st.expander("Getting Started"):
    st.markdown("""
    1. Install dependencies: `pip install -r requirements.txt`
    2. Run the app: `streamlit run app.py`
    3. Start building!
    """)

st.markdown("---")

# Interactive section
st.markdown("### 🎨 Try it out!")

form_col1, form_col2 = st.columns(2)

with form_col1:
    st.markdown("#### Quick Form")
    with st.form("quick_form"):
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@example.com")
        message = st.text_area("Message", placeholder="Tell us what you think...")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if name and email and message:
                st.success(f"✅ Thanks {name}! Your message has been received.")
            else:
                st.error("❌ Please fill in all required fields.")

with form_col2:
    st.markdown("#### Component Examples")
    
    # Button examples
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Primary", type="primary", use_container_width=True):
            st.toast("✅ Primary button clicked!")
    with col_btn2:
        if st.button("Secondary", use_container_width=True):
            st.toast("✅ Secondary button clicked!")
    
    st.markdown("---")
    
    # Select boxes
    option = st.selectbox(
        "Choose an option",
        ["Option 1", "Option 2", "Option 3"]
    )
    
    # Slider
    value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Selected value: **{value}**")
    
    # Badges
    badge_col1, badge_col2, badge_col3 = st.columns(3)
    with badge_col1:
        badges(badge_list=[("Active", "default")], key="badge1")
    with badge_col2:
        badges(badge_list=[("New", "secondary")], key="badge2")
    with badge_col3:
        badges(badge_list=[("Pro", "outline")], key="badge3")

# Alert example
st.markdown("---")
st.markdown("### 🔔 Alert Examples")

alert_col1, alert_col2 = st.columns(2)
with alert_col1:
    st.info("ℹ️ This is an informative message!")
    st.success("✅ Operation completed successfully!")
with alert_col2:
    st.warning("⚠️ Please review this warning.")
    st.error("❌ An error occurred during processing.")

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
