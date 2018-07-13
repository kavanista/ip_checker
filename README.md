# Webserver version checker
 

## Installation

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
ip_checker.py [-h] [-f FILE] [-i IPS]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing IP Addresses to check
  -i IPS, --ips IPS     IP's passed as comma-separated list
```
## Testing
```
nosetests tests.py
```
