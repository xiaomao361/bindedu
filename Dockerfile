FROM python:3.7

LABEL MAINTAINER="zhouwei" email='xiaomao361@163.com'

WORKDIR /home

ADD requirements.txt /home/
RUN pip install -r requirements.txt
ADD timechick /home/timechick
ADD bindedu /home/bindedu
ADD manage.py /home/manage.py
ADD db.sqlite3 /home/
ADD static /home/static

ADD entrypoint.sh /usr/bin/entrypoint.sh

EXPOSE 8000

CMD ["entrypoint.sh"]
