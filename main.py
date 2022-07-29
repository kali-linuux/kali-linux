import requests
import json
import subprocess
import helper
import time
import time
from subprocess import getstatusoutput
import logging
import os
import re
import simplejson

import requests

logger = logging.getLogger()

# thumb = os.environ.get("THUMB")
# if thumb.startswith("http://") or thumb.startswith("https://"):
#     getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
#     thumb = "thumb.jpg"


ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = (f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos")
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

url = (f"https://elearn.crwilladmin.com/api/v1/login-other")
info = {"password": "Redminote4x", "email": "8468056864"}

login_response = requests.post(url, info)
token = login_response.json()["data"]["token"]

url1 = requests.get("https://elearn.crwilladmin.com/api/v1/comp/my-batch?&token=" + token)
b_data = url1.json()['data']['batchData']

cool = ""
for data in b_data:
    FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
    aa = f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
    # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
    if len(f'{cool}{aa}') > 4096:
        cool = ""
    cool += aa
print(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')

editable1 = input("**Now send the Batch ID to Download**")
raw_text2 = editable1

# topic id url = https://elearn.crwilladmin.com/api/v1/comp/batch-topic/881?type=class&token=d76fce74c161a264cf66b972fd0bc820992fe576
url2 = requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-topic/" + raw_text2 + "?type=class&token=" + token)
topicid = url2.json()["data"]["batch_topic"]
bn = url2.json()["data"]["batch_detail"]["name"]
#     #await m.reply_text(f'Batch details of **{bn}** are :')
vj = ""
for data in topicid:
    tids = (data["id"])
    idid = f"{tids}&"
    if len(f"{vj}{idid}") > 4096:
        ##await m.reply_text(idid)
        vj = ""
    vj += idid

vp = ""
for data in topicid:
    tn = (data["topicName"])
    tns = f"{tn}&"
    if len(f"{vp}{tn}") > 4096:
        ##await m.reply_text(tns)
        vp = ""
    vp += tns

cool1 = ""
for data in topicid:
    t_name = (data["topicName"])
    tid = (data["id"])

    urlx = "https://elearn.crwilladmin.com/api/v1/comp/batch-detail/" + raw_text2 + "?redirectBy=mybatch&topicId=" + tid + "&token=" + token
    ffx = requests.get(urlx)
    vcx = ffx.json()["data"]["class_list"]["batchDescription"]
    vvx = ffx.json()["data"]["class_list"]["classes"]
    vvx.reverse()
    zz = len(vvx)
    BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
    hh = f"```{tid}```     - **{t_name} - ({zz})**\n"

    #         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

    if len(f'{cool1}{hh}') > 4096:
        ##await m.reply_text(hh)
        cool1 = ""
    cool1 += hh
# await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
#     #await m.reply_text(f'**{vcx}**')
#     #await m.reply_text(f'```{vj}```')

editable3 = input("**Now send the Resolution**")
raw_text4 = editable3

editable2 = input(
    f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
raw_text3 = editable2

#     editable9= #await m.reply_text(f"Now send the **Topic Names**\n\nSend like this **1&2&3&4** and so on\nor copy paste or edit **below names according to you in Order of ids you entered above** :\n\n**Enter this to download full batch :-**\n```{vp}```")


try:
    xv = raw_text3.split('&')
    for y in range(0, len(xv)):
        t = xv[y]

        #              xvv = raw_text9.split('&')
        #              for z in range(0,len(xvv)):
        #                  p =xvv[z]

        # gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57

        url3 = "https://elearn.crwilladmin.com/api/v1/comp/batch-detail/" + raw_text2 + "?redirectBy=mybatch&topicId=" + t + "&token=" + token
        ff = requests.get(url3)
        # vc =ff.json()["data"]["class_list"]["batchDescription"]
        mm = ff.json()["data"]["class_list"]["batchName"]

        vv = ff.json()["data"]["class_list"]["classes"]
        vv.reverse()
        # clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
        # #await m.reply_text(clan)
        count = 1
        try:
            for data in vv:
                vidid = (data["id"])
                lessonName = (data["lessonName"]).replace("/", "_")

                bcvid = (data["lessonUrl"][0]["link"])
                #                     lessonName = re.sub('\|', '_', cf)

                if True:
                    try:
                        video_response = requests.get(f"{bc_url}/{bcvid}", headers=bc_hdr)
                        video = video_response.json()
                        video_source = video["sources"][5]
                        video_url = video_source["src"]
                        # print(video_url)

                        surl = requests.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid=" + vidid + "&token=" + token)
                        stoken = surl.json()["data"]["token"]
                        # print(stoken)

                        link = video_url + "&bcov_auth=" + stoken  # print(link)
                    except Exception as e:
                        print(str(e))

                else:
                    link = "https://www.youtube.com/embed/" + bcvid
                    print(link)
                raw_text4 ="480"
                lessonName = "videos/"+lessonName
                cc = f"**{count}) Title :** {lessonName}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}"
                Show = f"**Downloading:-**\n**Title -** ```{lessonName}\n\nQuality - {raw_text4}```\n\n**Url :-** ```{link}```"
                prog = print(Show)

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
                    ytf = f"bestvideo[height<={raw_text4}]"

                if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                    cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}" "{link}"'
                else:
                    cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'

                # cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
                try:
                    download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                    os.system(download_cmd)

                    filename = f"{lessonName}.mp4"
                    #                         #await prog.delete (True)
                    #                         reply = #await m.reply_text("Uploading Video")
                    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:19 -vframes 1 "{filename}.jpg"', shell=True)

                    # thumbnail = f"{filename}.jpg"
                    # await prog.delete(True)
                    reply = print("Uploading Video")
                    dur = int(helper.duration(filename))
                    start_time = time.time()
                    # await m.reply_video(f"{lessonName}.mp4", caption=cc, supports_streaming=True, height=720, width=1280, thumb=thumbnail, duration=dur, progress=progress_bar,
                    progress_args = (reply, start_time)
                    count += 1
                    #os.remove(f"{lessonName}.mp4")
                    os.remove(f"{filename}.jpg")  # await reply.delete(True)
                except Exception as e:
                    print(f"**Video downloading failed ❌**\n{str(e)}\n\n**Url :-** ```{link}```")
            continue
        except Exception as e:
            print(str(e))
except Exception as e:
    print(str(e))
# await m.reply_text("Done")

notex =  input("Do you want download notes ?\n\nSend **y** or **n**")
raw_text5 = notex.text
if raw_text5 == 'y':
    url5 = requests.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/" + raw_text2 + "?topicid=" + raw_text2 + "&token=" + token)
    k = url5.json()["data"]["notesDetails"]
    bb = len(url5.json()["data"]["notesDetails"])
    ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
    # await m.reply_text(ss)
    k.reverse()
    count1 = 1
    for data in k:
        name = (data["docTitle"])
        s = (data["docUrl"])
        xi = (data["publishedAt"])

        ww = f"**{count1}) File Name :- **{name}\n**Date : **{xi}\n{bn}"
        show2 = f'**Downloading :-**\n\n**Link :** ```{s}```'
        prog2 =  print(show2)
        cmd2 = f'yt-dlp -o "{name}.pdf" "{s}"'
        try:
            download_cmd2 = f"{cmd2} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
            os.system(download_cmd2)
            # await m.reply_document(f'{name}.pdf', caption=ww)

            count1 += 1
            # await prog2.delete(True)
            os.remove(f'{name}.pdf')
            time.sleep(2)

        except Exception as e:
            # await m.reply_text(f"**PDF downloading failed ❌**\n{str(e)}")
            continue
