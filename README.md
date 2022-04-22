This repository will be useful to scrap YouTube comments

# Backend setup (go to python-backend directory)

1) Create virtual environment: py -m venv env

2) Start virtual environment: .\env\Scripts\activate

3) Run: pip install pipreqs

4) pip install -r requirements.txt

5) Put your google API key inside .env file

6) Run: set FLASK_APP=api.py

7) Run: flask run (This will start flask server on http://127.0.0.1:5000/)


# Frontend setup (go to react-frontend directory)

1) Run: npm install

2) Run: npm start (This will start react app on http://localhost:3000/)


# Scrap YouTube comments

1) Enter YouTube video URL in URL field and click on submit

2) Check scraped comments inside python-backend/data directory
