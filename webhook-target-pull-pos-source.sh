#/bin/bash

# pull pos-source into /fiscal 
cd /fiscal
#git reset --hard HEAD # reset to last pull to sync up with repo, don't do this for development box
echo 'pull pos-source into /fiscal'
git pull origin 
echo 'pull pos-source into /fiscal done'
git log -p --name-status |head 
