#!/usr/bin/env bash
# Configure your Nginx server

if [ ! -x /usr/sbin/nginx ];
then
    apt-get -y update
    apt-get -y install nginx
    ufw allow  'Nginx HTTP' #on port 80
    service nginx restart
else

    service nginx restart
fi
mkdir -p /data/web_static/releases/test
touch  /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html
mkdir -p /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu data
sudo sed -i "5i rewrite \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;/\n\t}" /etc/nginx/sites-available/default
