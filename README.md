# sunrise
![alt text][logo]

Simple script to drive DMX led strip to mimic daily sunrise



## Prerequisites

- install [libfdti](https://www.intra2net.com/en/developer/libftdi/)
- install dmx485

```
pip3 install dmx485
```
## Hardware

This script assumes a DMX device at address 1, with channel order R,G,B,W.

Check the system clock is correct (avoid sunrise at odd time!)

## Installation
```
git clone https://github.com/timdrysdale/sunrise.git
cd sunrise
./demo
```

## Running the daily sunrise
```
./sunrise
```

## Autostarting sunrise
```
sudo su
cp sunrise /usr/bin/
cp sunrise-blank /usr/bin/
cp sunrise-demo /usr/bin/
cp sunrise.service /lib/systemd/system
pip install dmx485
systemctl enable sunrise
systemctl start sunrise
exit
```

 
[logo]: ./img/logo.png "sunrise logo"


