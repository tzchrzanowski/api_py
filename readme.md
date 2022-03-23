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

# GET single item with known id request:
# GET request:
    http GET localhost:5000/movies/1


# 2. Test using postman:
# POST request:
    url = http://localhost:5000/movies
    Body json:
{
     "title": "Title of movie",
     "year": 2022,
     "description": "description..."
}

# PUT request: 
    url example = http://localhost:5000/movies/1
    Body json: 
{
     "title": "1111",
     "year": 1111,
     "description": "1 1 1 1 1 1 1"
}