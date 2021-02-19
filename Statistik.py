#!/usr/bin/env python
# coding: utf-8

# In[55]:


from __future__ import print_function
import pickle
import os
#import shutil
import re
#import numpy as np
import xlsxwriter
import json
import time
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime
from datetime import date
from datetime import timedelta
from operator import add

from discord_webhook import DiscordWebhook, DiscordEmbed

import configparser
import webbrowser

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)

# If modifying these scopes, delete the file token.pickle.

def my_sum(*nested_lists):
    return [[sum(items) for items in zip(*zipped_list)] for zipped_list in zip(*nested_lists)]

def my_sumwithfails(list1,list2):
    Erg = []
    for i in range(len(list1)):
        #print(i)
        #print(list1[i][0])
        #print(list2)
        if list1[i][0] == "-" and list2[i][0] == "-":
            Erg.append(["-"])
        if list1[i][0] == "-" and list2[i][0] != "-":
            Erg.append([list2[i][0]])
        if list1[i][0] != "-" and list2[i][0] == "-":
            Erg.append([list1[i][0]])
        if list1[i][0] != "-" and list2[i][0] != "-":
            Erg.append([int(list1[i][0]) + int(list2[i][0])])
    return[Erg]

today = date.today()


# In[38]:


#Response
response_monday = {'spreadsheetId': '1K9NAbYNht6TVqER8Z15mxWtFBjhpum_Z_izQVN4YMWw',
 'valueRanges': [{'range': 'Mech_twinlargos!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_twinlargos!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_twinlargos!X9:AG9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_twinlargos!AI9:AR9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_qadim!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sloth!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sloth!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sloth!X9:AG9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_matt!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_matt!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_cairn!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_cairn!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_cairn!X9:AG9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_mo!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sam!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_dei!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_dei!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_xera!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_xera!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_adina!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sabir!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_prlqadim!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_twinlargos!X9:AG9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_dhuum!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_dhuum!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_dhuum!X9:AG9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_vg!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_gors!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_gors!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sab!B9:K9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]},
 {'range': 'Mech_sab!M9:V9',
  'majorDimension': 'ROWS',
  'values': [['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]}]}


# In[39]:


def close_window(blub): 
    blub.destroy()


# In[40]:


def dateentry_view(root):

    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    
    ttk.Button(top, text="ok", command=lambda:[Running([cal.get_date()]),close_window(top)]).pack()


# In[41]:


def dateentry_start(root):

    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    
    ttk.Button(top, text="ok", command=lambda:[WriteInConfig("startmontag",cal.get_date().strftime("%d.%m.%Y")),close_window(top)]).pack()


# In[42]:


def dateentry_view2(root):
 
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal2 = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal2.pack(padx=10, pady=10)

    ttk.Button(top, text="ok", command=lambda:[Running([cal.get_date() + timedelta(days=x) for x in range((cal2.get_date() - cal.get_date()).days+1)]),close_window(top)]).pack()


# In[43]:


def Hauptfunktion(date1,config,mondaystart):
    spread = config['DEFAULT']["spreadsheetId"]
    ordner = config['DEFAULT']["dirs"]
    StaticAccs = config['DEFAULT']["staticaccs"].split("\",\"")
   
    Bosse = ["vg","gors","sab","sloth","trio","matt","kc","twstcstl","xera","cairn","mo","sam","dei","sh","river","brokenking","souleater","eyes","dhuum","ca","twinlargos","qadim","adina","sabir","prlqadim"]
    
    #date2 = datetime.strptime(date1,"%-m/%-d/%-y")
    datumaktuell = date1.strftime("%Y%m%d")
    
    
    l= []
    
    dirs = os.listdir(ordner)
    #print(dirs)
    for datei in dirs:
        if datei.endswith(".html"):
            if datei.startswith(datumaktuell):
                #print(datei)
                l.append(datei.split('_'))
                
    Output = [item for item in l if item[3] == 'fail.html'] 
    fails = len(Output)
    Output2 = [item for item in l if item[3] == 'kill.html'] 
    kills = len(Output2)
    
    if kills == 0 and fails == 0:
        fails = "-"
    
    #print("kills",Output2)
    #print(l)
    Kill = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    killinte = 0
    for i in Bosse:
        if any(i in s for s in Output2):
            Kill[killinte] = 1
        else:
            Kill[killinte] = 0
        killinte+=1
    #print(Kill)
    
    last_m = date1 +timedelta(days=-date1.weekday(), weeks=0)
    #print(last_m)
    #print(mondaystart)
    weekdiff1 = (last_m-mondaystart.date()).days / 7

    colmn=(xlsxwriter.utility.xl_col_to_name(int(weekdiff1 + 3)))

    range1 = "Statistik!"
    range1 = range1 + colmn + "3:" + colmn + "27"
    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spread,range=range1).execute()
    valuesMi = result.get('values', [])

    if not valuesMi:
        valuesMi=[["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
    else:{}#print(valuesMi)}  

    
    Fails_Mittwoch = []
    for i in range(len(Bosse)):
        Output = [item for item in l if item[1] ==  Bosse[i] and item[3] == 'fail.html'] 
        Fails_Mittwoch.append(len(Output))
    
    #check = Fails_Mittwoch + Kill
    check = list( map(add, Fails_Mittwoch, Kill) )
    #print(len(check))
    for i in range(len(check)):
        #print(i)
        if check[i] > 0:{}
        else:
            Fails_Mittwoch[i] = "-"
    
    
    MiFAILS = [[Fails_Mittwoch[0]],[Fails_Mittwoch[1]],[Fails_Mittwoch[2]],[Fails_Mittwoch[3]],[Fails_Mittwoch[4]],[Fails_Mittwoch[5]],[Fails_Mittwoch[6]],[Fails_Mittwoch[7]],[Fails_Mittwoch[8]],[Fails_Mittwoch[9]],[Fails_Mittwoch[10]],[Fails_Mittwoch[11]],[Fails_Mittwoch[12]],[Fails_Mittwoch[13]],[Fails_Mittwoch[14]],[Fails_Mittwoch[15]],[Fails_Mittwoch[16]],[Fails_Mittwoch[17]],[Fails_Mittwoch[18]],[Fails_Mittwoch[19]],[Fails_Mittwoch[20]],[Fails_Mittwoch[21]],[Fails_Mittwoch[22]],[Fails_Mittwoch[23]],[Fails_Mittwoch[24]]]
    
    
    cMi = []
    #print("valuesMi",valuesMi)
    new_list = [[x for x in lst] for lst in valuesMi]
    #print("check",check)
    #print("FAILS_Mittwoch",Fails_Mittwoch)
    #print("MiFAILS",MiFAILS)
    #print("new_list",new_list)
    
    
    #def my_sumwithfails():
        
    
    #return[MiFAILS,new_list]
    
    
    #print(MiFAILS)
    #print(new_list)
    #print(MiFAILS[11])
    #print(new_list[11])
    #print(len(MiFAILS))
    #print(len(new_list))
    cMi = my_sumwithfails(MiFAILS,new_list)
    
    return[cMi,fails, Kill,l]


# In[44]:


def Mechaniccount(ordner,date1,StaticAccs):
    #date2 = datetime.strptime(date1,"%-m/%-d/%-y")
    datumaktuell = date1.strftime("%Y%m%d")
    mechs = [["Float","Wave","Tornado","Charge"],["Q.Wave"],["Floor","Shake","Tantrum"],["Spirit","Hadouken"],["Port","Green","Agony"],["Jade Expl"],["Schk.Wv"],["Oil T.","Pizza"],["Orb","Orb Aoe"],["R.Blind"],["B.Tornado"],["A.Prj.H"],["Scythe"],["Mark","Dip","Crack"],["Boss TP"],["Egg","Slam"],["Flamewall","Cannon"]]
    mechsbosse = ["twinlargos","qadim","sloth","matt","cairn","mo","sam","dei","xera","adina","sabir","prlqadim","sh","dhuum","vg","gors","sab"]
    people = {StaticAccs[0]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[1]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[2]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[3]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[4]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[5]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[6]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[7]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[8]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] },
              StaticAccs[9]: {"twinlargos": [0,0,0,0], "qadim": [0], "sloth": [0,0,0],"matt": [0,0],"cairn": [0,0,0],"mo": [0],"sam": [0],"dei": [0,0],"xera": [0,0],"adina": [0],"sabir": [0],"prlqadim": [],"sh": [0],"dhuum": [0,0,0],"vg": [0],"gors": [0,0],"sab": [0,0] }}
    #bosseMech = {"twinlargos": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "qadim": [[0,0,0,0,0,0,0,0,0,0]],
     #            "sloth": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "matt": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
      #           "cairn":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "mo": [[0,0,0,0,0,0,0,0,0,0]], "sam": [[0,0,0,0,0,0,0,0,0,0]], "dei": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
       #          "xera": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
        #         "adina": [[0,0,0,0,0,0,0,0,0,0]],"sabir": [[0,0,0,0,0,0,0,0,0,0]],"prlqadim": [[0,0,0,0,0,0,0,0,0,0]],
         #        "sh": [[0,0,0,0,0,0,0,0,0,0]],"dhuum":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
          #       "vg": [[0,0,0,0,0,0,0,0,0,0]],"gors": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],"sab": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]}    
    bosseMech = {"twinlargos": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]], "qadim": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "sloth": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]], "matt": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "cairn":  [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]], "mo": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]], "sam": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]], "dei": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "xera": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "adina": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],"sabir": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],"prlqadim": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "sh": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],"dhuum":  [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],
                 "vg": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],"gors": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]],"sab": [["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]}    

    vari = -1
    for file in os.listdir(ordner):
        if file.endswith(".json"):
            if file.startswith(datumaktuell):
                with open(ordner + "\\\\" +file, encoding='utf-8') as json_file:
                    #print(file)
                    data = json.load(json_file) 
                    playerlist=[]
                    #print(StaticAccs)
                    
                    if file.find("ca_") == 16 :
                        continue
                    if file.find("twinlargos_") == 16 :
                        vari=0
                    if file.find("qadim_") == 16 :
                        vari=1
                    if file.find("sloth_") == 16 :
                        vari=2
                    if file.find("trio_") == 16 :
                        continue
                    if file.find("matt_") == 16 :
                        vari=3
                    if file.find("cairn_") == 16 :
                        vari=4
                    if file.find("mo_") == 16 :
                        vari=5
                    if file.find("sam_") == 16 :
                        vari=6
                    if file.find("dei_") == 16 :
                        vari=7
                    if file.find("kc_") == 16 :
                        continue
                    if file.find("twstcstl_") == 16 :
                        continue
                    if file.find("xera_") == 16 :
                        vari=8
                    if file.find("adina_") == 16 :
                        vari=9
                    if file.find("sabir_") == 16 :
                        vari=10
                    if file.find("prlqadim_") == 16 :
                        vari=11
                    if file.find("sh_") == 16 :
                        vari=12
                    if file.find("river_") == 16 :
                        continue
                    if file.find("brokenking_") == 16 :
                        continue
                    if file.find("souleater_") == 16 :
                        continue
                    if file.find("eyes_") == 16 :
                        continue
                    if file.find("dhuum_") == 16 :
                        vari=13
                    if file.find("vg_") == 16 :
                        vari=14
                    if file.find("gors_") == 16 :
                        vari=15
                    if file.find("sab_") == 16 :
                        vari=16
           
           
                    for u in StaticAccs:
                        player1 = list(filter(lambda x:x["account"]==u,data["players"]))
                        if not player1:
                               playerlist.append(player1)
                        else:
                               player1 = player1[0]["name"]
                               #print(player1)
                               playerlist.append(player1)
           
                    iteraplayer = 0
                    #print("playerlist",playerlist)
                    for j in playerlist:
                        #print("j",j)
                        iteramech = 0
                        AnzMech = len(mechs[vari])
                        #print("AnzMech",AnzMech)
                        list2 = [0] * AnzMech
                        for i in mechs[vari]:
                            if j == []:
                                #print(vari)
                                #print(mechsbosse[vari])
                                #print(iteramech)
                                #print(iteraplayer)
                                bosseMech[mechsbosse[vari]][iteramech][iteraplayer]= "NA"
                                iteramech +=1
                                continue
                            test666 = (list(filter(lambda x:x["name"]==i,data["mechanics"])))
                            #print("test666",test666)
                            if not test666:
                                fails = 0
                                list2[iteramech] = fails
                                if bosseMech[mechsbosse[vari]][iteramech][iteraplayer] == "NA":
                                    bosseMech[mechsbosse[vari]][iteramech][iteraplayer] = fails
                                else:
                                    bosseMech[mechsbosse[vari]][iteramech][iteraplayer] = bosseMech[mechsbosse[vari]][iteramech][iteraplayer] + fails
                                
                                iteramech +=1
                                
                            else:
                                test666 = test666[0]["mechanicsData"]
                                fails = str(test666).count(str(j))
                                list2[iteramech] = fails
                                #print("vari",vari)
                                #print("iteramech",iteramech)
                                #print("iteraplayer",iteraplayer)
                                #print(bosseMech[mechsbosse[vari]][iteramech][iteraplayer])
                                if bosseMech[mechsbosse[vari]][iteramech][iteraplayer] == "NA":
                                    bosseMech[mechsbosse[vari]][iteramech][iteraplayer] = fails
                                else:
                                    bosseMech[mechsbosse[vari]][iteramech][iteraplayer] = bosseMech[mechsbosse[vari]][iteramech][iteraplayer] + fails
                                
                                iteramech +=1
                            people[StaticAccs[iteraplayer]][mechsbosse[vari]] = list(map(lambda n1, n2: n1+n2, people[StaticAccs[iteraplayer]][mechsbosse[vari]], list2) )
                        iteraplayer +=1
    return(bosseMech)


# In[45]:


def Running(date_list):
    
    if isinstance(date_list, list): {}
        
    else: 
        date_list = [date_list]
    
    config = configparser.ConfigParser()
    config.read('Static.ini')
    mondaystart = datetime.strptime(config['DEFAULT']["startmontag"],"%d.%m.%Y")
    
    mechsbosse = ["twinlargos","qadim","sloth","matt","cairn","mo","sam","dei","xera","adina","sabir","prlqadim","sh","dhuum","vg","gors","sab"]
    mechs = [["Float","Wave","Tornado","Charge"],["Q.Wave"],["Floor","Shake","Tantrum"],["Spirit","Hadouken"],["Port","Green","Agony"],["Jade Expl"],["Schk.Wv"],["Oil T.","Pizza"],["Orb","Orb Aoe"],["R.Blind"],["B.Tornado"],[],["Scythe"],["Mark","Dip","Crack"],["Boss TP"],["Egg","Slam"],["Flamewall","Cannon"]]
    MechSave = {"twinlargos": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "qadim": [[0,0,0,0,0,0,0,0,0,0]],
                     "sloth": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "matt": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "cairn":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "mo": [[0,0,0,0,0,0,0,0,0,0]], "sam": [[0,0,0,0,0,0,0,0,0,0]], "dei": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "xera": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "adina": [[0,0,0,0,0,0,0,0,0,0]],"sabir": [[0,0,0,0,0,0,0,0,0,0]],"prlqadim": [[0,0,0,0,0,0,0,0,0,0]],
                     "sh": [[0,0,0,0,0,0,0,0,0,0]],"dhuum":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "vg": [[0,0,0,0,0,0,0,0,0,0]],"gors": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],"sab": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]}    
    OldMechs = {"twinlargos": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "qadim": [[0,0,0,0,0,0,0,0,0,0]],
                     "sloth": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "matt": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "cairn":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], "mo": [[0,0,0,0,0,0,0,0,0,0]], "sam": [[0,0,0,0,0,0,0,0,0,0]], "dei": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "xera": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "adina": [[0,0,0,0,0,0,0,0,0,0]],"sabir": [[0,0,0,0,0,0,0,0,0,0]],"prlqadim": [[0,0,0,0,0,0,0,0,0,0]],
                     "sh": [[0,0,0,0,0,0,0,0,0,0]],"dhuum":  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                     "vg": [[0,0,0,0,0,0,0,0,0,0]],"gors": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],"sab": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]}    
        
    
    ordner = config['DEFAULT']["dirs"]
    StaticAccs = config['DEFAULT']["staticaccs"].split("\",\"")
    
    ############################################################################################################################################################
    ### Alle Logs
    #
    #delta = date(2021,2,1) - mondaystart
    #numdays = delta.days
    #
    #dateList = []
    #date_list = [mondaystart + timedelta(days=x) for x in range(numdays)]
    
    ### Logs eines Tages
    
    #date_list = [date(2021,2,1)]
    
    ############################################################################################################################################################
    
    
    for i in range(len(date_list)):
        print(date_list[i])
        
        a = Mechaniccount(ordner,date_list[i],StaticAccs)
        b = Hauptfunktion(date_list[i],config,mondaystart)
        
        Rangelist = []
        last_m = date_list[i] +timedelta(days=-date_list[i].weekday(), weeks=0)
        row = int((last_m-mondaystart.date()).days / 7)+2
        
        for k in a: 
            for j in range(len(a[str(k)])):
                mechnumbercol=(xlsxwriter.utility.xl_col_to_name(j*11+1))
                mechnumbercol2=(xlsxwriter.utility.xl_col_to_name(j*11+10))
                RangeMechwrite =  "Mech_"
                RangeMechwrite = RangeMechwrite + k +"!" + mechnumbercol + str(row) + ":" + mechnumbercol2 + str(row)
                Rangelist.append(RangeMechwrite)
        
        
        weekdiff1 = (last_m-mondaystart.date()).days / 7
        colmn=(xlsxwriter.utility.xl_col_to_name(int(weekdiff1 + 3)))
    
        readranges2 = [Rangelist[0],Rangelist[1],Rangelist[2],Rangelist[3],Rangelist[4],Rangelist[5],Rangelist[6],Rangelist[7],Rangelist[8],Rangelist[9],Rangelist[10],Rangelist[11],Rangelist[12],Rangelist[13],Rangelist[14],Rangelist[15],Rangelist[16],Rangelist[17],Rangelist[18],Rangelist[19],Rangelist[20],Rangelist[21],Rangelist[22],Rangelist[23],Rangelist[24],Rangelist[25],Rangelist[26],Rangelist[27],Rangelist[28],Rangelist[29],Rangelist[30]]
        if last_m == date_list[i]:
            response = response_monday
        else:
            request = service.spreadsheets().values().batchGet(spreadsheetId=config['DEFAULT']["spreadsheetid"], ranges=readranges2)
            response = request.execute()
       
        
        l=0
        for n in mechsbosse: 
            for o in range(len(a[n])):
                for m in range(10):
                    #print(int(a[j][k][i])+int(response["valueRanges"][l]["values"][0][i]))
                    if a[n][o][m] == "NA" and response["valueRanges"][l]["values"][0][m] == "NA":
                        #print("beide NA")
                        MechSave[n][o][m] = "NA"
                    if a[n][o][m] == "NA" and response["valueRanges"][l]["values"][0][m] != "NA":
                        #print("a NA")
                        MechSave[n][o][m] = response["valueRanges"][l]["values"][0][m]
                    if a[n][o][m] != "NA" and response["valueRanges"][l]["values"][0][m] == "NA":
                        #print("response NA")
                        MechSave[n][o][m] = a[n][o][m]
                    if a[n][o][m] != "NA" and response["valueRanges"][l]["values"][0][m] != "NA":
                        #print(int(a[j][k][m])+int(response["valueRanges"][l]["values"][0][m]))
                        MechSave[n][o][m] = int(a[n][o][m])+int(response["valueRanges"][l]["values"][0][m])
                l +=1
    
        
        
        
        range1 = "Statistik!"
        range1 = range1 + colmn + "3:XXX27"    
        range2 = "Statistik!" + colmn + str(date_list[i].weekday()+28)
        range3 = "Statistik!" + colmn + str((2*date_list[i].weekday())+58)
        Rangelist.append(range1)
        Rangelist.append(range2)
        Rangelist.append(range3)
        #print(range2)
        #print(Rangelist)
        #print(range1)
        #print(range2)
        #print(range3)
        #print([MechSave["twinlargos"][0]])
        if not b[3]: 
            Raidzeit = "00:00:00"
        else:
            Raidzeit = datetime.strptime(b[3][-1][0][9:],"%H%M%S")-datetime.strptime(b[3][0][0][9:],"%H%M%S")+timedelta(seconds=int(b[3][0][2][:-1]))
    
        #print(str(Raidzeit))
        #body = {'values': b[0][0]}
        #result = service.spreadsheets().values().update(spreadsheetId=config['DEFAULT']["spreadsheetid"], range=range1, valueInputOption='USER_ENTERED', body=body).execute()
        #body = {'values': [[b[1]]]}
        #result = service.spreadsheets().values().update(spreadsheetId=config['DEFAULT']["spreadsheetid"], range=range2, valueInputOption='USER_ENTERED', body=body).execute()
        batch_update_values_request_body = {
        # How the input data should be interpreted.
        'value_input_option': "USER_ENTERED",  # TODO: Update placeholder value.
    
        # The new values to apply to the spreadsheet.
        'data':  [{"range": Rangelist[31],
                   "values": b[0][0]},
                  {"range": Rangelist[32],
                   "values": [[str(b[1])]]},
                  {"range": Rangelist[33],
                   "values": [[str(Raidzeit)]]},
        {
              "range":  Rangelist[0],
              "values": [MechSave["twinlargos"][0]]
            },{
              "range": Rangelist[1],
              "values": 
                [MechSave["twinlargos"][1]]
              
            },{
              "range": Rangelist[2], 
              "values": 
                [MechSave["twinlargos"][2]]
              
            },{
              "range": Rangelist[3],
              "values": 
                [MechSave["twinlargos"][3]]},{
              "range": Rangelist[4],
              "values": 
                [MechSave["qadim"][0]]},{
              "range": Rangelist[5],
              "values": 
                [MechSave["sloth"][0]]},{
              "range": Rangelist[6],
              "values": 
                [MechSave["sloth"][1]]},{
              "range": Rangelist[7],
              "values": 
                [MechSave["sloth"][2]]},{
              "range": Rangelist[8],
              "values": 
                [MechSave["matt"][0]]},{
              "range": Rangelist[9],
              "values": 
                [MechSave["matt"][1]]},
                {
              "range": Rangelist[10],
              "values": 
                [MechSave["cairn"][0]]},
                {
              "range": Rangelist[11],
              "values": 
                [MechSave["cairn"][1]]},
                {
              "range": Rangelist[12],
              "values": 
                [MechSave["cairn"][2]]},
                {
              "range": Rangelist[13],
              "values": 
                [MechSave["mo"][0]]},
                {
              "range": Rangelist[14],
              "values": 
                [MechSave["sam"][0]]},
                {
              "range": Rangelist[15],
              "values": 
                [MechSave["dei"][0]]},
                {
              "range": Rangelist[16],
              "values": 
                [MechSave["dei"][1]]},
                {
              "range": Rangelist[17],
              "values": 
                [MechSave["xera"][0]]},
                {
              "range": Rangelist[18],
              "values": 
                [MechSave["xera"][1]]},
                {
              "range": Rangelist[19],
              "values": 
                [MechSave["adina"][0]]},
                {
              "range": Rangelist[20],
              "values": 
                [MechSave["sabir"][0]]},
                {
              "range": Rangelist[21],
              "values": 
                [MechSave["prlqadim"][0]]},
                {
              "range": Rangelist[22],
              "values": 
                [MechSave["sh"][0]]},
                {
              "range": Rangelist[23],
              "values": 
                [MechSave["dhuum"][0]]},
                {
              "range": Rangelist[24],
              "values": 
                [MechSave["dhuum"][1]]},
                {
              "range": Rangelist[25],
              "values": 
                [MechSave["dhuum"][2]]},
                {
              "range": Rangelist[26],
              "values": 
                [MechSave["vg"][0]]},
                {
              "range": Rangelist[27],
              "values": 
                [MechSave["gors"][0]]},
                {
              "range": Rangelist[28],
              "values": 
                [MechSave["gors"][1]]},
                {
              "range": Rangelist[29],
              "values": 
                [MechSave["sab"][0]]},
                {
              "range": Rangelist[30],
              "values": 
                [MechSave["sab"][1]]
        },
            ],  # TODO: Update placeholder value.
        
            # TODO: Add desired entries to the request body.
        }
        
        request = service.spreadsheets().values().batchUpdate(spreadsheetId=config['DEFAULT']["spreadsheetid"], body=batch_update_values_request_body).execute()
    print("DONE")


# In[46]:


def WriteInConfig(usedkey,stringy):
    config = configparser.ConfigParser()
    config.read('Static.ini')
    config['DEFAULT'][usedkey] = stringy
    with open('Static.ini', 'w') as configfile:
        config.write(configfile)


# In[47]:


def Stringerstellen(arg1,*argv):
    if arg1 == "directory":
        for arg in argv:
            arg = arg.get()
            arg = arg.replace("\\", "\\\\")
            string = arg
    if arg1 == "staticaccs":
        string = ""
        #string = "\""
        for arg in argv:
            arg = arg.get()
            string = string + arg + "\",\""
        string = string[:-3]
    if arg1 == "spreadsheetid":
        for arg in argv:
            string = arg.get()
    return string


# In[48]:


def Teamcomp(root):
    newWindow = tk.Toplevel(root)
    label1 = tk.Label(newWindow, text="Spieler1").pack()

    eingabefeld1_wert=tk.StringVar()
    eingabefeld1=tk.Entry(newWindow, textvariable=eingabefeld1_wert)
    eingabefeld1.pack()
    
    label2 = tk.Label(newWindow, text="Spieler2").pack()
    
    eingabefeld2_wert=tk.StringVar()
    eingabefeld2=tk.Entry(newWindow, textvariable=eingabefeld2_wert)
    eingabefeld2.pack()
    
    label3 = tk.Label(newWindow, text="Spieler3").pack()
    
    eingabefeld3_wert=tk.StringVar()
    eingabefeld3=tk.Entry(newWindow, textvariable=eingabefeld3_wert)
    eingabefeld3.pack()
    
    label4 = tk.Label(newWindow, text="Spieler4").pack()
    
    eingabefeld4_wert=tk.StringVar()
    eingabefeld4=tk.Entry(newWindow, textvariable=eingabefeld4_wert)
    eingabefeld4.pack()
    
    label5 = tk.Label(newWindow, text="Spieler5").pack()
    
    eingabefeld5_wert=tk.StringVar()
    eingabefeld5=tk.Entry(newWindow, textvariable=eingabefeld5_wert)
    eingabefeld5.pack()
    
    label6 = tk.Label(newWindow, text="Spieler6").pack()
    
    eingabefeld6_wert=tk.StringVar()
    eingabefeld6=tk.Entry(newWindow, textvariable=eingabefeld6_wert)
    eingabefeld6.pack()
    
    label7 = tk.Label(newWindow, text="Spieler7").pack()
    
    eingabefeld7_wert=tk.StringVar()
    eingabefeld7=tk.Entry(newWindow, textvariable=eingabefeld7_wert)
    eingabefeld7.pack()
    
    label8 = tk.Label(newWindow, text="Spieler8").pack()
    
    eingabefeld8_wert=tk.StringVar()
    eingabefeld8=tk.Entry(newWindow, textvariable=eingabefeld8_wert)
    eingabefeld8.pack()
    
    label9 = tk.Label(newWindow, text="Spieler9").pack()
    
    eingabefeld9_wert=tk.StringVar()
    eingabefeld9=tk.Entry(newWindow, textvariable=eingabefeld9_wert)
    eingabefeld9.pack()
    
    label10 = tk.Label(newWindow, text="Spieler10").pack()
    
    eingabefeld10_wert=tk.StringVar()
    eingabefeld10=tk.Entry(newWindow, textvariable=eingabefeld10_wert)
    eingabefeld10.pack()
    
    schaltf1 = tk.Button(newWindow, text="Beenden", command=lambda:[close_window(newWindow),WriteInConfig("staticaccs",Stringerstellen("staticaccs",eingabefeld1_wert,eingabefeld2_wert,eingabefeld3_wert,eingabefeld4_wert,eingabefeld5_wert,eingabefeld6_wert,eingabefeld7_wert,eingabefeld8_wert,eingabefeld9_wert,eingabefeld10_wert))])
    schaltf1.pack()


# In[49]:


def directory(root):
    newWindow = tk.Toplevel(root)
    label1 = tk.Label(newWindow, text="directory").pack()
    eingabefeld1_wert=tk.StringVar()
    eingabefeld1=tk.Entry(newWindow, textvariable=eingabefeld1_wert)
    eingabefeld1.pack()
    
    schaltf1 = tk.Button(newWindow, text="Beenden", command=lambda:[close_window(newWindow),WriteInConfig("dirs",Stringerstellen("directory",eingabefeld1_wert))])
    schaltf1.pack()


# In[50]:


def Sync():
    config = configparser.ConfigParser()
    config.read('Static.ini')
    
    Range1 = "HintergrundDaten!B1:B10"
    Range2 = "HintergrundDaten!B72"
    StaticAccs = config['DEFAULT']["staticaccs"].split("\",\"")
    StaticAccs2 = [[StaticAccs[0]],[StaticAccs[1]],[StaticAccs[2]],[StaticAccs[3]],[StaticAccs[4]],[StaticAccs[5]],[StaticAccs[6]],[StaticAccs[7]],[StaticAccs[8]],[StaticAccs[9]]]
    Monday = config['DEFAULT']["startmontag"]
    batch_update_values_request_body = {
        'value_input_option': "USER_ENTERED", 
        'data':  [{"range": Range1,
                   "values": StaticAccs2},
                  {"range": Range2,
                   "values": [[str(Monday)]]}]}
    
    request = service.spreadsheets().values().batchUpdate(spreadsheetId=config['DEFAULT']["spreadsheetid"], body=batch_update_values_request_body).execute()


# In[51]:


def Spreadsheet(root):
    newWindow = tk.Toplevel(root)
    label1 = tk.Label(newWindow, text="Bestehendes Spreadsheet").pack()
    eingabefeld1_wert=tk.StringVar()
    eingabefeld1=tk.Entry(newWindow, textvariable=eingabefeld1_wert)
    eingabefeld1.pack()
    
    link1 = tk.Label(newWindow, text="Hier eine Kopie erstellen und neue ID angeben", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://docs.google.com/spreadsheets/d/1A5TMvVukDm8RQJ_-bRh4mvMjeNNx2604PwxUdVXL-fI/edit#gid=875665894"))
    
    schaltf1 = tk.Button(newWindow, text="Beenden", command=lambda:[close_window(newWindow),WriteInConfig("spreadsheetid",Stringerstellen("spreadsheetid",eingabefeld1_wert))])
    schaltf1.pack()


# In[52]:


def callback(url):
    webbrowser.open_new(url)


# In[53]:


def main():
    root = tk.Tk()
    s = ttk.Style(root)
    s.theme_use('clam')

    ttk.Button(root, text='OneDate', command=lambda:[dateentry_view(root)]).pack(padx=10, pady=10)
    ttk.Button(root, text='MultipleDates', command=lambda:[dateentry_view2(root)]).pack(padx=10, pady=10)
    button1 = ttk.Button(root,text="Teamcomp",command=lambda:[Teamcomp(root)])
    button1.pack()
    button2 = ttk.Button(root,text="directory",command=lambda:[directory(root)])
    button2.pack()
    button4 = ttk.Button(root,text="Montag der ersten Raid Woche",command=lambda:[dateentry_start(root)])
    button4.pack()
    button3 = ttk.Button(root,text="Spreadsheet",command=lambda:[Spreadsheet(root)])
    button3.pack()
    button5 = ttk.Button(root,text="Sync",command=lambda:[Sync()])
    button5.pack()
    buttonend = ttk.Button(root, text="Beenden", command=lambda:[close_window(root)])
    buttonend.pack()

    root.mainloop()


# In[58]:


if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[ ]:





# In[ ]:




