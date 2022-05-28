FROM python:3.8-slim-buster  

# set work directory  
RUN mkdir -p webapp  

# where your code lives  
WORKDIR /webapp  

# copy whole project to your docker working directory. 
COPY . .

# install dependencies  
RUN pip install --upgrade pip  
# run this command to install all dependencies  
RUN pip install -r requirements.txt

# start server  
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]