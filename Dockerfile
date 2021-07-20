FROM python:3.8

WORKDIR /src

ADD requirements.txt .
ENV FLASK_APP=models.py

RUN pip install -r requirements.txt

ADD . /src


# RUN export FLASK_APP=models.py && \
#     flask db init && \
#     flask db migrate && \
#     flask db upgrade && \
#     python add.py

# CMD ["bash","-c","flask db init && flask db migrate && flask db upgrade && python collect.py && python views.py"]
CMD ["bash","-c","python views.py"]