## 🚀 Installation

This project uses [`uv`](https://github.com/astral-sh/uv) — a fast Python package manager compatible with `pyproject.toml`. As well as this project helps to register and create events.

### Prerequisites
- Clone git repository
```bash
git clone https://github.com/qwertyllionman/Event-Booking/tree/master
```
- Install uv if not exist.
```bash
pip install uv
```
- Install dependencies with uv.
```bash
uv pip install pyproject.toml
```
- Migrate database, inside the project there is a Makefile to make migrations easier.
```bash
make migration
```
- Finally run django project!
```bash
make runserver
```
After runnning the project add /docs to the url for opening swagger.
## 🛠️ Technologies Used

- Python 3.12
- [uv](https://github.com/astral-sh/uv) – Fast Python package manager
- [Django Rest Framework](https://www.django-rest-framework.org/) – Rest Framework
- [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Authentication
- [Swagger](https://github.com/tfranzel/drf-spectacular) - Swagger user interface

## 📘 API Endpoints

### `POST /api/token/`

- **Description:** Create token for authentication.
- **Note:** Before creating token. User should be exist. 
- **Response:**
  - `200 OK` – Returns a JSON.
#### Example Request:
```json
{
  "username": "string",
  "password": "string"
}
```
#### Example Response:
```json
{
  "access": "string",
  "refresh": "string"
}
```


### `POST /api/v1/event/create`

- **Description:** Create event.
- **Response:**
  - `201 OK` – Returns a JSON.
#### Example Request:
```json
{
  "title": "string",
  "description": "string",
  "date": "2025-08-07",
  "location": "string",
  "organizer_id": 2
}
```
#### Example Response:
```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "date": "2025-08-07",
  "location": "string",
  "organizer_id": 0
}
```
### `GET /api/v1/event/list`

- **Description:** Retrieve a list of all events belong to the user.
- **Response:**
  - `200 OK` – Returns a JSON array of events.

#### Example Response:
```json
[
  {
    "id": 0,
    "title": "string",
    "description": "string",
    "date": "2025-08-07",
    "location": "string",
    "organizer_id": 0
  }
]
```
### `POST /api/v1/registration/create`

- **Description:** Create a registration.
- **Response:**
  - `201 OK` – Returns a JSON.

#### Example Request:
```json
{
  "user": 0,
  "event": 0
}
```
#### Example Response:
```json
{
  "id": 0,
  "registered_at": "2025-08-07T08:25:02.501Z",
  "user": 0,
  "event": 0
}
```
### `GET /api/v1/registration/list`

- **Description:** Retrieve a list of all registrations belong to the user.
- **Response:**
  - `200 OK` – Returns a JSON array of registrations.

#### Example Response:
```json
[
  {
    "id": 0,
    "registered_at": "2025-08-07T08:27:27.009Z",
    "user": 0,
    "event": 0
  }
]
```
You can practice this in swagger.





