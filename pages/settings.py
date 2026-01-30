"""
Settings Page
Configuration and preferences for the application
"""
import streamlit as st
from streamlit_shadcn_ui import switch, slider, alert, badges

# Configure the page
st.set_page_config(
    page_title="Settings - Streamlit Template",
    page_icon="⚙️",
    layout="wide",
)

# Page title
st.title("⚙️ Settings")

st.markdown("Configure your application settings and preferences.")

# Create tabs for different settings categories
tab1, tab2, tab3 = st.tabs(["🎨 Appearance", "🔔 Notifications", "🔒 Privacy"])

with tab1:
    st.markdown("### Appearance Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Theme")
        theme = st.selectbox(
            "Select theme",
            ["Light", "Dark", "Auto"],
            index=2
        )
        
        st.markdown("#### Color Scheme")
        color_scheme = st.selectbox(
            "Primary color",
            ["Blue", "Green", "Purple", "Red", "Orange"],
            index=0
        )
        
        st.markdown("#### Font Size")
        font_size = st.slider("Adjust font size", 12, 20, 14)
        st.caption(f"Current size: {font_size}px")
    
    with col2:
        st.markdown("#### Layout")
        layout_compact = st.checkbox("Compact layout", value=False)
        show_sidebar = st.checkbox("Show sidebar by default", value=True)
        
        st.markdown("#### Display Options")
        show_tooltips = st.checkbox("Show tooltips", value=True)
        enable_animations = st.checkbox("Enable animations", value=True)
        high_contrast = st.checkbox("High contrast mode", value=False)
    
    st.markdown("---")
    
    # Preview section
    st.markdown("#### Preview")
    with st.container(border=True):
        st.markdown(f"This is a preview with **{theme}** theme and **{color_scheme}** color scheme.")
        st.progress(0.75)
        st.caption(f"Font size: {font_size}px")

with tab2:
    st.markdown("### Notification Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Email Notifications")
        email_notifications = st.checkbox("Enable email notifications", value=True)
        
        if email_notifications:
            st.text_input("Email address", placeholder="user@example.com")
            
            st.markdown("##### Notification Types")
            notify_updates = st.checkbox("Product updates", value=True)
            notify_news = st.checkbox("News and announcements", value=True)
            notify_tips = st.checkbox("Tips and tutorials", value=False)
            notify_marketing = st.checkbox("Marketing emails", value=False)
    
    with col2:
        st.markdown("#### Push Notifications")
        push_notifications = st.checkbox("Enable push notifications", value=True)
        
        if push_notifications:
            st.markdown("##### Alert Types")
            alert_errors = st.checkbox("Error alerts", value=True)
            alert_warnings = st.checkbox("Warning alerts", value=True)
            alert_info = st.checkbox("Info messages", value=False)
        
        st.markdown("#### Notification Frequency")
        frequency = st.radio(
            "How often would you like to receive notifications?",
            ["Immediately", "Hourly digest", "Daily digest", "Weekly digest"],
            index=0
        )
    
    st.markdown("---")
    
    with st.expander("🔕 Do Not Disturb"):
        enable_dnd = st.checkbox("Enable Do Not Disturb mode", value=False)
        if enable_dnd:
            dnd_col1, dnd_col2 = st.columns(2)
            with dnd_col1:
                st.time_input("Start time", value=None)
            with dnd_col2:
                st.time_input("End time", value=None)

with tab3:
    st.markdown("### Privacy & Security Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Data Collection")
        analytics = st.checkbox("Allow analytics", value=True)
        crash_reports = st.checkbox("Send crash reports", value=True)
        usage_data = st.checkbox("Share usage data", value=False)
        
        st.markdown("#### Privacy")
        public_profile = st.checkbox("Make profile public", value=False)
        show_activity = st.checkbox("Show activity status", value=True)
        allow_indexing = st.checkbox("Allow search engine indexing", value=False)
    
    with col2:
        st.markdown("#### Security")
        two_factor = st.checkbox("Enable two-factor authentication", value=False)
        
        if two_factor:
            st.info("📱 Two-factor authentication adds an extra layer of security to your account.")
            auth_method = st.radio(
                "Authentication method",
                ["SMS", "Authenticator app", "Email"],
                index=1
            )
        
        st.markdown("#### Session Management")
        session_timeout = st.selectbox(
            "Session timeout",
            ["15 minutes", "30 minutes", "1 hour", "4 hours", "Never"],
            index=2
        )
    
    st.markdown("---")
    
    # Data management section
    with st.expander("💾 Data Management"):
        st.markdown("#### Export Your Data")
        st.markdown("Download a copy of your data in JSON format.")
        st.button("Request Data Export", type="secondary")
        
        st.markdown("#### Delete Your Data")
        st.markdown("Permanently delete all your data from our servers.")
        st.button("Delete All Data", type="primary")

# Action buttons at the bottom
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("💾 Save Settings", type="primary", use_container_width=True):
        st.success("✅ Settings saved successfully!")

with col2:
    if st.button("↺ Reset to Defaults", use_container_width=True):
        st.warning("⚠️ Settings reset to defaults!")

with col3:
    st.empty()

# Info section
st.markdown("---")
st.info("💡 **Tip:** Changes are automatically saved when you interact with the settings.")
