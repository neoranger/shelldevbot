#!/bin/bash
while true
do
python2 /home/pi/Documents/git/shelldevbot/shelldevbot.py
echo "¡The bot is crashed!"
#echo "ShellDevBot is crashed" | mail -s "Aviso" email@gmail.com
echo "Rebooting in:"
for i in 1
do
echo "$i..."
done
echo "###########################################"
echo "#ShellDevBot is restarting now            #"
echo "###########################################"
done
