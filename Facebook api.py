#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('C:/Python36/Lib/site-packages/') # Replace this with the place you installed facebookads using pip
sys.path.append('C:/Python36/Lib/site-packages/facebook_business-3.3.4-py3.6.egg/EGG-INFO') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
import datetime
import time
import json
import pandas as pd 
import numpy as np 

access_token = 'X'
ad_account_id = 'X'
my_app_secret = 'X'
my_app_id = 'X'
FacebookAdsApi.init(access_token=access_token)


#Definimos las variables para fecha inicial y fecha final. En estas primeras lineas la fecha final siempre debe ser igual a la fecha inicial
#el ciclo for se encargará de ir aumentando día por día sobre la fecha inicial
date_init = datetime.datetime(2019, 11, 1, 0, 0, 0)
date_fin = date_init

#Convertimos la fecha inicial y la fecha final en formato unix
date_init_unix = time.mktime(date_init.timetuple())
date_fin_unix = time.mktime(date_fin.timetuple())

#Creamos una variable para tener un tamaño de paso de un día convertido a segundos
secs_day= 60*60*24

contador=0
date_init_str = datetime.datetime.fromtimestamp(int(time.mktime(date_init.timetuple()))).strftime("%Y-%m-%d")

insights = []
#df_campaigns = pd.DataFrame(columns=['campaign_id', 'campaign_name', 'clicks', 'cost_per_unique_click', 'cpc', 'cpm', 'ctr', 'date_start', 'date_stop', 'impressions', 'reach', 'spend', 'unique_ctr'])
df_campaigns = pd.DataFrame()
#El ciclo for está definido para la lectura de 30 días, pero pueden adaptarlo para periodos más amplios o más cortos
for i in range(1,31):
    date_init_str = datetime.datetime.fromtimestamp(int(time.mktime(date_init.timetuple()) + contador)).strftime("%Y-%m-%d")
    date_fin_str =datetime.datetime.fromtimestamp(int(time.mktime(date_init.timetuple()) + contador)).strftime("%Y-%m-%d")
    
    fields = [
        'account_name',
        'account_id',
        'ad_name',
        'adset_name',
        'campaign_name',
        'frequency',
        'reach',
        'impressions',
        'spend',
        'objective',
        'video_p100_watched_actions',
        'video_p25_watched_actions',
        'video_p50_watched_actions',
        'video_p75_watched_actions',
        'video_play_actions',
        'video_thruplay_watched_actions',
        'clicks',
        'full_view_impressions',
        'video_30_sec_watched_actions',
        'video_avg_time_watched_actions',
        'conversions',
        'date_start',
        'date_stop',
        'ad_id',
        'campaign_id',
        'actions',
        'inline_link_clicks',
        'video_avg_time_watched_actions'

    ]

    params = {
        'level': 'ad',
        'time_range': { 'since': date_init_str, 'until': date_fin_str },
    }


    metrics = AdAccount(ad_account_id).get_insights(
        fields=fields,
        params=params,
    )
    contador= contador + secs_day 

    df_campaigns = df_campaigns.append(pd.DataFrame.from_dict(metrics))
    
    export_csv = df_campaigns.to_csv(r'C:\Users\X\OneDrive\Desktop\Archive.csv', header=True, index = None)

