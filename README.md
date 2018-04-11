# python-webserver
## Note - Use older commit for git webhook operation - maybe commit 93b651369f9c65febafc3b111a2a4660983ed3c5 or one before

This is a simple python webserver

I plan to run this on a linux box to receive web hooks from github to compile and run pos in the lab

this works in conjuction with the learn-git repo
Webhooks on github learn-git repo

http://10.20.132.84:8686/  (push) - local python server will kill currently running progress program
http://10.20.132.84:8080/  (push) - local python server will run progress program

steps of operation:
clone python-webserver repo

run dummy-web-server.py which will listen for push webhook from git hub on port 8080 and run the progress program :

	[adsphr@ads9955 python-webserver]$ python dummy-web-server.py 8080

for automatic kill and re-run of progress program also
run second web server on port 8686 that will listen for webhook and trigger a kill of last progress session  :

	[adsphr@ads9955 python-webserver]$ python dummy-web-server.py 8080

There is a 1 second sleep in the first server which allows the second server to run the kill script.
Running the second 'kill' server just allows the progress program to automatically run for every push to github

OPEN another shell same box:

clone learn-git into /tmp 

make a change to important-progress-program.p 

git add -uv 
git commit -m " made change" 
git push

dummy server2 will kill the still running important-progress-program.p .
dummy server will run important-progress-program.p with pushed changes.

