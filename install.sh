#!/bin/bash
sudo mkdir /media/sleep_media
sudo chown `whoami` /media/sleep_media
sudo cp sleep_player.service /lib/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable sleep_player.service 
sudo systemctl start sleep_player.service 
