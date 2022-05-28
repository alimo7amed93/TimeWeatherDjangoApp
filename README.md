# TimeWeatherDjangoApp

### Install Django in a new Venv and activate it
  **pipenv install django**

### Install the reuired dependencies in check-me


### I used OpenWeatherAPI form openweathermap.org 
  They offer free service tier with limiter No. of calls per min, make sure to
  get and update the API key in the project

![Screenshot](https://github.com/alimo7amed93/TimeWeatherDjangoApp/blob/main/Images/OpenWeatherAPI.png)

### OpenWeatherAPI Time Conversiton
  OpenWeatherAPI returns time in UTC timestamp along with the time-zone of the required city 
  so I had to use datetime package for conversion and readability

![Screenshot](https://github.com/alimo7amed93/TimeWeatherDjangoApp/blob/main/Images/Datetime.png)


### Dockerizing the project
  install **Docker** in your machine.

  Run: **pip freeze > requirements.txt**
  in order to capture the required dependencies for the project.

  Run: **docker build -t time-weather-app .**
  in order to build an image -Check the docker file I attached for the required build details-
![Screenshot](https://github.com/alimo7amed93/TimeWeatherDjangoApp/blob/main/Images/DockerImage.png)

  Run: **docker run -dp 8000:8000 time-weather-app**
  in order to run the built image.
![Screenshot](https://github.com/alimo7amed93/TimeWeatherDjangoApp/blob/main/Images/DockerRunImage.png)

### The app should be running in localhost:8000
![Screenshot](https://github.com/alimo7amed93/TimeWeatherDjangoApp/blob/main/Images/RunningApp.png)


