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

#### Option 1: Run Locally

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

#### Option 2: Run with Docker

Build the Docker image:
```bash
docker build -t streamlit-template .
```

Run the container:
```bash
docker run -p 8501:8501 streamlit-template
```

The application will be available at `http://localhost:8501`

To run in detached mode:
```bash
docker run -d -p 8501:8501 --name streamlit-app streamlit-template
```

Stop the container:
```bash
docker stop streamlit-app
docker rm streamlit-app
```

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

1. Create a new Python file in the `pages/` directory (e.g., `pages/analytics.py`)
2. Streamlit will automatically detect it and add it to the sidebar navigation
3. The page filename determines the menu label (e.g., `analytics.py` becomes "Analytics")
4. You can customize the page icon and name using page configuration:

```python
import streamlit as st

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics")
# Your page content here
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

## Docker Deployment 🐳

This template includes a Dockerfile for containerized deployment.

### Building the Docker Image

```bash
docker build -t streamlit-template .
```

### Running the Container

```bash
docker run -p 8501:8501 streamlit-template
```

### Publishing to Docker Hub

1. Tag your image:
```bash
docker tag streamlit-template yourusername/streamlit-template:latest
```

2. Push to Docker Hub:
```bash
docker push yourusername/streamlit-template:latest
```

### Deploying to Cloud Platforms

The Dockerfile is compatible with popular cloud platforms:

- **Google Cloud Run**: `gcloud run deploy --image gcr.io/PROJECT_ID/streamlit-template`
- **AWS ECS/Fargate**: Use the image with your ECS task definition
- **Azure Container Instances**: `az container create --image yourusername/streamlit-template:latest`
- **Heroku**: Use the Heroku Container Registry
- **Railway/Render**: Connect your GitHub repository with automatic deployments

## License 📄

This project is open source and available under the MIT License.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Support 💬

If you encounter any issues or have questions, please open an issue on GitHub.