inotifywait -mrq -e modify --format %w%f $1 | while read FILE
do
    ./sendmail.sh "$(cat $FILE)"
done
