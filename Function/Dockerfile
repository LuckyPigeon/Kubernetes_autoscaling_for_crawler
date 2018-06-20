FROM ubuntu
COPY . /function
WORKDIR /function
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get update
RUN pip3 install -r requirements.txt
ENV CRAWLER_HOST=mysql
ENV CRAWLER_USER=root
ENV CRAWLER_PASSWORD=password
EXPOSE 3000
CMD python3 functioon.py
