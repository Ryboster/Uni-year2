**Date: Wed 27 Aug 2025**<br>

# Activities

* 12pm - Created a crawler in selenium to recursively scrape a bunch of video links.<br><br>

* 3pm - Started writing a script for automatic management of this very repository.<br>

* 3:15pm - Read about variable assignment and splitting strings in bash.<br>

* 3:30pm - Read about logic in bash.<br><br>

* 4pm - Bogdan started approving my overdue PR's. Started working with him. Rebased 3 branches. Fixed merge conflicts. Issued a quick fix patch to dev.<br>

* 4:30pm - All PR's merged!<br>

* 6pm - Discovered linux tty's.<br>

* 6:30pm - Read about users in linux. Created new user with uid < 1000. Transferred some files over to that user.<br>

* 7:20pm - Read about chown.<br>

* 7:30pm - Enountered some strange unexpected behaviour with tty's. Read up on what the shortcuts do exactly.<br><br>

* 9pm - Watched a video about TBM.<br>

# Issues/Errors

<br>

# Next Steps

<br>

## Resources

https://crontab.guru/every-5-minutes<br>
https://unix.stackexchange.com/questions/666116/bash-interpreting-a-variable-assignment-as-a-command<br>
https://linuxize.com/post/linux-chown-command/<br>
https://linuxize.com/post/linux-chown-command/<br>
https://www.namehero.com/blog/bash-string-comparison-the-comprehensive-guide/<br>
https://stackoverflow.com/questions/638975/how-do-i-tell-if-a-file-does-not-exist-in-bash<br>
https://askubuntu.com/questions/66195/what-is-a-tty-and-how-do-i-access-a-tty<br>
https://www.youtube.com/watch?v=ZPOJxS6nqlo<br>

### Prepare_for_day.sh:

```bash
DATE=`date`

REPO_DIR="/home/snek/Desktop/portfolio/year-2-1/"
DAILY_LOGS_DIR="/home/snek/Desktop/portfolio/year-2-1/daily_logs/"
TEMPLATE_FILE="$DAILY_LOGS_DIR""template.md"
LAST_DAY_FILE="$DAILY_LOGS_DIR""last_day"

read -r -a lastDayParts <<< `cat $LAST_DAY_FILE`
read -r -a partsOfDate <<< "$DATE"

DAY_OF_WEEK=${partsOfDate[0]}
DAY_OF_MONTH=${partsOfDate[1]}
MONTH=${partsOfDate[2]}
TIME=${partsOfDate[3]}
TIMEZONE=${partsOfDate[4]}
YEAR=${partsOfDate[5]}
LAST_DAY=${lastDayParts[0]}
LAST_DAY_OF_MONTH=${lastDayParts[1]}
DATE_HEADER="**Date:"" $DAY_OF_WEEK"" $DAY_OF_MONTH"" $MONTH"" $YEAR""**<br>"
TODAYS_LOGS_DIR="$DAILY_LOGS_DIR""$MONTH""$YEAR""/"
TODAYS_LOG_FILENAME="day$LAST_DAY""_""$DAY_OF_WEEK""$DAY_OF_MONTH""$MONTH""$YEAR"".md"

if [ "$LAST_DAY_OF_MONTH" == "$DAY_OF_MONTH" ]; then
    exit 0
else
    LAST_DAY=$((LAST_DAY + 1))
    echo "$LAST_DAY $DAY_OF_MONTH" > $LAST_DAY_FILE
    mkdir $TODAYS_LOGS_DIR
fi

if [ -e "$TODAYS_LOGS_DIR""$TODAYS_LOG_FILENAME" ]; then
    echo "File exists"
else
    touch "$TODAYS_LOGS_DIR""$TODAYS_LOG_FILENAME"
    echo "$DATE_HEADER" > "$TODAYS_LOGS_DIR""$TODAYS_LOG_FILENAME"
    cat $TEMPLATE_FILE >> "$TODAYS_LOGS_DIR""$TODAYS_LOG_FILENAME"
fi

cd $REPO_DIR
git status
git add .
git commit -m "Automated commit #$LAST_DAY - $DAY_OF_WEEK $DAY_OF_MONTH $MONTH $TIME $TIMEZONE $YEAR \n"
git push

gedit "$TODAYS_LOGS_DIR""$TODAYS_LOG_FILENAME"
```

<br>
