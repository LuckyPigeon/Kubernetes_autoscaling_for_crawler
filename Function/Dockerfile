FROM ubuntu
COPY ./function.py ./function
WORKDIR /function
RUN apt-get update
RUN pip3 install selenium
RUN pip3 install bs4
EXPOSE 3000
CMD python3 function.py LSA.txt
