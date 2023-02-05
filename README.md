# databeats_task



1. Create a virtual environment
2. Install the packages from the requirements.txt file
   
   command:
   pip install -r requirements.txt

3. Database Used is default sqlite3 database


4. After installation of all the packages create tables 
  commands: python manage.py makemigrations
            python manage.py migrate 


5 Tables created in the database
6. Use POst man to run the below API's




Register User API


===================


url-method -Post
===

http://localhost:8000/register/user/


Payload data
============

{
    "username":"ravi kumar",
    "password":"ravi123@@",
    "confirm_password":"ravi123@@",
    "email":"ravikumar45@gmail.com"

}









Login User API:

================




    Url method==POSt
    ==================

    http://localhost:8000/user/login/





     payload data
    ==============


    {
        "username":"Uday kumar",
        "password":"uday123@@"
    }






     Response
     ========

   {
      "message": "User Logged in successfully",
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IlVkYXkga3VtYXIiLCJleHAiOjE2NzU2NzMxNzQsImVtYWlsIjoidWRheWt1bWFyYW5kb2x1QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjc1NTg2Nzc0fQ.CTy7GOcopApojKrnkYi8_gTajGFz3wgkMNzdF6bPzdo"
    }





Part B
=======


After the user login in copy the JWT Token and  Use in the  Movie and Cast API's


Create A Movie
============

	URl method -POST :
	===================
 			
      http://localhost:8000/create/movie/

    

     payload data:
     =============

       {
        "title":"Dasara",
        "runtime":3,
        "language":"Telugu,Hindi, English",
        "tagline":"Movie is about fighting for the rights of the people"
        }


     
    Response
    ===========


       {
    		"id": 6,
    		"title": "Dasara",
    		"created_at": "2023-02-05T17:17:46.116732",
    		"updated_at": "2023-02-05T17:17:46.116732",
    		"runtime": 3,
    		"language": "Telugu,Hindi,Englist",
    		"tagline": "Movie is about fighting for the rights of the people",
    		"casts": []
  	}



Create A Cast of the Movie
===========================


     URl Method -- POST
     ==================
     
       http://localhost:8000/create/cast/


     
    Payload Data:
    ===============

        {
 		   "movie":6,
    		   "name":"Nani",
    		   "gender":"M",
    		   "dob":"1987-02-24"
		} 


    Response
    =========



      {
       "id": 8,
       "name": "Nani",
       "gender": "M",
       "dob": "1987-02-24",
        "movie": 6
      }


List of movies
===============


    URL method --GET

   ====================


    http://localhost:8000/movies/

  
   Response:
   ==========

     [
    {
        "id": 1,
        "title": "Bahubali",
        "created_at": "2023-02-05T12:49:04.576122",
        "updated_at": "2023-02-05T12:49:04.576122",
        "runtime": 24,
        "language": "Telugu",
        "tagline": "terere",
        "casts": [
            {
                "id": 3,
                "name": "Prabhas",
                "gender": "M",
                "dob": "1985-10-23",
                "movie": 1
            },
            {
                "id": 4,
                "name": "Anushka shetty",
                "gender": "F",
                "dob": "1989-01-23",
                "movie": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "dhamaka",
        "created_at": "2023-02-05T13:05:30.075259",
        "updated_at": "2023-02-05T13:05:30.075259",
        "runtime": 24,
        "language": "Telugu",
        "tagline": "mass performance",
        "casts": [
            {
                "id": 5,
                "name": "Ravi Teja",
                "gender": "M",
                "dob": "1972-11-10",
                "movie": 2
            },
            {
                "id": 6,
                "name": "sree leela",
                "gender": "F",
                "dob": "1992-01-16",
                "movie": 2
            }
        ]
    },
    {
        "id": 3,
        "title": "Varis",
        "created_at": "2023-02-05T13:51:30.179684",
        "updated_at": "2023-02-05T13:51:30.179684",
        "runtime": 24,
        "language": "Telugu,Hindi",
        "tagline": "fight erukum, Dance erukum",
        "casts": [
            {
                "id": 7,
                "name": "Vijay thalapathy",
                "gender": "M",
                "dob": "1975-01-16",
                "movie": 3
            }
        ]
    },
    {
        "id": 4,
        "title": "Hari hari vera mallu",
        "created_at": "2023-02-05T14:18:10.199428",
        "updated_at": "2023-02-05T14:18:10.199428",
        "runtime": 24,
        "language": "Telugu,Hindi",
        "tagline": "pavan star movie",
        "casts": []
    },
    {
        "id": 5,
        "title": "kgf",
        "created_at": "2023-02-05T14:19:06.104913",
        "updated_at": "2023-02-05T14:19:06.104913",
        "runtime": 24,
        "language": "Telugu,Hindi",
        "tagline": "kgf movie",
        "casts": [
            {
                "id": 1,
                "name": "Yash",
                "gender": "M",
                "dob": "1996-02-25",
                "movie": 5
            },
            {
                "id": 2,
                "name": "Radhika pandit",
                "gender": "F",
                "dob": "1996-07-08",
                "movie": 5
            }
        ]
    },
    {
        "id": 6,
        "title": "Dasara",
        "created_at": "2023-02-05T17:17:46.116732",
        "updated_at": "2023-02-05T17:17:46.116732",
        "runtime": 3,
        "language": "Telugu,Hindi,Englist",
        "tagline": "Movie is about fighting for the rights of the people",
        "casts": [
            {
                "id": 8,
                "name": "Nani",
                "gender": "M",
                "dob": "1987-02-24",
                "movie": 6
            }
        ]
    }
]




TO get the details of movie using movie id


================================================




URl method--- GET:

======================

  http://localhost:8000/movie/6/


 Response:

=============

{
    "id": 6,
    "title": "Dasara",
    "created_at": "2023-02-05T17:17:46.116732",
    "updated_at": "2023-02-05T17:17:46.116732",
    "runtime": 3,
    "language": "Telugu,Hindi,Englist",
    "tagline": "Movie is about fighting for the rights of the people",
    "casts": [
        {
            "id": 8,
            "name": "Nani",
            "gender": "M",
            "dob": "1987-02-24",
            "movie": 6
        }
    ]
}





Part C
=============


question:

Bonus: If we want to extend our database to incorporate tv shows, what additions would you do
for the existing application.



Answer

===========



 In the Existing application if we want to extend our database to incoperate tv shows

 I will create a Choice field ie type  in the movies Model table

      Choice_Type=(

     ('Movies','Movies'),
     ('TV Shows','Tv Shows')
      )  

      type=models.CharField(max_length=30,choices=Choice_Type)

   
  Using this we dont need to create a seperate model or table to TV shows we can reuse the existing MoviesModel

   1.   if we are adding the movie details we will select the type movies 
   2.   if we are adding the Tv show details we will select Tv shows from the choice



   When we are retrieving the data based on the Type we can differentate the data


     












       
     



