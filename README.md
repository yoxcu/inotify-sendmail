# inotify-sendmail
send mail if files are modified

# usage

## install dependencies
```
apt-get install inotify-tools swaks
```

## adjust email settings
edit `sendmail.sh` to your email providers setting, modify Subject and --to as well.

## execute
`monitor.sh /path/to/monitor`
