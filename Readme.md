

# Project Details -  instructions to run and test the application.

## Prerequisites

* Node.js (v14 or higher)
* Python (v3 or higher)

## Installation and usage

1. Clone the repository `https://github.com/lidasusansabu13/SE577-Project.git`
2. Navigate to the cloned repo using the command `cd SE577-Project`
3. Type the command `git pull` to get all latest updates.
4. Type the command `git checkout proj-Release-3` to switch  to `proj-Release-3` branch
5. If you run the `ls` command you can see the folder structure:
```
├── Server
│
├── client
│
├── GitManagerArchitecture.jpg
│
└── Readme.md
```
6. Make sure you have Python 3.x installed you can use these commanda `$ sudo apt-get update
$ sudo apt-get install python3.6`
7. You can make use of a virtual envirnment to avoid installation issues `python3 -m venv se577venv ` and activate it by using the command `source bin/activate  ` after moving to the directory using `cd se577venv` after that `cd ..` 

8. Navigate to the `Server` directory and run `pip install -r requirements.txt` to install the necessary dependencies for the backend
9. Create a `.env` file and copy paste the appropriate envirnment variables example :
`GH_ACCESS_TOKEN=your_github_access_token
GH_API_URL=https://api.github.com/`
10. Open a terminal and run `python app.py` or `python3 app.py`to start backend server
11. To check if the server is running open your web browser and navigate to `http://localhost:8080/` to see the message 'Server is working....'
12. Open your web browser and navigate to `http://localhost:8080/repositories` to get all repositories data
13. Navigate to the `client` directory in a seperate terminal and run `yarn` to install the necessary dependencies for the frontend
14.  run `yarn dev` to start the frontend development server and it will open in `http://localhost:5173/`
15. navigate to `http://localhost:5173/projects` to see the list of repositories.



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