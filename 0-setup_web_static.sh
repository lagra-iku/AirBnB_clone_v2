#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

if [ ! -d "/data/web_static/releases/test" ]; then
    sudo mkdir -p /data/web_static/releases/test
fi

if [ ! -d "/data/web_static/shared" ]; then
    sudo mkdir -p /data/web_static/shared
fi

echo "<html>
  <head></head>
  <body>
    <h1>Test page for Air_BnB Clone V2 deployment</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership and permissions
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/

CONFIG_BLOCK="location /hbnb_static {\n\talias /data/web_static/current/;\n}"
sudo sed -i "/listen 80 default_server/a $CONFIG_BLOCK" /etc/nginx/sites-enabled/default

sudo service nginx restart
