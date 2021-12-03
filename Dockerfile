FROM python:3.8


# Download wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh


# Add entry point script
COPY ./entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh


# Install pip modules
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt


# Add django source code
COPY ./deufood /app/deufood/
COPY ./users /app/users/
COPY ./foods /app/foods/
COPY ./articles /app/articles/

COPY ./manage.py /app/


# Set up environment variable
ENV PYTHONUNBUFFERED=0


# Set entry point
CMD ["bash", "-c", "./entrypoint.sh"]