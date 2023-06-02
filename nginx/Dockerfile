FROM ubuntu

EXPOSE 80

RUN apt -y update && apt -y install nginx

RUN rm -r /etc/nginx/sites-available && rm -r /etc/nginx/sites-enabled

COPY files /

CMD["/usr/sbin/nginx"]