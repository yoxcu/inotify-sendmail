# inotify-sendmail
send mail if files are modified either using inotify (better for huge folders and instant) or python3

# usage of inotify-sendmail

## install dependencies
```
apt-get install inotify-tools swaks
```

## adjust email settings
edit `sendmail.sh` to your email providers setting, modify Subject and --to as well.

## execute to monitor
`´´
monitor.sh /path/to/monitor
´´`

# usage of scan.py

## setup
- install python > 3.5
- adjust email settings and formatting

## execute to scan once (use any sheduler to monitor)
`´´
python3 scan.py /path/to/scan
´´`
