FROM selenium/standalone-chrome
COPY . /function
WORKDIR /function
RUN sudo apt-get update \
    && sudo apt-get -y install python3-pip
RUN pip3 install -r requirements.txt
ENV CRAWLER_HOST=mysql
ENV CRAWLER_USER=root
ENV CRAWLER_PASSWORD=password
<<<<<<< HEAD
EXPOSE 5000
CMD python3 function.py
=======
EXPOSE 3000
CMD python3 functioon.py
>>>>>>> 456c6ba3265dfb2db1c2dd3695f9d52e6dda48de
