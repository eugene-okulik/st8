FROM python
EXPOSE 8080/tcp
ENV MY_PORT=8080
ENV MY_IP=0.0.0.0
RUN mkdir logs
ENV MY_LOG=logs
RUN mkdir /usr/share/my-app
RUN echo "My docker excersise is started" > /usr/share/my-app/my-app.txt
RUN git clone https://github.com/Hopenot/docker.git
CMD ["python3", "docker/programm.py"]
