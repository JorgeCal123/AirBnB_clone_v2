#!/usr/bin/env bash
# Configure your Nginx server

if [ ! -x /usr/sbin/nginx ];
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo ufw allow  'Nginx HTTP' #on port 80
    sudo service nginx restart
else

    sudo service nginx restart
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
sudo service nginx restart
