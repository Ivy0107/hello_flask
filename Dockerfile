FROM python:3.11.3
WORKDIR /HELLO_FLASK  
ADD . /HELLO_FLASK
RUN pip install -r requirements.txt
EXPOSE 5000  
CMD ["python", "app.py"]  