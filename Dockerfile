FROM ubuntu:20.04

RUN apt-get update -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3.8 python3-pip git

COPY ./requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY app/ /

WORKDIR app
RUN ls -a && echo khay && pwd
EXPOSE 5000

ENTRYPOINT ["python3","/app.py"]
