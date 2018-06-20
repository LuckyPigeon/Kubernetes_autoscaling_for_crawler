FROM selenium/standalone-chrome
COPY . /function
WORKDIR /function
RUN sudo apt-get update \
    && sudo apt-get -y install python3-pip
RUN pip3 install -r requirements.txt
ENV CRAWLER_HOST=mysql
ENV CRAWLER_USER=root
ENV CRAWLER_PASSWORD=password
EXPOSE 5000
CMD python3 function.py
