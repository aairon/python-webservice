#/bin/bash

# kill progress

ps -ef | grep "important-progress" | grep -v grep | awk '{print $2 }'  | xargs kill
exit 0
