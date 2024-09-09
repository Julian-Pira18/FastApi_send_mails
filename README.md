# Email Management Project

This project manages the sending of emails to students based on events and courses. It uses FastAPI for the backend and PostgreSQL as the database.

## Requirements

- **Docker**
- **Python 3.8** or higher
- Python dependencies specified in `requirements.txt`

## Setting Up the Database with Docker

To set up the PostgreSQL database using Docker, run the following command:

```bash
docker run -d \
  --name emails_db_container \
  -e POSTGRES_DB=emails_db \
  -e POSTGRES_PASSWORD=password_emails \
  -e POSTGRES_USER=emails \
  -p 5432:5432 \
  postgres:16-alpine