# MAChanger
A Simple Python script to change your MAC address to specify a new one.

## Installation
```
git clone https://github.com/ozXsasson/MAChanger
cd MAChanger
```

## Usage
```
Usage: MAChanger.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
```

## Example
```
python2 MAChanger.py --interface eth0 --mac 00:34:12:78:9a:bc
