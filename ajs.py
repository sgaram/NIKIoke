import ARIFISTIFIK
from ARIFISTIFIK import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
cl = LineClient(authToken='EyF2eOykkZOlhMSskbSc.Uv/0YYcEoAwu5rWj4Sx9Ja.JcV6XLyVQYi5TRHwcyhTWHGieRNzyB8pw6EpWEBNo2g=')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))
ki = LineClient(authToken='EyaTHDoUmqkSk5rDF2q0.9T/PGPFdadrWbCl3Gzx/Ga.nUOhdvYkYuxQeCD1Rd0aQ1afE7FXsggDnm5+TiUcvCA=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))
kk = LineClient(authToken='EyMVAJrWT3K1Bu2aeFJd.tLlReCirgG96uB+Q5pwO+q.W4ZMj2CEkJN79WkN1g75Su2cgwv4vW4YQ/o6bUHmNwI=')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))
kc = LineClient(authToken='EyqnPU6eypUkKha2u6ef.XzmbAwonn5keEY4vw/uKlW.WezUTgQUQU8avjFlu5LZcAv4KsEZrMrOIiCk38AoLFQ=')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))
sw = LineClient(authToken='EyNblrpMHXKdNRPHHDcb.zr+MvMh78HjcGGT1M17UEW.Tue/sbqqhBOgtGpOa8vNhZ/hFIqTvKqN/m7ydXe10Y8=')
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))
poll = LinePoll(cl)
call = cl
creator = ["ub95fb4cb209e39a594e51c09e2c5fd8c"]
owner = ["ub95fb4cb209e39a594e51c09e2c5fd8c"]
admin = ["ub95fb4cb209e39a594e51c09e2c5fd8c"]
staff = ["ub95fb4cb209e39a594e51c09e2c5fd8c"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [ki,kk,kc,sw]
ABC = [ki,kk,kc,sw]
Bots = [mid,Amid,Bmid,Cmid,Zmid]
Delta = admin + staff
protectqr = []
protectkick = []
responsename1 = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kk.getProfile().displayName
responsename5 = sw.getProfile().displayName
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "staff":{},
    'autoJoin':True,
    'autoAdd':True,
    "selfbot":True,
    }
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}
with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIdsx()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"❂-➣Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n❂-➣Group : "+str(len(gid))+"\n❂-➣Teman : "+str(len(teman))+"\n❂-➣Expired : In "+hari+"\n❂-➣Version : ARIFISTIFIK\n❂-➣Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n❂-➣Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "❂-➣MENU HELP\n" + \
                  "❂-➣" + key + "Me\n" + \
                  "❂-➣" + key + "Mid「@」\n" + \
                  "❂-➣" + key + "Kick1「@」\n" + \
                  "❂-➣" + key + "Status\n" + \
                  "❂-➣" + key + "Restart\n" + \
                  "❂-➣" + key + "Joinall\n" + \
                  "❂-➣" + key + "Byeall\n" + \
                  "❂-➣" + key + "Byeme\n" + \
                  "❂-➣" + key + "Remove chat\n" + \
                  "❂-➣" + key + "Protecturl「on/off」\n" + \
                  "❂-➣" + key + "Protectkick「on/off」\n" + \
                  "❂-➣" + key + "Refresh\n" + \
                  "❂-➣TEAM FANKZHER"
    return helpMessage
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "❂-➣HELP BOT\n" + \
                  "❂-➣" + key + "Banlist\n" + \
                  "❂-➣" + key + "Clearban\n" + \
                  "❂-➣" + key + "Refresh\n" + \
                  "❂-➣" + key + "Restart\n" + \
                  "❂-➣TEAM FANKZHER"
    return helpMessage1
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return      
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        ki.updateGroup(G)
                                        Ticket = ki.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = kc.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            kc.updateGroup(G)
                            Ticket = kc.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    except:
                                        try:
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = kc.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            kc.updateGroup(G)
                            Ticket = kc.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    sw.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                sw.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            sw.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        sw.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            cl.updateGroup(G)
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                sw.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")                               
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")                                      
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ━━━━━━━━━━━━━━━\n         ✯ S T A T U S ✯\n━━━━━━━━━━━━━━━\n"
                                if msg.to in protectqr: md+="❂-➣Protecturl「ON」\n"
                                else: md+="❂-➣Protecturl「OFF」\n"
                                if msg.to in protectkick: md+="❂-➣Protectkick「ON」\n"
                                else: md+="❂-➣Protectkick「OFF」\n"
                                cl.sendMessage(msg.to, md+"━━━━━━━━━━━━━━━\nFunkZher Bot\nWAR\n  ━━━━━━━━━━━━━━━")
                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid} 
                               cl.sendMessage1(msg)
                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass
                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to,responsename1)
                                ki.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kk.sendMessage(msg.to,responsename4)
                                sw.sendMessage(msg.to,responsename5)
                        elif cmd == "joinall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)
                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)                             
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.leaveGroup(msg.to)
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           ki.kickoutFromGroup(msg.to, [target])
                                           kc.kickoutFromGroup(msg.to, [target])
                                           kk.kickoutFromGroup(msg.to, [target])
                                           sw.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")
                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"❂-➣FunkZher Bot Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))
                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses mengampuni para pendosa " +mc)
    except Exception as error:
        print (error)
while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
