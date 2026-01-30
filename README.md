# Streamlit + shadcn Template 🎨

A beautiful, production-ready template for building data applications with Streamlit and shadcn-ui components.

## Features ✨

- 🏠 **Multi-page Navigation**: Home and Settings pages with sidebar menu
- 🎨 **shadcn-ui Components**: Beautiful UI components including cards, progress bars, accordions, and forms
- 📱 **Responsive Layout**: Works great on desktop and mobile devices
- ⚙️ **Comprehensive Settings**: Theme customization, notifications, and privacy controls
- 🚀 **Easy to Extend**: Well-structured codebase ready for your customizations

## Quick Start 🚀

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/dcosta-stf/streamlit-template.git
cd streamlit-template
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Project Structure 📁

```
streamlit-template/
├── app.py                 # Main application file (Home page)
├── pages/
│   └── settings.py       # Settings page
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Dependencies 📦

- **streamlit**: The main framework for building data apps
- **streamlit-shadcn-ui**: Beautiful UI components inspired by shadcn/ui
- **st-pages**: Enhanced page navigation for multi-page apps

## Usage 💡

### Home Page
The home page demonstrates:
- Progress indicators for tracking tasks
- Metric cards for displaying statistics
- Accordion/expander components for organizing content
- Interactive forms and buttons
- Multi-column layouts

### Settings Page
The settings page includes:
- Tabbed interface for organizing settings
- Appearance customization (theme, colors, font size)
- Notification preferences
- Privacy and security controls
- Data management options

## Customization 🎨

### Adding New Pages

1. Create a new Python file in the `pages/` directory
2. Add the page reference in `app.py`:
```python
show_pages([
    Page("app.py", "Home", "🏠"),
    Page("pages/settings.py", "Settings", "⚙️"),
    Page("pages/your_new_page.py", "New Page", "📄"),  # Add this
])
```

### Styling

Streamlit uses its own theming system. You can customize the theme by creating a `.streamlit/config.toml` file:

```toml
[theme]
primaryColor = "#3b82f6"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## License 📄

This project is open source and available under the MIT License.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Support 💬

If you encounter any issues or have questions, please open an issue on GitHub.