#/bin/bash

# kill progress
# compile important-progress-program.p 
# run important-progress-program.p
cd /tmp/learn-git
git reset --hard HEAD # reset to last pull to sync up with repo, don't do this for development box
git pull
sleep 5
pro -p important-progress-program.p 

