## Setup Instructions

1. Set up the `.env` file from `.env-sample`.

### Generate an EMAIL_HOST_PASSWORD Password:

1. Enable 2-Step Verification on your Google Account.
2. Navigate to Security > App Passwords.
3. Generate a password for the app (e.g., "Mail").
4. Copy the generated 16-character password (e.g., abcd efgh ijkl mnop).
5. Use this password as `EMAIL_HOST_PASSWORD`.

*Please use a valid email for this setup.*
### Installation Steps:

1. Install Astral UV if not installed.
2. Set up the container:
    ```sh
    docker compose up -d
    ```
3. Run migrations:
    ```sh
    uv run manage.py migrate
    ```
4. Create an admin user:
    ```sh
    uv run manage.py createsuperuser
    ```
5. Start the server:
    ```sh
    uv run manage.py runserver
    ```

### API-Setup Instructions:

1. Open Postman.
2. Import the task-management collection.
3. Use the admin email and password created with the `createsuperuser` command.
4. Run the collections.

## Completed Functionality

1. The API has the following endpoints:
    - `POST /tasks`: Create a new task (title, description, status, assigned user).
    - `GET /tasks`: Retrieve all tasks.
    - `GET /tasks/:id`: Retrieve a specific task by ID.
    - `PUT /tasks/:id`: Update a task's details.
    - `DELETE /tasks/:id`: Delete a task.
2. Uses JSON format for data exchange and ensures proper validation and error handling.

### Task 2: Database Management

1. Uses a database to store tasks and user data.
2. Each task has a title, description, status (To-Do, In Progress, Done), created_at timestamp, and assigned user.
3. Queries are optimized for efficient data retrieval.

### Task 3: Authentication & User Management

1. Implements user authentication (JWT, OAuth, or session-based).
2. Users can register and log in.
3. Implements role-based access control (Admin can manage all tasks, users can only update their own tasks).

### Task 4: Extra Features (Optional)

1. Implements task assignment notifications (email or in-app alerts).
2. Adds task priority levels (Low, Medium, High).
