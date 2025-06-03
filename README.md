# GitHub Analytics Dashboard
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-red)
![Status](https://img.shields.io/badge/status-WIP-yellow)

This project analyzes and visualizes traffic and engagement data from my GitHub profile and repositories. 

Using GitHub's REST API, it automatically collects metrics like views, clones, stars, and forks. A Streamlit dashboard displays trends over time, offering insights into how my GitHub presence evolves, especially during job hunting and open-source contributions.

### 🔍 Features
- Fetches GitHub traffic data (views, clones) from the GitHub API
- Tracks stars, forks, and watchers across multiple repos
- Stores data in CSV or SQLite for historical trend analysis
- Streamlit dashboard to visualize activity over time
- (Planned) Automation with GitHub Actions to pull daily data

### 📸 Dashboard Preview

![screenshot](images/dashboard_preview.png)

### 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/github-analytics-dashboard.git
   cd github-analytics-dashboard
2. **Install dependencies**
    pip install -r requirements.txt
3. **Set up environment variables**
   **GITHUB_TOKEN=your_token_here**
4. Run the dashboard 
   **streamlit run dashboard/app.py**

5. ⚙️ Tech Stack
   - Python 🐍
   - GitHub REST API
   - Streamlit 📊
   - SQLite / CSV for storage
   - GitHub Actions (optional, for automation)

