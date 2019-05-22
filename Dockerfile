FROM python:3.7-alpine

# create work_dir
WORKDIR /hellopy/flaskwebapp

#copy model list file to docker directory
COPY requirements.txt ./

#install  python depend
RUN pip install -r requirements.txt

