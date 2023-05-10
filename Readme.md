

# Project Details -  instructions to run and test the application.

## Prerequisites

* Node.js (v14 or higher)
* Python (v3 or higher)

## Installation

1. Clone the repository `https://github.com/lidasusansabu13/SE577-Project.git`
2. Checkout to `proj-release-2` branch
3. Navigate to the `server` directory and run `pip install -r requirements.txt` to install the necessary dependencies for the backend
4. Navigate to the `github-web-service` directory and run `yarn` to install the necessary dependencies for the frontend

## Usage

1. Navigate to the `server` directory and run `python app.py` or `python3 app.py`to start backend server
2. To check if the server is running open your web browser and navigate to `http://localhost:8080/` to see the message 'Server is working....'
3. In a separate terminal window, navigate to the `github-web-service` directory and run `yarn dev` to start the frontend development server
4. Open your web browser and navigate to `http://localhost:8080/repositories` to get all repositories data
5. Open your web browser and navigate to Vue.js app
6. The Projects page in the Vue.js app displays the list of Repositories. Should I change the name of the page to Repositories from Projects?

## Features

* Feature 1: Under `/repositories` page, to get all repositories data


## API Endpoints

*  `http://localhost:8080/repositories`: Get all repositories data.


## Technologies Used

* Vue.js
* Python Flask

## Highlevel architecture diagram
![Highlevel architecture diagram][def]

[def]: https://github.com/lidasusansabu13/SE577-Project/blob/proj-Release-2/GitManagerArchitecture.jpg