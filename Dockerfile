FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /system_rt_mgt
WORKDIR /system_rt_mgt
COPY . /system_rt_mgt

RUN pip install -r ./requirements/base.txt

EXPOSE 30303
CMD python3 manage.py runserver 0.0.0.0:30303
