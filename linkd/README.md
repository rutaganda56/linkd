# LINKD CLI

A developer research CLI tool that aggregates search results from multiple platforms in one place.

## Overview

**LINKD CLI** is a command-line interface designed to help developers quickly search and gather information from GitHub, Reddit, and Stack Overflow without switching between multiple tabs and websites.

## Features

### Working Features ✅

- **GitHub Repository Search** - Search and retrieve the top GitHub repositories for any topic with clone URLs
- **Reddit Posts Search** - Find relevant discussions and posts from Reddit communities
- **Stack Overflow Solutions** - Get popular Stack Overflow answers sorted by votes for technical questions

### Upcoming Features 🚀

- Hacker News integration (coming soon)

## What It Does

When you run a search for a topic, LINKD CLI:

1. Queries **GitHub** and retrieves the top 3 repositories with their names and clone URLs
2. Searches **Reddit** and displays the 5 most relevant posts with titles and discussion links
3. Fetches **Stack Overflow** solutions sorted by popularity to help you find answers fast

All results are displayed in clean, formatted tables for easy reading.

## Tech Stack

- **Language**: Python
- **CLI Framework**: Rich (for beautiful terminal formatting)
- **APIs**: GitHub API, Reddit API, Stack Overflow API

## Author

**Rutaganda Valentin (RUTA)**  
Version: 1.0.0

## Installation & Usage

```bash
python3 main.py
```

Then enter a topic to search across all platforms.

## Requirements

- Python 3.x
- requests library
- rich library

## Error Handling

The CLI handles network errors gracefully and returns informative error messages if API calls fail.
