# Contact API Script

The Contact API script is a Python application that opens a port and accepts GET and POST requests to collect contact information. It utilizes Flask and Telegram to handle the requests and send notifications.

## Prerequisites

- Python 3.7 or higher
- Docker (if running in a Docker container)

## Getting Started

1. Clone the repository:

```
    git clone https://github.com/your-username  contact-api.git
    cd contact-api
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

Create a config.txt file and add your Telegram bot token and chat ID:

```
BOT_TOKEN=<your-bot-token>
CHAT_ID=<your-chat-id>
```

# Running the Script
## Local Development
To run the script locally, execute the following command:

```
python app.py
```

The script will start a Flask development server and listen on *http://localhost:5000*

## Docker
To run the script in a Docker container, follow these steps:

1 Build the Docker image:

```
docker build -t contact-api .
```

2. Run the Docker container:

```
docker run -p 5000:5000 --env-file config.txt contact-api
```

Replace config.txt with the path to your configuration file if it's not in the current directory.

The script is now running inside a Docker container and accessible at *http://localhost:5000*

# Usage
## Sending a POST Request
To send contact information via a POST request, use the following endpoint:
- *URL*: http://localhost:5000/
- *Method*: POST
- *Form data*:
    - name: (string) The name of the contact.
    - email: (string) The email address of the contact.
    - subject: (string) The subject of the message.
    - message: (string) The message content.

Example curl command:
```
curl -X POST -F "name=John Doe" -F "email=john@example.com" -F "subject=Hello" -F "message=This is a test message." http://localhost:5000/
```

## Health Check
To perform a health check, send a GET request to the /health endpoint:
- *URL*: http://localhost:5000/health
- *Method*: GET

Example curl command:
```
curl http://localhost:5000/health
```