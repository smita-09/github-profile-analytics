import os
from time import sleep
from datetime import datetime

import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

if "GITHUB_TOKEN" in st.secrets:
    TOKEN = st.secrets["GITHUB_TOKEN"]
else:
    # Fall back to local .env (works in local dev)
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {"Authorization": f"token {TOKEN}"}

USERNAME = "smita-09"  # Your GitHub username


def get_public_repos(username):
    print(f"Fetching repos for user: {username}")
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        r = requests.get(url, headers=HEADERS)

        if r.status_code != 200:
            print("Failed to fetch repos:", r.json())
            return repos
        data = r.json()
        if not data:
            break
        for repo in data:
            if not repo["private"] and repo["owner"]["login"] == username:
                repos.append(repo["name"])
        page += 1
    print(f" Found {len(repos)} public repos.")
    return repos


def fetch_views(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}/traffic/views"
    r = requests.get(url, headers=HEADERS)

    if r.status_code in [403]:
        print(f"Failed to fetch data, shows {r.status_code}")
        return pd.DataFrame()

    views = r.json().get("views", [])
    if not views:
        print(f"No views for {repo}")
        return pd.DataFrame()

    df = pd.DataFrame(views)
    df["repo"] = repo
    df["fetched_at"] = datetime.utcnow()
    return df


def main():
    repos = get_public_repos(USERNAME)

    all_data = []

    for repo in repos:
        df = fetch_views(repo)
        if not df.empty:
            all_data.append(df)
        sleep(1)  # Being polite to the GitHub API

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        os.makedirs("data", exist_ok=True)
        final_df.to_csv("data/github_views.csv", index=False)
        print(f"Saved all repo views to data/github_views.csv")
    else:
        print("No view data available.")


if __name__ == "__main__":
    main()
