# Zoo Management API

This is a Flask-based RESTful API for managing a zoo. It provides endpoints for managing animals and employees in the zoo.

## Features

- Animal Management: Add, update, delete, and retrieve information about animals in the zoo.
- Employee Management: Manage staff working at the zoo, including their roles and schedules.

## Installation

1. Clone the repository:

   ```bash

   git clone https://github.com/your-username/zoo-management-api.git
   cd zoo-management-api

2. Install dependencies:

```pip install -r requirements.txt```

3.Run the application:

```python app.py```

## API Endpoints

GET /api/animals: Retrieve all animals

URL: `http://your-api-url.com/api/animals`

GET /api/animals/{id}: Retrieve a specific animal

URL: `http://your-api-url.com/api/animals/1`

POST /api/animals: Add a new animal

URL: `http://your-api-url.com/api/animals`

Body (raw JSON)

{
  "species": "Lion",
  "name": "Simba",
  "age": 5,
  "gender": "Male",
  "special_requirements": "Carnivore diet, large enclosure"
}

PUT /api/animals/{id}: Update an existing animal

URL: `http://your-api-url.com/api/animals/1`
Body (raw JSON)

{
  "species": "Lion",
  "name": "Simba",
  "age": 6,
  "gender": "Male",
  "special_requirements": "Carnivore diet, large enclosure, regular health check-ups"
}

DELETE /api/animals/{id}: Delete an animal

URL: `http://your-api-url.com/api/animals/1`

### Employees

GET /api/employees: Retrieve all employees

URL: `http://your-api-url.com/api/employees`
GET /api/employees/{id}: Retrieve a specific employee

URL: `http://your-api-url.com/api/employees/1`
POST /api/employees: Add a new employee

URL: `http://your-api-url.com/api/employees`
Body (raw JSON)

{
  "name": "Doe Whot",
  "email": "doe.whot@zoo.com",
  "phone": "+1234567890",
  "role": "Zookeeper",
  "schedule": "Monday to Friday, 9 AM - 5 PM"

}

## PUT /api/employees/{id}: Update an existing employee

URL: ```http://your-api-url.com/api/employees/1```
Body (raw JSON)

{
  "name": "John Doe",
  "email": john.doe@zoo.com,
  "phone": "+1234567890",
  "role": "Senior Zookeeper",
  "schedule": "Monday to Friday, 8 AM - 4 PM"
}

DELETE /api/employees/{id}: Delete an employee

URL: `http://your-api-url.com/api/employees/1`

## Docker

To build and run the application using Docker:

1. Build the Docker image:

`docker build -t zoo-management-api .`

2.Run the Docker container:

`docker run -p 5000:5000 zoo-management-api

