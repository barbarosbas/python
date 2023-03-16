
FROM python:3.11-slim

#set application directory
WORKDIR /myapp


#copy files
COPY lib/. lib/.
COPY main.py .
COPY capture.pcap .
COPY requirements.txt .

#check and install update
RUN apt-get update && apt-get upgrade -y

#install libraries
RUN  pip install --no-cache-dir -r requirements.txt

#  create non-root user to run the application
RUN groupadd -r barbarosgroup && useradd -r -g barbarosgroup barbaros
USER barbaros

CMD ["python","main.py","capture.pcap"]