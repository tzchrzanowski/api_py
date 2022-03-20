# running project on cmd

# 1. create local virtual environment for python: use any name you lake in place of env3" 
		py -m venv env3

# 2. activate local virtual environment
		env3\Scripts\activate

# 3. install required libraries locally:
		pip install -r requirements.txt
        OR
		pip install flask
		pip install flask-restful
		pip install httpie
		pip install python-dotenv

# 4. run app locally either using flask or directly from app.py :
   		set FLASK_APP=app.py
		flask run
    OR
        python app.py

# --------------------------
#       testing API :

# 1. Test using httpie, in cmd type:
# POST request:
    http POST localhost:5000/movies title="The Batman" year="2022" description="New take on Batman"

# GET request:
    http GET localhost:5000/movies

# 2. Test using postman:
# POST request:
    url = http://localhost:5000/movies
    Body json:
{
     "title": "Title of movie",
     "year": 2022,
     "description": "description..."
}

# GET request
    url = http://localhost:5000/movies
