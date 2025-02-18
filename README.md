## Setup Instructions

1. Install Astral UV if not installed.
2. Set up the container:
    ```sh
    sudo docker compose up -d
    ```
3. Run migrations:
    ```sh
    uv run manage.py migrate
    ```
4. Start the server:
    ```sh
    uv run manage.py runserver
    ```
    