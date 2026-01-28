# URL Shortener CLI --- MVC Python Project

A clean, backend-style **URL Shortener Service** built using **Python
and MVC architecture**.\
This project mimics the core logic behind services like **bit.ly /
tinyurl**, implemented as a command-line application.

Designed specifically for: - Portfolio projects - Clean Git commit
history - MVC architecture practice - Interview preparation

------------------------------------------------------------------------

## Features

-   Create short URLs\
-   Resolve short URLs\
-   Track click analytics\
-   View all stored URLs\
-   Delete URLs\
-   Save & load data using JSON\
-   Export analytics to CSV

------------------------------------------------------------------------

## Architecture (MVC)

    url_shortener/
    │
    ├── main.py
    │
    ├── controller/
    │   └── url_controller.py
    │
    ├── model/
    │   ├── url_entry.py
    │   └── url_repository.py
    │
    ├── view/
    │   └── url_view.py
    │
    └── storage/
        ├── json_storage.py
        └── analytics_exporter.py

------------------------------------------------------------------------

## How It Works

-   **Model:** Stores and manages URL mappings and click analytics\
-   **View:** Handles CLI input and output\
-   **Controller:** Controls application flow and business logic

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/url-shortener-cli.git
cd url-shortener-cli
```

### 2. Run the Application

``` bash
python main.py
```

------------------------------------------------------------------------

## Sample Usage

    1. Create Short URL
    2. Resolve Short URL
    3. Show All URLs
    4. Delete URL
    5. Export Analytics
    6. Save Data
    7. Load Data
    0. Exit

------------------------------------------------------------------------

## Example Output

    Short URL created: Ab3xK9
    Redirects to: https://openai.com

------------------------------------------------------------------------

## Files Generated

-   `urls.json` → Persistent URL storage\
-   `analytics.csv` → Click analytics export

------------------------------------------------------------------------

## Recommended Git Commit Strategy

This project is structured for **40 clean Git commits**, following: -
MVC layers - One method per commit - Clear development progression

------------------------------------------------------------------------

## Technologies Used

-   Python 3.x
-   JSON
-   CSV
-   MVC Architecture

------------------------------------------------------------------------

## Future Improvements

-   REST API version (FastAPI)
-   SQLite database backend
-   Redis caching
-   Web frontend

------------------------------------------------------------------------

## License

MIT License --- free to use and modify.
