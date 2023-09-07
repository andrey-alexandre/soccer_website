# base image  
FROM python:3.8   
# setup environment variable  
ENV DOCKERHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DOCKERHOME  

# where your code lives  
WORKDIR $DOCKERHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DOCKERHOME 

# copy AUTH JSON for Google Drive
COPY Soccer.json $DOCKERHOME 

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# port where the Django app runs  
EXPOSE 8000  
# start server
# CMD python soccer/manage.py runserver 0.0.0.0:8000
# CMD ["python", "soccer/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["soccer/manage.py", "runserver", "0.0.0.0:8000"]
