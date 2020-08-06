FROM python:3.8-alpine

LABEL Author="Gean Ivamoto"
LABEL E-mail="geanyoshio@gmail.com"
LABEL version="1.0.0"

ENV PYTHONPATH "/magicnumber"

WORKDIR /magicnumber

COPY bin ./bin
COPY datasets ./datasets
COPY magicnumber ./magicnumber
COPY tests tests
COPY pytest.ini .
COPY requirements.txt .
COPY tox.ini .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/magicnumber/bin/calcmagicnumber.py"]