# sleep-player

a simple script and service for playing sleep meditations using a raspberry pi and a single pushbutton

## Requirements
uses python-mpv https://github.com/jaseg/python-mpv

`pip install python-mpv`

## Installation

* git clone in your homedir
* edit the init script no need if using "pi" user
* run install.sh to install the service


note: This has not been a super stable system, it tends to need a reboot every few days. 
This is at least partially due to using a full linux system as the platform, and there is likely some garbage collection I'm missing somewhere.
I eventually found that a dedicated sound playing board was a more reliable option, I may document that further later.
Please contact me if you want details.

