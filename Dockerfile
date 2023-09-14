FROM python:3.10.0-alpine
WORKDIR /abc
COPY . /abc/
RUN python3 -m pip install -r requirment.txt


EXPOSE 5000
CMD python flaskmongo/run.py


