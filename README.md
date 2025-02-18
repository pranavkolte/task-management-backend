## Setup Instructions

Generate an EMAIL_HOST_PASSWORD Password:

1. Enable 2-Step Verification on your Google Account.
2. Navigate to Security > App Passwords.
3. Generate a password for the app (e.g., "Mail").
4. Copy the generated 16-character password (e.g., abcd efgh ijkl mnop).
5. Use this password as EMAIL_HOST_PASSWORD.



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
    