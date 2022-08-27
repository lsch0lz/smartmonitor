FROM python:3.8
RUN mkdir -p data
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run"]
CMD ["Login.py"]