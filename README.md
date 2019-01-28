# LogPoint-director-toolset

## Pre-requisites

### Python 2.7

Code is written for python 2.7

### Install required python packages:

(Using a virtualenv is highly recommended)

```
easy_install requests configparser tabulate
```
or
```
pip install requests configparser tabulate
```

Update `config.ini` with API host, API key and ID of Logpoint server

## Examples:

run `./lpapi.py [-h]` for help

**Specify a specific LogPoint host:**

Making a request or update uses the default host in config.ini
If you what to specify the host use: `./lpapi -lph <host of config.ini>`

> **TODO** config.ini snippet here

**Collector**

`./lpapi.py get system -lph lpcol`

**Search head**

`./lpapi.py get system -lph lpsh`

**System**

`./lpapi.py get system`

Update system:
```
/lpapi.py update system -p li_name=lpcol li_ip=10.199.199.115 ha_default_path=/opt/immune/storage/ timestamp_on=col_ts timezone=Europe/Amsterdam overscan_period=10 lp_mode=dlp default_auth=LogpointAuthentication timeout=15 -o json
````

**Repository**

Get repository info:

`./lpapi.py get repo`

Edit repository:

`./lpapi.py edit repo --parameter id=59a992b31fa1ae0e1ee90020 retention=22`

Create repository:
```
./lpapi.py create repo --parameter name=Windows
./lpapi.py create repo --parameter name=Windows retention=36
./lpapi.py create repo --parameter name=Windows retention=36 path=/opt/immune/storage2/

# keep the path/retention in pairs:
./lpapi.py create repo --parameter name=Windows retention=30 path=/opt/immune/storage/ path=/opt/immune/morestorage/ retention=120
```

`./lpapi.py delete repo -p id=59fc31f62a94c726fcefcf4c`

**Device**

Get device info:

`./lpapi.py get device`

Create device:
```
./lpapi.py create device --parameter name=winserver ip=10.1.1.3
./lpapi.py create device --parameter ip=10.1.1.3 ip=10.1.1.4 name=winserver
```

Edit device:

```
./lpapi.py edit device --parameter ip=10.8.9.9 id=59aa711a1fa1ae103f429795
./lpapi.py edit device --parameter name=winserv01 ip=10.8.9.9 devicegroup=windows devicegroup=printer
```

Delete device:

```
./lpapi.py delete device --parameter name=server03
./lpapi.py delete device --parameter id=59aa711a1fa1ae103f429795
```

Bulk operations using json file import:

```
./lpapi.py create device --file import.json
./lpapi.py edit device --file import.json
./lpapi.py delete device --file import.json
```

**Syslog collector**

`./lpapi.py create syslogcollect -p processpolicy=default name=linuxserver03`

**Devicegroup**

Get devicegroup:

`./lpapi.py get devicegroup`

Create devicegroup:

`./lpapi.py create devicegroup --parameter name=testgrp description=tester`

**Normalization**

Get normalization pack:

`./lpapi.py get normpack`

Get normalization policy:

`./lpapi.py get normpol`

Get process policy:

`./lpapi.py get processpol`

**OpenDoor**

Get opendoor:

`./lpapi.py get opendoor`

Create opendoor:

`./lpapi.py create opendoor -lph lp1 -p network=10.172.100.1 netmask=255.255.255.128 password=oJO0X2IbFeWfk opened=on`

**Distributedlogpoint**

Get distributed logpoint:

`./lpapi.py get dlp`

Create distributed logpoint:

```
./lpapi.py create dlp -p ip_dns=10.199.199.116 private_ip=10.172.100.1 password=oJO0X2IbFeWfk

# or:
./lpapi.py create distributedlogpoint -lph lpcol1 -p ip_dns=10.199.199.116 private_ip=10.172.100.1 password=oJO0X2IbFeWfk
```

**DistributedCollector**

Refresh distributed collector:

`./lpapi.py refresh dcol`

Get distributed collector:

`./lpapi.py get dcol`

Activate distributed collector:

`./lpapi.py activate dcol -p id=5a03715c2a94c7711ed0670b`

**NTP**

Create NTP server(s):

```
./lpapi.py create ntp --parameter ntp_enabled=on ntp_server=10.199.199.2
./lpapi.py create ntp --parameter ntp_server=10.199.199.2 ntp_server=10.199.199.3

# restart NTP service:
./lpapi.py restart ntp
```

**SupportConnection**

Get supportconnection:

`./lpapi.py get supportconnection`

Create support connection:

```
./lpapi.py create support -p support_connection=on connection_forever=true
# or with time limit:
./lpapi.py create support -p support_connection=on enable_hours=0 enable_days=1 enable_minutes=0
```

Refresh support connection:

`./lpapi.py refresh support`

**SSH key**

Get ssh private key:

`./lpapi.py get ssh`

Create new ssh private/public key pair:

`./lpapi.py create ssh -p pass_phrase=QoYjPhfhs8boQ`
