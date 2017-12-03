# -*- coding: utf-8 -*-
#NX_BOT

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate
from gtts import gTTS

cl = LINETCR.LINE()
cl.login(token="EnvkuWcbWcefvYouIjg2.VyJ6iKnWDMTkM+Do0igvSG.FezTewKOLw8F9mhCpHcwXYvKN9KBVgZnII7LMlXuIBM=")
#cl.login(token='')
cl.loginResult()
print "Cl-Login Success\n"

ki = LINETCR.LINE()
ki.login(token="EnY66Xy1fsWGEKKYxnsc.a5W5Uxa5CjR5SyEGh1wKda.AnOD3ci2E2g66r7rPLS6MhxfXkdv4agDMroi7CnMj8c=")
#ki.login(token='')
ki.loginResult()
print "Ki-Login Success\n"

kk = LINETCR.LINE()
kk.login(token="Enpzl9opqWPvNUMassc1.REd9l2nLC8+St2sjd9IQGq.L6vTZRnRfy0o4LWKVXGeFi61SJbtYBnEukG2+93JBqE=")
#kk.login(token='')
kk.loginResult()
print "Kk-Login Success\n"

kc = LINETCR.LINE()
kc.login(token="EndHFVpXWULHqa3YF3A0.I+DfCfJ6bvXZycRseDNkaa.2tQd/zbaSU5aNeo1BKrTDXTR+MbHVmQ4zYnMN36Bd2I=")
#kc.login(token='')
kc.loginResult()
print "Kc-Login Success\n"

ks = LINETCR.LINE()
ks.login(token="EnNjcmFuI6kDZy5MYEx9.Noscy/kvUr/AkQPeJI7kwq.0el6n4HT1076wNCuL/yNnqe0cooAMN7zDkkmyUEw/tM=")
#ks.login(token=")
print "All Login Success"

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
┏━━ೋ• ❄ •ೋ━━━┓
     ❁ ᴇxᴏʀᴄɪsᴛ ᴛᴇᴀᴍ❁    
┗━━ೋ• ❄ •ೋ━━━┛
║❂͜͡➣ᴄʀᴇᴀᴛᴏʀ
║❂͜͡➣ɢᴄʀᴇᴀᴛᴏʀ
║❂͜͡➣ɢɪғᴛ
║❂͜͡➣ʀᴇsᴘᴏɴsᴇɴᴀᴍᴇ
║❂͜͡➣/ᴛʀᴀɴsʟᴀᴛᴇ-ᴇɴ
║❂͜͡➣/ᴛʀᴀɴsʟᴀᴛᴇ-ɪᴅ
║❂͜͡➣sᴇᴛᴠɪᴇᴡ
║❂͜͡➣ᴠɪᴇᴡsᴇᴇɴ
║❂͜͡➣.ɪɴsᴛᴀɢʀᴀᴍ
║❂͜͡➣/ʏᴏᴜᴛᴜʙᴇ
╠════════════════
╠ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴀᴅᴍɪɴ
╠════════════════
║❂͜͡➣ɢʟɪsᴛ/ʟɪsᴛ ɢʀᴏᴜᴘ
║❂͜͡➣ᴋɪᴄᴋ:
║❂͜͡➣ʙᴄ:
║❂͜͡➣ᴄᴀɴᴄᴇʟᴀʟʟ
║❂͜͡➣ᴛᴀɢ ᴀʟʟ
║❂͜͡➣ᴀʟʟ ᴊᴏɪɴ
║❂͜͡➣ᴀᴜᴛᴏᴄᴀɴᴄᴇʟ:ᴏɴ/ᴏғғ
║❂͜͡➣ᴀᴜᴛᴏᴋɪᴄᴋ:ᴏɴ/ᴏғғ
║❂͜͡➣ʙᴏᴏᴍ @
║❂͜͡➣sᴛᴀғғ ᴀᴅᴅ @
║❂͜͡➣sᴛᴀғғ ᴅᴇʟ @
║❂͜͡➣sᴛᴀғғʟɪsᴛ
║❂͜͡➣ᴀᴜᴛᴏᴊᴏɪɴ:ᴏɴ
║❂͜͡➣ᴡɪᴋɪ*ᴮᴱᵀᴬ
║❂͜͡➣ɪғᴄᴏɴғɪɢ*ᴮᴱᵀᴬ
║❂͜͡➣sʏsᴛᴇᴍ*ᴮᴱᵀᴬ
║❂͜͡➣ᴋᴇʀɴᴇʟ*ᴮᴱᵀᴬ
║❂͜͡➣ᴄᴘᴜ*ᴮᴱᵀᴬ
║❂͜͡➣ᴍɪᴍɪᴄ ᴛᴀʀɢᴇᴛ @*ᴮᴱᵀᴬ
║❂͜͡➣ᴍɪᴍɪᴄ ᴜɴᴛᴀʀɢᴇᴛ @*ᴮᴱᵀᴬ
╠════════════════
╠ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴏᴡɴᴇʀs
╠═══════════════
║❂͜͡➣ᴀᴅᴍɪɴ ᴀᴅᴅ @
║❂͜͡➣ᴀᴅᴍɪɴ ʀᴇᴍᴏᴠᴇ @
║❂͜͡➣ᴀᴅᴍɪɴʟɪsᴛ
║❂͜͡➣ʙᴏᴛ ʀᴇsᴛᴀʀᴛ
║❂͜͡➣ᴊᴏɪɴ ɢʀᴏᴜᴘ:
╠════════════════
╠ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʀᴇᴀᴛᴏʀ
╠════════════════
║❂͜͡➣ᴀʟʟ ʀᴇɴᴀᴍᴇ:
║❂͜͡➣ᴀʟʟʙɪᴏ:
║❂͜͡➣ᴋɪᴄᴋᴀʟʟ
║❂͜͡➣sʜᴜᴛᴅᴏᴡɴ

sᴜᴘᴘᴏʀᴛᴇᴅ : ᴇxᴏʀᴄɪsᴛ ᴛᴇᴀᴍ
"""

KAC=[cl,ki,kk,kc,ks]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid]
Creator="u5b35770e73cfaed07833c355f6705bd5"
admin=["u5b35770e73cfaed07833c355f6705bd5","ubd88fa224370766b4a9bf74ed08195b2","uade0fd2f636573cfec4f64890fd8aa81","u8bf7457058fa055c73602ad211d9ca00","u26063976cec7bb7507b8ed9053d2a247","u22dbfc8cf6a88aae724f7573dcd279c4","ue8f1af91716c53e8f4ecc2271018a654","u7f4bffb2218e3e0f774bfc2406a9abda","ucbb110bd9876374cf41da1bb9a702720"]
staff=["u5b35770e73cfaed07833c355f6705bd5","ubd88fa224370766b4a9bf74ed08195b2","uade0fd2f636573cfec4f64890fd8aa81","u8bf7457058fa055c73602ad211d9ca00","u26063976cec7bb7507b8ed9053d2a247","u22dbfc8cf6a88aae724f7573dcd279c4","ue8f1af91716c53e8f4ecc2271018a654","u7f4bffb2218e3e0f774bfc2406a9abda","ucbb110bd9876374cf41da1bb9a702720"]
owner="u5b35770e73cfaed07833c355f6705bd5","u7f4bffb2218e3e0f774bfc2406a9abda","u7fd29ae17122147632fc57cde32ed310","ucbb110bd9876374cf41da1bb9a702720","ue8f1af91716c53e8f4ecc2271018a654"

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":1,
    "AutoCancel":True,
    "AutoKick":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "clock":False,
    "cName":"ᴺˣᴮᴼᵀᴘʀᴇsᴇɴᴛ-1",
    "cName2":"ᴺˣᴮᴼᵀᴘʀᴇsᴇɴᴛ-2",
    "cName3":"ᴺˣᴮᴼᵀᴘʀᴇsᴇɴᴛ-3",
    "cName4":"ᴺˣᴮᴼᵀᴘʀᴇsᴇɴᴛ-4",
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e


def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"Ketik 'Help' untuk bantuan\n\nHarap gunakan dengan bijak!")
                else:
		    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"Ketik 'Help' untuk bantuan\n\nHarap gunakan dengan bijak!")
		    else:
                        cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
		            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    kk.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		
#-----------------------------------------------------------------
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------------------------------------
                if Creator in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Bots:
		    pass
		else:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti) #kicker join
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    kr.kickoutFromGroup(msg.to,[op.param2])
                    kr.leaveGroup(msg.to)
            else:
                pass
#--------------------------RECEIVE_MESSAGE---------------------------
        if op.type == 26:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            ki.sendText(msg.to,"already")
                            kk.sendText(msg.to,"already")
                            kc.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            ki.sendText(msg.to,"aded")
                            kk.sendText(msg.to,"aded")
                            kc.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        ks.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        ks.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))


#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"▶️MY CREATOR BOT◀️")
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
            elif msg.text in ["Backup on","backup on"]:
                if msg.from_ in admin:
                    wait["backup"] == True
                    cl.sendText(msg.to,"Backup mode already on")
                    kk.sendText(msg.to,"Backup mode already on")
                    ki.sendText(msg.to,"Backup mode already on")
                    kc.sendText(msg.to,"Backup mode already on")
                    print "[Command]Backup on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Backup off","backup off"]:
                if msg.from_ in admin:
                    wait["backup"] == False
                    cl.sendText(msg.to,"Backup mode already off")
                    kk.sendText(msg.to,"Backup mode already off")
                    ki.sendText(msg.to,"Backup mode already off")
                    kc.sendText(msg.to,"Backup mode already off")
                    print "[Command]Backup off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Protection on","protection on"]:
                if msg.from_ in admin:
                    wait["protectionOn"] == True
                    cl.sendText(msg.to,"Protect members is now on")
                    print "[Command]Protect on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["protection off","Protection off"]:
                if msg.from_ in admin:
                    wait["protectionOn"] == False
                    cl.sendText(msg.to,"Protect members is now off")
                    print "[Command]Protect off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Protect(admin):on","protect(admin):on"]:
                if msg.from_ in admin:
                    wait["protectionAdmin"] == True
                    cl.sendText(msg.to,"Protect admin is now on")
                    print "[Command]Protect admin on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["protect(admin):off","Protect(admin):off"]:
                if msg.from_ in admin:
                    wait["protectionAdmin"] == False
                    cl.sendText(msg.to,"Protect Admin is now off")
                    print "[Command]Protect admin off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#--------------------------------------------------------
            elif msg.text in ["List group","Glist","glist"]:
		if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "❂͜͡➣ 【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"===[List Group]===\n"+ h +"Total group: "+str(jml))
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Creator")
#--------------------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                
            elif "Kenapa " in msg.text:
                tanya = msg.text.replace("Kenapa ","")
                jawab = ("Gapapa","Terserah","Gpp.")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                
            elif msg.text in ["Xb1 rename "]:
                string = msg.text.replace("Xb1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Xb2 rename "]:
                string = msg.text.replace("Xb2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Xb3 rename "]:
                string = msg.text.replace("Xb3 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Xb4 rename "]:
                string = msg.text.replace("Xb4 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif "All rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("All rename:","")
                if len(string.decode('utf-8')) <= 9999999999999999999999999:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 999999999999999999999999:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 999999999999999999999999:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 999999999999999999999999:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
#--------------------------------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#--------------------------------------------------------
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        ki.sendText(msg.to,"nothing")
                        kk.sendText(msg.to,"nothing")
                        kc.sendText(msg.to,"nothing")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        ki.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
		elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#--------------------------------------------------------
            elif "Admin add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Admin add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif "Admin remove @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Admin remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in owner:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "❂͜͡➣ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"

#--------------------------------------------------------
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in owner:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Creator")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot di paksa keluar oleh owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    ks.leaveGroup(i)
			    cl.sendText(msg.to,"Success left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Khusus Creator")
#--------------------------------------------------------
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Bot di paksa keluar oleh owner!")
		        cl.leaveGroup(i)
			ki.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
			ks.leaveGroup(i)
		    cl.sendText(msg.to,"Success leave all group")
		else:
		    cl.sendText(msg.to,"Khusus Creator")
#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    Cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Ourl","Url:on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Curl","Url:off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    cl.sendText(msg.to,"AutoJoin Active")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin:off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"AutoJoin inActive")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
	    elif msg.text in ["Autocancel:on"]:
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["Autocancel:off"]:
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
	    elif "Qr:on" in msg.text:
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Active")

	    elif "Qr:off" in msg.text:
	    	wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["Status"]:
                md = ""
		if wait["AutoJoin"] == True: md+="✦ Auto join : on\n"
                else: md +="✦ Auto join : off\n"
		if wait["Contact"] == True: md+="✦ Info Contact : on\n"
		else: md+="✦ Info Contact : off\n"
                if wait["AutoCancel"] == True:md+="✦ Auto cancel : on\n"
                else: md+= "✦ Auto cancel : off\n"
		if wait["Qr"] == True: md+="✦ Qr Protect : on\n"
		else:md+="✦ Qr Protect : off\n"
		if wait["AutoKick"] == True: md+="✦ Autokick : on\n"
		else:md+="✦ Autokick : off"
                cl.sendText(msg.to,"=====[Status]=====\n"+md)
#--------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)

            elif msg.text in ["Xb1 Gift","Xb1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text in ["Xb2 Gift","Xb2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kk.sendMessage(msg)

            elif msg.text in ["Xb3 Gift","Xb3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kc.sendMessage(msg)

#--------------------------------------------------------
	#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Tag all"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = "" 
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
    
    #-------------Fungsi Tagall User  Edit By NyX-------------#
#--------------------------CEK SIDER------------------------------

            elif "Setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "Viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "++++TERCIDUK++++\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "Boom " in msg.text:
		if msg.from_ in Creator:
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])
		else:
		    cl.sendText(msg.to, "Khusus Creator")
#--------------------------------------------------------
	    elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif "Add all" in msg.text:
		if msg.from_ in admin:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif "Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "staff del @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("staff del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Staff del @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    mc = ""
                    for mi_d in staff:
                        mc += "|•| " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, "ᴺˣᴮᴼᵀᴘʀᴇsᴇɴᴛ(s)\n\nStaff list:\n" + mc)
                    print "[Command]Stafflist executed"
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		kc.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [cl,ki,kk,kc,ks]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam","Kam","kam","Wc","wc"]:
                gs = cl.getGroup(msg.to)
                ki.sendText(msg.to,"Welcome To "+ gs.name)
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
			cl.sendText(i,"[BROADCAST]\n"+bc+"\n#SorryBroadcast")
		    cl.sendText(msg.to,"Success Broadcast")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#--------------------------------------------------------
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Xb1 Cancelall"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                ki.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Xb2 Cancelall"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                kk.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Xb3 Cancelall"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                kc.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
            elif msg.text in ["Exorcist","Join all","join all","Join All","join All","Kuy"]: #Panggil Semua Bot
              if msg.from_ in admin:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Xb1 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Xb2 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Xb3 join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

#--------------------------------------------------------
	    elif msg.text in ["Xb Like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ki.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    kk.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    kc.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "AUTOLIKE BY NYX/nLIKE BACK line.me/ti/p/~nyx_on")
		    ki.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "AUTOLIKE BY NYX/nLIKE BACK line.me/ti/p/~nyx_on")
		    kk.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "AUTOLIKE BY NYX/nLIKE BACK line.me/ti/p/~nyx_on")
		    kc.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "AUTOLIKE BY NYX/nLIKE BACK line.me/ti/p/~nyx_on")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#--------------------------------------------------------
            elif msg.text in ["Bye all"]:
		if msg.from_ in admin:
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    ks.leaveGroup(msg.to)
                else:
                    cl.sendText(msg.to,"Lu Sapa!")

            elif msg.text in ["@Bye"]:
		if msg.from_ in admin:
		    cl.leaveGroup(msg.to)
		else:
		    cl.sendText(msg.to,"Lu Sapa!")
#--------------------------------------------------------
            elif msg.text in ["Absen","absen","Responsename","responsename"]:
		cl.sendText(msg.to,"EXORCIST 1 WAS HERE")
                ki.sendText(msg.to,"EXORCIST 2 WAS HERE")
                kk.sendText(msg.to,"EXORCIST 3 WAS HERE")
                kc.sendText(msg.to,"EXORCIST 4 WAS HERE")
                ks.sendText(msg.to,"EXORCIST 5 WAS HERE")
                ks.sendText(msg.to,"PASUKAN EXORCIST SIAP PROTECT\nMASALAH GAK AMAN URUSAN BELAKANG\nKEEP EATING MICIN ON YOUR DAY")

#--------------------------------------------------------
       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in staff:
                start = time.time()
                cl.sendText(msg.to, "Wait...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sDetik" % (elapsed_time))
                kk.sendText(msg.to, "%sDetik" % (elapsed_time))
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
                kc.sendText(msg.to, "%sDetik" % (elapsed_time))
                ks.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#
#==========================================
            elif "Nk: " in msg.text:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti) #kicker join
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                kr.kickoutFromGroup(msg.to,[target])
                                kr.leaveGroup(msg.to)
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Pakyu~")
			    else:
			        cl.sendText(msg.to,"Admin Detected")
		else:
		    cl.sendText(msg.to,"Lu sape!")
#--------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
#--------------------------------------------------------
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        kk.sendText(msg.to,"Not found")
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes BosQ")
                                    kk.sendText(msg.to,"Succes BosQ")
                                    kc.sendText(msg.to,"Succes BosQ")
                                except:
                                    ki.sendText(msg.to,"Error")
                                    kk.sendText(msg.to,"Error")
                                    kc.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"nothing")
                    kk.sendText(msg.to,"nothing")
                    kc.sendText(msg.to,"nothing")
                    ks.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "❂͜͡➣" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,"=[Blacklist User]=\n"+mc)

#--------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        kk.sendText(msg.to,"Not found")
                        kc.sendText(msg.to,"Not found")
                        ks.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Succes BosQ")
                                kc.sendText(msg.to,"Succes BosQ")
                                ks.sendText(msg.to,"Succes BosQ")
                            except:
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Succes BosQ")
                                kc.sendText(msg.to,"Succes BosQ")
                                ks.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            kk.sendText(msg.to,"There was no blacklist user")
                            kc.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                        kk.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                        kc.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    cl.sendText(msg.to, "Khusus admin JENG")
#--------------------------------------------------------
            elif msg.text in ["Kill"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kk.sendText(msg.to,"Fuck You")
                            kc.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc,ks]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif "Shutdown" in msg.text:
               if msg.from_ in Creator:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#--------------------------------------------------------
            elif "Kickall" == msg.text:
		if msg.from_ in Creator:
                    if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = ks.getGroup(msg.to)
                        ki.sendText(msg.to,"⚡GROUP HAS DESTROYED⚡")
                        kc.sendText(msg.to,"️FUCK YOU ALL️")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            kk.sendText(msg.to,"Not found.")
                            kc.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[ki,kk,kc,ks]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["Bot:restart","Restart","Bot restart","Bot Restart"]:
		if msg.from_ in owner:
		    cl.sendText(msg.to, "Bot has been restarted")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")

#--------------------------------------------------------



        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

