#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE



import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import time
from subprocess import getstatusoutput
import logging
import os
import re

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)
auth_users = [ int(chat) for chat in os.environ.get("AUTH_USERS").split(",") if chat != '']
logger = logging.getLogger()
# thumb = os.environ.get("THUMB")
# if thumb.startswith("http://") or thumb.startswith("https://"):
#     getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
#     thumb = "thumb.jpg"



@bot.on_message(filters.command(["start"]))
async def start(bot, update):
      await update.reply_text('''

█▄▄ █░░ ▄▀█ █▀▀ █▄▀  █▀█ █░█ ▀█▀
█▄█ █▄▄ █▀█ █▄▄ █░█  █▄█ █▄█ ░█░

🅷🅸 🅸 🅰️🅼 **🅲🅰️🆁🅴🅴🆁🆆🅸🅻🅻 🅳🅾️🆆🅽🅻🅾️🅰️🅳🅴🆁**

**🅽🅾🆆:-** 🅿🆁🅴🆂🆂 **/login** 🆃🅾 🅲🅾🅽🆃🅸🅽🆄🅴..

**🅱🅾🆃 🅼🅰🅳🅴 🅱🆈 **🅰🅱🅷🅸🆂🅷🅴🅺 🅱🅻🅰🅲🅺🅾🆄🆃**
         ''')

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1VmXspFMod94-pT7xDCvmBEYt8U7f0mRB6XnG5huPE7I9qjhDW0qpx3LRyTD9WX7W6JvUGtgKN-qf1pJoZO-QXBMIykDivtAOgkJOmN-kyv4m_F0thrJ45z95hqWON0nsKBwvd"
bc_url = (
    f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
)
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

url="https://elearn.crwilladmin.com/api/v1/"

info= {
 "deviceType":"android",
    "password":"",
    "deviceModel":"Asus ASUS_X00TD",
    "deviceVersion":"Pie(Android 9.0)",
    "email":"",
}

@bot.on_message(filters.command(["login"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
      myjsonfile=open('kali-linuux\UP Police Constable.json','r')
        jsondata=myjsonfile.read()
    obj=json.load(jsondata)
    b_data = obj.json()['data']['batchData']

    editable3= await m.reply_text("**Now send the Resolution**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text

    editable4= await m.reply_text("Now send the **Thumb url** Eg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text


    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    
   # editable9= await m.reply_text(f"Now send the **Topic Names**\n\nSend like this **1&2&3&4** and so on\nor copy paste or edit **below names according to you in Order of ids you entered above** :\n\n**Enter this to download full batch :-**\n```{vp}```")
    
    #   input9 = message = await bot.listen(editable.chat.id)
    #     raw_text9 = input9.text
  
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]
       
            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            
            ff = json.load(videos_dict)
            vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff.json()["data"]["class_list"]["batchName"]
            
            vv =ff.json()["data"]["class_list"]["classes"]
            vv.reverse()
            clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
#                     lessonName = re.sub('\|', '_', cf)
                    
                
                
                    if bcvid.startswith("62"):
                        try:
                            video_response = requests.get(f"{bc_url}/{bcvid}", headers=bc_hdr)
                            video = video_response.json()
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)

                            surl=requests.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token)
                            stoken = surl.json()["data"]["token"]
                            #print(stoken)

                            link = video_url+"&bcov_auth="+stoken
                            #print(link)
                        except Exception as e:
                            print(str(e))
                        
                    else:
                        link="https://www.youtube.com/embed/"+bcvid
                   #  await m.reply_text(link)

                    editable3= await m.reply_text("**Now send the Resolution**")
                    input4 = message = await bot.listen(editable.chat.id)
                    raw_text4 = input4.text

                    cc = f"**{count}) Title :** {lessonName}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}"
                    Show = f"**Downloading:-**\n**Title -** ```{lessonName}\n\nQuality - {raw_text4}```\n\n**Url :-** ```{link}```"
                    prog = await m.reply_text(Show)

                    if "youtu" in link:
                        if raw_text4 in ["144", "240", "480"]:
                            ytf = f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]'
                        elif raw_text4 == "360":
                            ytf = 18
                        elif raw_text4 == "720":
                            ytf = 22
                        else:
                            ytf = 18
                    else:
                        ytf=f"bestvideo[height<={raw_text4}]"
                        
                    if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}" "{link}"'
                    else:
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'


                    #cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
                    try:
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd)
                        

                        filename = f"{lessonName}.mp4"
#                         await prog.delete (True)
#                         reply = await m.reply_text("Uploading Video")
                        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:19 -vframes 1 "{filename}.jpg"', shell=True)
    
                        #thumbnail = f"{filename}.jpg"
                        await prog.delete (True)
                        reply = await m.reply_text("Uploading Video")
                        

                        try:
                            if thumb == "no":
                                thumbnail = f"{filename}.jpg"
                            else:
                                thumbnail = thumb
                        except Exception as e:
                            await m.reply_text(str(e))



                        dur = int(helper.duration(filename))
#                         await prog.delete (True)
                        start_time = time.time()
                        await m.reply_video(f"{lessonName}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{lessonName}.mp4")
                        
                        os.remove(f"{filename}.jpg")
                        await reply.delete (True)
                    except Exception as e:
                        await m.reply_text(f"**Video downloading failed ❌**\n{str(e)}\n\n**Url :-** ```{link}```")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")
    
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            url5=requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token)
            k=url5.json()["data"]["notesDetails"]
            bb = len(url5.json()["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                 
                    
                    ww = f"**{count1}) File Name :- **{name}\n**Date : **{xi}\n{bn}"
                    show2 = f'**Downloading :-**\n\n**Link :** ```{s}```'
                    prog2 = await m.reply_text(show2)
                    cmd2=f'yt-dlp -o "{name}.pdf" "{s}"'
                    try:
                        download_cmd2 = f"{cmd2} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd2)
                        await m.reply_document(f'{name}.pdf', caption=ww)

                        count1+=1
                        await prog2.delete (True)
                        os.remove(f'{name}.pdf')
                        time.sleep(2)
                        
                    except Exception as e:
                        await m.reply_text(f"**PDF downloading failed ❌**\n{str(e)}")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")

bot.run()
