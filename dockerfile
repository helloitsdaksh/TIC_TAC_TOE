FROM python:3
ADD XO.py /
RUN pip install numpy pyttsx3==2.7
CMD [ "python", "./XO.py" ]