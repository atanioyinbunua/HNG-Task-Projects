# HNG stage zero Task

A simple Flask-based API endpoint that returns your user information, the current timestamp, and a random cat fact fetched from the [Cat Facts API](https://catfact.ninja/fact).

---

## Features

- Returns basic user info (name, email, stack)
- Includes the current local timestamp (ISO format)
- Fetches a random cat fact from an external API
- Returns all data as JSON

---

## API Endpoint

### **GET `/me`**

**Response Example:**

```json
{
  "status": "success",
  "user": {
    "email": "oyinbunuaatani@gmail.com",
    "name": "Atani Oyinbunua",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-19T10:43:12.123456",
  "fact": "Cats can jump up to six times their length."
}
```

# Setup Instructions

Follow these steps to run the API endpoints locally.

---

### Clone this repository

```bash
git clone https://github.com/atanioyinbunua/HNG-Task-Projects.git
cd stage-0
```

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
flask --app run run
```
