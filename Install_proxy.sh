#!/bin/bash

echo "Install pip..."
sudo apt update
sudo apt install -y python3-pip

echo "Installing the necessary libraries..."
pip install sleekxmpp aiortc opencv-python
if [ $? -ne 0 ]; then
    echo "Error installing libraries. Please check your pip settings and internet connection."
    exit 1
fi
echo "Create the module_proxy.service service..."
sudo tee /etc/systemd/system/module_proxy.service > /dev/null << EOL
[Unit]
Description=Module Proxy Service
After=network.target

[Service]
ExecStart=/usr/local/lib/module_proxy.py
ExecReload=/bin/kill -HUP \$MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOL

echo "Activate and start the module_proxy.service service..."
sudo systemctl daemon-reload
sudo systemctl enable module_proxy.service
sudo systemctl start module_proxy.service
