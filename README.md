# pyjrm (Python JSON Resource Monitor)

## Overview: 
pyjrm uses psutil to record a variety of information at a given time interval and saves it to a JSON file. 


## Usage:

1. Run `main.py`.
2. When prompted, enter a process name. For example, `chrome.exe`.
3. When prompted, specify how often, in seconds, data is collected. For example, `10`.
4. When prompted, specify how long, in seconds, data is collected.  For example, `60`.

In the above example, `main.py` will collect information on a process with the name `chrome.exe` every `10` seconds for `60` seconds. 


## Process data collected:


## JSON Formatting:
See `data/example.json`.


## Motivation: 
I needed a way to record resource usage of a specifc application over a given period of time to process later, so I made this.