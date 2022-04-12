#!/bin/bash

# Create media directory
sudo mkdir /media/sleep_media
sudo chown $USER:$USER /media/sleep_media

# Install service
sudo cp sleep_player.service /lib/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable sleep_player.service 
sudo systemctl start sleep_player.service 
