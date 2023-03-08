# starting  from python image
FROM python
# create app directory
WORKDIR /app
COPY python.py .
#installing flask
RUN pip install flask
EXPOSE 81
CMD python /app/python.py