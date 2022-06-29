FROM python:3.8

# Create the working directory
RUN set -ex && mkdir /challenge
WORKDIR /challenge

# Install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the relevant directories
COPY . .

# Run the web server
EXPOSE 8000
ENV PYTHONPATH /challenge
CMD python3 /challenge/app.py
