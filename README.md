# sunrise
![alt text][logo]

Simple script to drive DMX led strip to mimic daily sunrise



## Installation

- install [libfdti](https://www.intra2net.com/en/developer/libftdi/)
- install dmx485

```
pip install dmx485
```
## Hardware

This script assumes a DMX device at address 1, with channel order R,G,B,W.

## Running

Set the clock correctly, esp if using Raspberry Pi which might have lost track of the time.

Then run the script at the command line

```
python3 sunrise.py
```

[logo]: ./img/logo.png "sunrise logo"


