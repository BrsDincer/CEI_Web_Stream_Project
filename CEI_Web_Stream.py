import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
import time
import feedparser
from streamlit_folium import folium_static
import folium
import cv2


    
st.set_page_config(page_title="CEI PORTAL",layout="wide",
                   initial_sidebar_state="expanded")




try:
    
    LASCO_C2_IMAGE = Image.open(requests.get("https://soho.nascom.nasa.gov/data/realtime/c2/512/latest.jpg",
                 stream=True).raw) 
except:
    
    pass

try:
    
    LASCO_C3_IMAGE = Image.open(requests.get("https://soho.nascom.nasa.gov/data/realtime/c3/512/latest.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    HMII_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/sdo-hmii/latest.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_131_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/suvi/primary/131/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_304_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/suvi/primary/304/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_195_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/suvi/primary/195/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_094_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/suvi/primary/094/latest.png",
                 stream=True).raw)
except:
    
    pass


try:
    
    SYNOPTIC_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/synoptic-map.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    MULTI_ANA_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/swx-overview-small.gif",
                 stream=True).raw)
except:
    
    pass

try:
    
    STORM_CORR_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/storm-corrections.png",
                 stream=True).raw)
except:
    
    pass


try:
    
    SEAESRT_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/seaesrt-space-environment.png?time=1637079370000",
                 stream=True).raw)
except:
    
    pass

try:
    
    CHAR_HAZ_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/seaesrt-charging-hazards.png?time=1637079672000",
                 stream=True).raw)
except:
    
    pass


try:
    
    QUONTIENTS_HAZ_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/seaesrt-time-series-270.png",
                 stream=True).raw)
except:
    
    pass


try:
    
    SUN_L_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/suvi/primary/map/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    IMAGE_PATH_EQ_SEI = Image.open(requests.get("https://ds.iris.edu/seismon/views/eveday//imgs/topMap.eveday.png",
                 stream=True).raw)
except:
    
    pass


try:
    
    TOTAL_ELECTRON_CONTENT_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/ctipe/tec/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    ENLIL_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/enlil/latest.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    MAGNETOSPHERE_DENSITY_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/geospace/density/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    MAGNETOSPHERE_PRESSURE_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/geospace/pressure/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    MAGNETOSPHERE_VELOCITY_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/geospace/velocity/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    POLAR_NT_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/geospace/polar_lt/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    HF_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/d-rap/global/d-rap/latest.png",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_NORTH_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/ovation/north/latest.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    A_SOUTH_IMAGE = Image.open(requests.get("https://services.swpc.noaa.gov/images/animations/ovation/south/latest.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    EARTH_PAR_1_IMAGE = Image.open(requests.get("https://sdo.gsfc.nasa.gov/assets/img/latest/GONGFarsideMap.jpg",
                 stream=True).raw)
except:
    
    pass

try:
    
    EARTH_PAR_2_IMAGE = Image.open(requests.get("https://sdo.gsfc.nasa.gov/assets/img/latest/HMIFarsideMap.jpg",
                 stream=True).raw)

except:
    
    pass




PLASMA_2_HOURS_LINK = "https://services.swpc.noaa.gov/products/solar-wind/plasma-2-hour.json"
PLASMA_1_DAY_LINK = "https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json"

S_PROTONT_6_HOURS_LINK = "https://services.swpc.noaa.gov/json/goes/primary/integral-protons-plot-6-hour.json"
S_PROTONT_1_DAY_LINK = "https://services.swpc.noaa.gov/json/goes/primary/integral-protons-plot-1-day.json"

X_RAY_FLARES_7_DAYS_LINK = "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-7-day.json"
X_RAY_ENERGY_6_HOURS_LINK = "https://services.swpc.noaa.gov/json/goes/secondary/xrays-6-hour.json"
X_RAY_LATEST_LINK = "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json"
X_RAY_PERS_LINK = "https://services.swpc.noaa.gov/json/solar_probabilities.json"

SUN_SPOT_REGION_LINK = "https://services.swpc.noaa.gov/json/solar_regions.json"
SUN_SPOT_REGION_OTHER_LINK = "https://services.swpc.noaa.gov/json/sunspot_report.json"
SUN_SPOT_OBSERVED_LINK = "https://services.swpc.noaa.gov/json/solar-cycle/swpc_observed_ssn.json"
F107_LINK = "https://services.swpc.noaa.gov/json/f107_cm_flux.json"


try:
    
    GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
    
except:
    
    pass



CANADA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Canada/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
ALASKA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Alaska/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
USA_CON_HAWAII_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/USA_contiguous_and_Hawaii/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
CENTRAL_AMERICA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Central_America/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
SOUTH_AMERICA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/South_America/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
EUROPE_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Europe/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
NORTHERN_CENTRAL_AFRICA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Northern_and_Central_Africa/91cb2c01c62fe1291457d6a609abed0d/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
SOUTHERN_AFRICA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Southern_Africa/42102586c1688e590e18b046a4356bb4/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
RUSSIA_ASIA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Russia_Asia/42102586c1688e590e18b046a4356bb4/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
SOUTH_ASIA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/South_Asia/42102586c1688e590e18b046a4356bb4/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
SOUTHEAST_ASIA_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/SouthEast_Asia/42102586c1688e590e18b046a4356bb4/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"
AUSTRALIA_NEWZEALAND_FIRMS = "https://firms.modaps.eosdis.nasa.gov/mapserver/wfs/Australia_NewZealand/42102586c1688e590e18b046a4356bb4/?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAME=ms:fires_modis_7days&STARTINDEX=0&COUNT=1000&SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX=-90,-180,90,180,urn:ogc:def:crs:EPSG::4326&outputformat=csv"




def EUROPE_REGION_ALERT(country_type=str):
    
    URL_TARGET = f"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-{country_type}"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    

    AREA_TARGET = "cap:areadesc"
    AREA_EVENT = "cap:event"
    AREA_ONSET = "cap:expires"
    AREA_URGENCY = "cap:urgency"
    
    FIND_TARGET = SOUP_TARGET.find_all(AREA_TARGET)[-1]
    FIND_EVENT = SOUP_TARGET.find_all(AREA_EVENT)[-1]
    FIND_ONSET = SOUP_TARGET.find_all(AREA_ONSET)[-1]
    FIND_URGENCY = SOUP_TARGET.find_all(AREA_URGENCY)[-1]
    
    DICT_TARGET = {"TITLE":FIND_TARGET,
               "DESCRIPTION":FIND_EVENT,
               "DATE":FIND_ONSET,
               "URGENCY":FIND_URGENCY}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    
    
    
  
def BRAZIL_REGION_ALERT():
    URL_TARGET = "https://apiprevmet3.inmet.gov.br/avisos/rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    ITEM_ALL_CLASS = SOUP_TARGET.find_all("item")
    
    i_index_c = 0
    EVENT_LIST = []
    
    for X_LOOP_DIV in ITEM_ALL_CLASS:
    
        TD_ALL = X_LOOP_DIV.find_all("td")
        
        for X_SINGLE in TD_ALL:
            i_index_c += 1
            
            if 1 < i_index_c <= 6:
                
                EVENT_LIST.append(X_SINGLE.text)
                
                
    TYPE_TARGET = EVENT_LIST[0]
    STATUS_TARGET = EVENT_LIST[1]
    FIRST_DATE_TARGET = EVENT_LIST[2]
    SECOND_DATE_TARGET = EVENT_LIST[3]
    INFO_DATE = EVENT_LIST[4]
    
    DICT_TARGET = {"TITLE":TYPE_TARGET,
               "STATUS":STATUS_TARGET,
               "FIRST DATE":FIRST_DATE_TARGET,
               "SECOND DATE":SECOND_DATE_TARGET,
               "INFO DATE":INFO_DATE}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def CHINA_REGION_ALERT():
    URL_TARGET = "http://alert-feed.worldweather.org/cn-cma-xx/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    DATE_EVENT = EVENT_LIST[-1]
    DESCRIPTION_EVENT = EVENT_LIST[-6]
    TYPE_EVENT = EVENT_LIST[0]
    
    DICT_TARGET = {"TITLE":TYPE_EVENT,
               "DESCRIPTION":DESCRIPTION_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def ECUADOR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ec-inamhi-es/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def GUYANA_REGION_ALERT():
    
    URL_TARGET = "https://hydromet.gov.gy/cap/en/alerts/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]

    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def HONG_KONG_REGION_ALERT():
    
    URL_TARGET = "https://alerts.weather.gov.hk/V1/cap_atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")


    AREA_URGENCY = "cap:urgency"
        
    FIND_TARGET = SOUP_TARGET.find_all("title")[-1].text
    FIND_EVENT = SOUP_TARGET.find_all(AREA_URGENCY)[-1].text
    
    DICT_TARGET = {"TITLE":FIND_TARGET,
               "DESCRIPTION":FIND_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def INDIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    
    



def INDONESIA_REGION_ALERT():
    
    URL_TARGET = "https://signature.bmkg.go.id/alert/public/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[-2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    

    
def KENYA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ke-kmd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    


def MADAGASCAR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mg-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def MALAVI_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mw-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def MONGOLIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mn-namem-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def OMAN_REGION_TARGET():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/om-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def RUSSIA_REGION_ALERT():
    URL_TARGET = "https://meteoinfo.ru/hmc-output/cap/cap-feed/en/atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    DIV_ALL_CLASS = SOUP_TARGET.find("entry")
    
    FIND_TARGET = DIV_ALL_CLASS.find_all("summary")[-1].text
    FIND_EVENT = DIV_ALL_CLASS.find_all("dc:date")[-1].text
    
    DICT_TARGET = {"DESCRIPTION":FIND_TARGET,
               "DATE":FIND_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    
    


def SAUDI_ARABIA_ALERT():
    
    URL_TARGET = "https://ncm.gov.sa/Ar/alert/Pages/feedalerts.aspx"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    

    
def SOUTH_AFRICA_ALERT():
    
    URL_TARGET = "https://caps.weathersa.co.za/Home/RssFeed"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    
   
def SURINAME_AFRICA_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/sr-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME
    
    

def TANZANIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/tz-tma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def TRINIDAD_AND_TOBAGO_ALERT():
    
    URL_TARGET = "http://metproducts.gov.tt/ttms/public/api/feed?type=rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def UGANDA_REGION_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ug-unma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME



def ZIMBABWE_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/zw-msd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    DICT_TARGET = {"TITLE":TITLE_EVENT,
               "DESCRIPTION":DESC_EVENT,
               "DATE":DATE_EVENT}

    TARGET_FRAME = pd.DataFrame(DICT_TARGET,index=[0])
    
    return TARGET_FRAME


    
def MULTI_3_PLOT_SW(data_frame,title=str,marker_size_plot=int):
    
    figure_py = make_subplots(rows=1,cols=3,subplot_titles=("DENSITY","SPEED","TEMPERATURE"))
        
    figure_py.add_trace(
            go.Scatter(x=data_frame["time_tag"], y=data_frame["density"],name='p/cc',mode='markers',
                       marker=dict(size=marker_size_plot))
                       ,row=1, col=1
        )
        
    figure_py.add_trace(
            go.Scatter(x=data_frame["time_tag"], y=data_frame["speed"],name='km/s',mode='markers',
                       marker=dict(size=marker_size_plot)
                       ),
            row=1, col=2
        )
        
    figure_py.add_trace(
            go.Scatter(x=data_frame["time_tag"], y=data_frame["temperature"],name='K',mode='markers',
                       marker=dict(size=marker_size_plot)),
            row=1, col=3
        )
        
    figure_py.update_layout(height=420, width=740, title_text=title)
    
    return figure_py



def SINGLE_PROTON_PLOT(data_frame,title=str):

    figure_px = px.line(data_frame, x="time_tag", y="flux", color='energy', title=title)
    
    return figure_px





st.sidebar.title("**CLIMATIC EYE OF ISC INITIATIVE - CEI**")
st.sidebar.markdown("CEI was established by ISCI-Lab and created for report and analysis") 
SELECTBOX_SIDEBAR_GENERAL = st.sidebar.selectbox(
    "ANALYSIS PANEL",
    ("HOME", "SPACE WEATHER", "GENERAL DISASTERS PORTAL", "CYCLONE - FLOOD", "VOLCANO - EARTHQUAKE",
     "CLIMATIC PARAMETERS" ,"INTERACTIVE SEARCHING", "LOCAL ALERT", "REPORT A DISASTER")
)

if SELECTBOX_SIDEBAR_GENERAL == "HOME":
    
    
    st.header("INTERNATIONAL SPACE SCIENCE AND CLIMATE OBSERVATION INITIATIVE - ISCI")
    st.markdown("ISCI-Lab was established by ISCI")
    
    COL_VIS, COL_SW, COL_ND, COL_GS = st.columns(4)
    
    with COL_VIS:
        
        st.subheader("WHY WE EXIST")
        st.write("""                  
We are an initiative that conducts studies in the field of Space Science, publishes projects and reports, offers analytical perspectives and data analysis to stop the global climate catastrophe.
We believe that science changes the future. We want to host all the projects, studies and ideas that seem impossible. Imagination is the foundation of everything.

""")

    with COL_SW:
        
        st.subheader("SOLAR ACTIVITIES PANEL")
        st.write("""
                 Under this panel, there are solar and earth magnetosphere activities with various analyzes.
                 Instant monitoring and analysis of all data related to these areas are performed.
                 
                 Depending on the positions and structures of the satellites,the data is obtained at various time intervals.
                 """)
                 
    with COL_ND:
        
        st.subheader("NATURAL DISASTERS PANEL")
        st.write("""
                  This section shows disasters happening all over the planet and the data is in real time.
                  Wildfire, flood, drought, earthquake, tropical storms, industrial disasters, glacier meltdowns and all other disasters are included in this section.
                  Various reliable sources and databases are used in this section.
                 """)
    with COL_GS:
        
        st.subheader("CLIMATIC PARAMETERS")
        st.write("""
                  Data from all satellites (LEO) in the near orbital plane are analyzed and visualized in this section.
                  All general and detailed parameters are shown hourly, daily and monthly.
                  
                  These data analyzes are comparative and designed to give the most accurate results.
                 """)
                 
    
    
      
    st.header("THE GUARDIANS OF THE UNIVERSE")         
    SUB_COL_1,SUB_COL_2=st.columns(2)
    
    with SUB_COL_1:
        
        st.write("""
                  Climatic Eye of ISCI is an in-depth Earth Observation and Space Weather Tracking tool developed by the International Space Science and Climate Observation Initiative.
                  
                  It tracks different types of natural disasters (namely earthquakes, cyclones, forest fires, volcanoes, drought, floods, landslides, solar activities etc) at the very same moment they occur.
                  It also brings information related to that specific disaster, its location, size of the affected area, the magnitude of damage it caused along with the air quality measures of that location. 
                 """)

    with SUB_COL_2:
       st.write("""
                  The effect of global warming on Earth keeps increasing day by day, and this increase threatens many lives.
                  Sometimes it happens in the form of intense catastrophic natural disasters, sometimes it is as silent as the ice that melts in poles.  

                  Given the situation, as the world gets insatiable day by day the importance of observing parameters and detecting anomalies beforehand is crucial.
                  This is exactly why CEI exists.

                 """)
       
       
    st.subheader("_SCIENCE TO THE SKIES AND BEYOND_")
    
    
    with st.expander("CONTACT"):
         st.markdown("""

            **P-mail**:  
                
            initiative.isc@protonmail.com
            
            **T-mail**: 
                
            initiative.isc@tutanota.com
            
            **P-Private-mail**: 
                
            initiative.isc@pm.me
            
            _(prefer when you want to share confidential information)_
""")
               
        
        
    
if SELECTBOX_SIDEBAR_GENERAL == "SPACE WEATHER":
    
    
    st.header("SPACE WEATHER PANEL")
    st.markdown("_CEI was established by ISCI-LAB_")
    
    
    st.subheader("VIDEO - LAST 48 HOURS")
    
    st.markdown("**ANGSTROM TYPE**")
    COL_V_1, COL_V_2 = st.columns(2)
    
    try:
    
        with COL_V_1:
            
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0131.mp4")
            
        with COL_V_2:
            
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0304.mp4")
            
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
        
    COL_V_3, COL_V_4 = st.columns(2)
    
    try:
        
    
        with COL_V_3:
            
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0193.mp4")
            
        with COL_V_4:
            
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_1600.mp4")
        
        
        st.markdown("**TOTAL ANGSTROM WAVELENGTH**")
        st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_sixframe.mp4")
        
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
    
    COL_V_5, COL_V_6, COL_V_7 = st.columns(3)
    
    try:
        
    
        with COL_V_5:
            
            st.markdown("**LEFT SIDE**")
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/left.mp4")
            
        with COL_V_6:
            
            st.markdown("**TOP SIDE**")
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/top.mp4")
            
        with COL_V_7:
            
            st.markdown("**RIGHT SIDE**")
            st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/right.mp4")
            
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        st.markdown("**1-DIMENSION PERSPECTIVE**")
        st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_ar_map.mp4")
        
        st.markdown("**1-DIMENSION PERSPECTIVE**")
        st.video("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_composite_map.mp4")
        
        st.image(EARTH_PAR_1_IMAGE)
        st.image(EARTH_PAR_2_IMAGE)
        
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        # PLASMA 2 HOURS
        TARGET_PORT_2_HOURS = requests.get(PLASMA_2_HOURS_LINK)
        JSON_PORT_2_HOURS = TARGET_PORT_2_HOURS.json()
        
        PARAMETER_COLUMN_2_H = JSON_PORT_2_HOURS[0]
        PARAMETER_VALUES_2_H = JSON_PORT_2_HOURS[1:]
        
        DATA_2_H = pd.DataFrame(PARAMETER_VALUES_2_H)
        DATA_2_H.columns = PARAMETER_COLUMN_2_H
        
        # PLASMA 1 DAY
    
    
        
        TARGET_PORT_1_DAY = requests.get(PLASMA_1_DAY_LINK)
        JSON_PORT_1_DAY = TARGET_PORT_1_DAY.json()
        
        PARAMETER_COLUMN_1_DAY = JSON_PORT_1_DAY[0]
        PARAMETER_VALUES_1_DAY = JSON_PORT_1_DAY[1:]
        
        DATA_1_DAY = pd.DataFrame(PARAMETER_VALUES_1_DAY)
        DATA_1_DAY.columns = PARAMETER_COLUMN_1_DAY
        
    
        # CREATING FIGURE FOR PLASMA
        FIGURE_2_H_SW = MULTI_3_PLOT_SW(DATA_2_H,"PLASMA 2 HOURS - LIVE / PROTON BASE",4)
        FIGURE_1_D_SW = MULTI_3_PLOT_SW(DATA_1_DAY,"PLASMA 1 DAY - LIVE / PROTON BASE",4)
        
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
    
    
    # DEPLOY PLOTS FOR PLASMA
    st.subheader("PLASMA ANALYSIS")
    
    try:
        
        with st.expander("PLASMA 2 HOURS - LIVE"):
            st.plotly_chart(FIGURE_2_H_SW)
            
            st.dataframe(DATA_2_H)
            
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("PLASMA 1 DAY - LIVE"):
            st.plotly_chart(FIGURE_1_D_SW)
    
            st.dataframe(DATA_1_DAY)
        
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
        
     
        
    # SINGLE PROTON 6 HOURS
    
    try:
        
    
        S_PROTON_6_HOURS_JSON = pd.read_json(S_PROTONT_6_HOURS_LINK)
        PROTON_FIRST_6_HOURS = S_PROTON_6_HOURS_JSON
        
        # SINGLE PROTON 1 DAY
        
        S_PROTON_1_D_JSON = pd.read_json(S_PROTONT_1_DAY_LINK)
        PROTON_FIRST_1_D = S_PROTON_1_D_JSON
        
        # CREATIN FIGURE FOR SINGLE PROTON
        S_PROTON_6_H_P = SINGLE_PROTON_PLOT(PROTON_FIRST_6_HOURS,"PROTON FLUX 6 HOURS")
        S_PROTON_1_D_P = SINGLE_PROTON_PLOT(PROTON_FIRST_1_D,"PROTON FLUX 1 DAY")
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    # DEPLOY PLOTS FOR SINGLE PROTON
    st.subheader("PROTON FLUX ANALYSIS")
    
    try:
        
        with st.expander("PROTON FLUX 6 HOURS - LIVE"):
            st.plotly_chart(S_PROTON_6_H_P)
            st.dataframe(PROTON_FIRST_6_HOURS)
            
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("PROTON FLUX 1 DAY - LIVE"):
            st.plotly_chart(S_PROTON_1_D_P)
            st.dataframe(PROTON_FIRST_1_D)
    
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
        
        
        
    # X-RAY FLARES WAVELENGTH AND RATIO 7 DAYS
    
    try:
    
        S_7_DAYS_FLARES_JSON = pd.read_json(X_RAY_FLARES_7_DAYS_LINK)
        S_6_HOURS_FLUX_JSON = pd.read_json(X_RAY_ENERGY_6_HOURS_LINK)
        S_LATEST_FLUX_JSON = pd.read_json(X_RAY_LATEST_LINK)
        S_SPEC_FLUX_JSON = S_LATEST_FLUX_JSON[["current_class",
                                               "begin_class",
                                               "max_class",
                                               "end_class"]]
        S_SPEC_FLUX_JSON.index.name = None
        
        X_RAY_PERS_JSON = pd.read_json(X_RAY_PERS_LINK)
        X_RAY_PERS_JSON = X_RAY_PERS_JSON[["c_class_1_day",
                                               "m_class_1_day",
                                               "x_class_1_day"]].head(1)
        
        
        
        figure_py_x_ray_wave = make_subplots(rows=1,cols=3,subplot_titles=("MAX X-RAY","MAX RATIO","CURRENT X-RAY"))
            
        figure_py_x_ray_wave.add_trace(
                go.Scatter(x=S_7_DAYS_FLARES_JSON["time_tag"], y=S_7_DAYS_FLARES_JSON["max_xrlong"],name='MAX X-RAY')
                           ,row=1, col=1
            )
            
        figure_py_x_ray_wave.add_trace(
                go.Scatter(x=S_7_DAYS_FLARES_JSON["time_tag"], y=S_7_DAYS_FLARES_JSON["max_ratio"],name='MAX RATIO'
                           ),
                row=1, col=2
            )
            
        figure_py_x_ray_wave.add_trace(
                go.Scatter(x=S_7_DAYS_FLARES_JSON["time_tag"], y=S_7_DAYS_FLARES_JSON["current_int_xrlong"],name='CURRENT X-RAY'),
                row=1, col=3
            )
            
        figure_py_x_ray_wave.update_layout(height=420, width=740, title_text="X-RAY FLARES WAVELENGTH")
        
    except:
        
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN")
    
    
    # X-RAY FLARES TYPE
    
    try:
        
        figure_px_class_type = px.line(S_7_DAYS_FLARES_JSON,x="max_class",
                                      y="current_int_xrlong",title="CURRENT CLASS - CURRENT X-RAY")
    
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    
    # X-RAY ENERGY
    
    try:
    
        figure_px_energy = px.line(S_6_HOURS_FLUX_JSON,x="time_tag",
                                      y="flux",color="energy",title="FLUX - ENERGY")
    
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    

    
    
    # DEPLOY PLOTS FOR X-RAY ANALYSIS
    st.subheader("X-RAY ANALYSIS")
    
    try:
        
        with st.expander("X-RAY FLARES WAVELENGTH AND RATIO - LIVE"):
            st.plotly_chart(figure_py_x_ray_wave)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("X-RAY FLARES CLASS - LIVE"):
            st.plotly_chart(figure_px_class_type) 
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("X-RAY FLUX ENERGY - LIVE"):
            st.plotly_chart(figure_px_energy)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("X-RAY LATEST - LIVE"):
            st.markdown("_LATEST X RAY CLASS_")
            st.dataframe(S_SPEC_FLUX_JSON)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("SOLAR PROBABILITIES - LIVE"):
            st.markdown("_THE POWER PERCENTAGE OF LATEST EXPLOSIONS_")
            st.dataframe(X_RAY_PERS_JSON)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    
    # SUN SPOTS AND REGIONS
    
    try:
    
        SUN_REGION_JSON = pd.read_json(SUN_SPOT_REGION_LINK)
        SUN_REGION_JSON = SUN_REGION_JSON[["region","mag_class",
                                           "c_flare_probability",
                                           "m_flare_probability",
                                           "x_flare_probability"]]
        
        
        FIRST_4_REGION_JSON = SUN_REGION_JSON.head(4)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:    
        
        SUN_REGION_O_JSON = pd.read_json(SUN_SPOT_REGION_OTHER_LINK)
        SUN_REGION_O_JSON = SUN_REGION_O_JSON[["Region","Area",
                                           "Numspot",
                                           "Spotclass",
                                           "Magclass"]]
        
        FIRST_4_O_REGION_JSON = SUN_REGION_O_JSON.head(4)
        FIRST_4_O_REGION_JSON["Region"] = FIRST_4_O_REGION_JSON["Region"].apply(lambda x_value: ["%.f" % x_value for i_index in FIRST_4_O_REGION_JSON["Region"]][0])
    
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        SUN_SPOT_RE_O_JSON = pd.read_json(SUN_SPOT_OBSERVED_LINK)
        LAST_SSN_REPORT = SUN_SPOT_RE_O_JSON.tail(1)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    
    # SUNSPOT NUMBERS
    
    try:
        
        figure_px_sun_observed = px.line(SUN_SPOT_RE_O_JSON,x="Obsdate",
                                      y="swpc_ssn",title="OBSERVED SSN")
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    # DEPLOY SUN SPOTS AND REGIONS
    st.subheader("SUNSPOT REGIONS AND SSN")
    
    try:
        
        with st.expander("SUNSPOT REGIONS - LIVE"):
            st.dataframe(FIRST_4_REGION_JSON)
            st.dataframe(FIRST_4_O_REGION_JSON)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        with st.expander("SUNSPOT NUMBERS - LIVE"):
            st.plotly_chart(figure_px_sun_observed)
            st.markdown("_LATEST SSN REPORT_")
            st.dataframe(LAST_SSN_REPORT)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
        
    # HIGH-FREQUENCY
    
    try:
    
        F107_JSON = pd.read_json(F107_LINK)
        
        figure_px_sun_observed = px.line(F107_JSON,x="time_tag",
                                      y="flux",title="OBSERVED SSN")
        
        with st.expander("F10.7 CM FLUX - LIVE"):
            st.plotly_chart(figure_px_sun_observed)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
                  
        

    st.subheader("SOLAR OBSERVATION IMAGE")
    
    try:
        
        with st.expander("LASCO C2"):
            st.image(LASCO_C2_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        with st.expander("LASCO C3"):
            st.image(LASCO_C3_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    try:
        
        with st.expander("HMII"):
            st.image(HMII_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
        
    try:
        
        with st.expander("A - 094"):
            st.image(A_094_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("A - 131"):
            st.image(A_131_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("A - 195"):
            st.image(A_195_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("A - 304"):
            st.image(A_304_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("SUN LAYER"):
            st.image(SUN_L_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
        
    st.subheader("**SPOTS DETECTION**")
    st.markdown("_Real-time images are processed_")
    st.markdown("_USE TO BUTTON FOR RUNNING THE PROCESS_")
    
        
    BUTTON_DT_SS = st.button("DETECTION SUNSPOTS")
        
    if BUTTON_DT_SS:
        
        try:
        
            POR_BAR = st.progress(0)
    
            for percent_index in range(100):
                time.sleep(0.1)
                POR_BAR.progress(percent_index + 1)
                
            req_ss = urllib.request.urlopen('https://services.swpc.noaa.gov/images/animations/suvi/primary/094/latest.png')
            arr_ss = np.asarray(bytearray(req_ss.read()), dtype=np.uint8)
            img_ss = cv2.imdecode(arr_ss, cv2.IMREAD_COLOR)
    
            RESIZE_IMG_SS = cv2.resize(img_ss,(500,500))
            _,THRESHOLD_IMG_SS = cv2.threshold(RESIZE_IMG_SS,110,255,cv2.THRESH_BINARY)
            SEC_127_SS = cv2.inRange(THRESHOLD_IMG_SS,0,100)
    
            COPY_SEC_SS = RESIZE_IMG_SS.copy()
            Contour_C_S,_ = cv2.findContours(SEC_127_SS,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                
            for (i_s, c_s) in enumerate(Contour_C_S):
    
                ((cX_S, cY_S), radius_S) = cv2.minEnclosingCircle(c_s)
                Light_Circle_SS = cv2.circle(COPY_SEC_SS, (int(cX_S), int(cY_S)), int(radius_S),(255, 0, 0), 3)
                
                
            CUT_IMG_SS = COPY_SEC_SS[50:450,:,:]
    
            figure_dd, axis_dd = plt.subplots(figsize=(10,5))
            plt.style.use("dark_background")
            axis_dd.axis("off")
            axis_dd.plot(SEC_127_SS[:,:])
                
            st.image(CUT_IMG_SS)
            st.markdown("_The number of vertical bars in this graph represents the numerical density._")
            st.pyplot(figure_dd)
            
        except:
            
            st.info("PROCESS IS DEACTIVATED FOR NOW, PLEASE WAIT AND TRY AGAIN")
            
            
        
        
        
    st.subheader("MAGNETOSPHERE")
    
    with st.expander("BX-BY-BZ-BT LIVE"):
        
        try:
            
    
            MAG_URL = "https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json"
            
            MAG_RE = requests.get(MAG_URL)
            ALL_JSON_MAG = MAG_RE.json()
            COLUMN_DATA_MA = ALL_JSON_MAG[0]
            PARAMS_DATA_MA = ALL_JSON_MAG[1:]
            
            df_mag = pd.DataFrame(PARAMS_DATA_MA, columns = COLUMN_DATA_MA, dtype = float)
            
            fig_ma = go.Figure(
                    data=go.Scattergeo(
                        lon=df_mag['lon_gsm'],
                        lat=df_mag['lat_gsm'],
                        mode='markers',marker_color=df_mag['bt']))
            
            fig_ma.update_layout(
                    title='GEO-MAG',
                    geo=go.layout.Geo(
                        projection_type='orthographic',
                        showland=True,
                        showcountries=False,
                        landcolor='rgb(243, 243, 243)'))
            
            fig_ma.update_geos(
                resolution=50,
                showland=True, landcolor="#000000",
                showocean=False,
                showlakes=False
            )
            
            fig_ma.update_layout(autosize=False,
                width=500,
                height=500)
            
            st.plotly_chart(fig_ma)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    
    
    
    
    st.subheader("DRAFT REVIEWS AND OBSERVATIONS")
    
    try:
    
        with st.expander("SYNOPTIC SUN PAPER"):          
            st.image(SYNOPTIC_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
    
        with st.expander("FLARE - PFU - KP INDEX"):
            st.image(MULTI_ANA_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
        
    try:
    
        with st.expander("STORM CORRECTION"):
            st.image(STORM_CORR_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    
    st.subheader("SATELLITE STABILITY AND ANOMALY")
    
    try:
    
        with st.expander("ELECTRON CHARGING AND TIME"):          
            st.image(SEAESRT_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
    
        with st.expander("CHARGING HAZARD"):          
            st.image(CHAR_HAZ_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
    
        with st.expander("HAZARD QUANTIENTS"):          
            st.image(QUONTIENTS_HAZ_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
    
    st.subheader("EARTH BASED OBSERVATION IMAGE")
    
    try:
    
        with st.expander("AURORA NORTH"):
            st.image(A_NORTH_IMAGE,use_column_width=True)
            
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("AURORA SOUTH"):
            st.image(A_SOUTH_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("HIGH FREQUENCY"):
            st.image(HF_IMAGE,use_column_width=True)
    
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("POLARITY - POLAR BASED nT"):
            st.image(POLAR_NT_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("MAGNETOSPHERE DENSITY"):
            st.image(MAGNETOSPHERE_DENSITY_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("MAGNETOSPHERE PRESSURE"):
            st.image(MAGNETOSPHERE_PRESSURE_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("MAGNETOSPHERE VELOCITY"):
            st.image(MAGNETOSPHERE_VELOCITY_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("ENLIL IMAGE - PARKER"):
            st.image(ENLIL_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
        
    try:
        
        with st.expander("TOTAL ELECTRON CONTENT"):
            st.image(TOTAL_ELECTRON_CONTENT_IMAGE,use_column_width=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
                 
                 
if SELECTBOX_SIDEBAR_GENERAL == "GENERAL DISASTERS PORTAL":
    
    
    st.header("NATURAL DISASTERS TRACKING PANEL")
    st.markdown("_CEI was established by ISCI-LAB_")

    
    st.subheader("GLOBAL MAPPING AND INFORMATION")   
    st.markdown("_USE INTERACTIVE MAP_")
    try:
        
        with st.expander("GLOBAL DISASTERS"):
             
             
             TEST_SPEC_TARGET_URL = "https://eonet.sci.gsfc.nasa.gov/api/v3/events"
                    
             READ_URL = requests.get(TEST_SPEC_TARGET_URL)
             READ_JSON = READ_URL.json()
                    
             EVENTS_JSON_2 = READ_JSON["events"]
             
             Event_Name_2 = []
             Event_Latitude_2 = []
             Event_Longitude_2 = []
             Event_Date_2 = []
             
             Event_Name_V = []
             Event_Latitude_V = []
             Event_Longitude_V = []
             Event_Date_V = []
             
             Event_Name_FL = []
             Event_Latitude_FL = []
             Event_Longitude_FL = []
             Event_Date_FL = []
             
             Event_Name_EQ = []
             Event_Latitude_EQ = []
             Event_Longitude_EQ = []
             Event_Date_EQ = []
             
             Event_Name_CY = []
             Event_Latitude_CY = []
             Event_Longitude_CY = []
             Event_Date_CY = []
             
             
             Map_Folium_2 = folium.Map(location=[25.,38.],
                                tiles="Stamen Toner",
                                zoom_start=2.2)
             
             for x_range in range(50):
                        
                 EVENT_TITLE_2 = EVENTS_JSON_2[x_range]["title"]
                 EVENT_DATE_2 = EVENTS_JSON_2[x_range]["geometry"][0]["date"]
                 EVENTS_LAT_2 = EVENTS_JSON_2[x_range]["geometry"][0]["coordinates"][1]
                 EVENTS_LON_2 = EVENTS_JSON_2[x_range]["geometry"][0]["coordinates"][0]
                 
                 TARGET_TYPE_2 = EVENT_TITLE_2.split(" ")
    
                 
                 if "Fire" in TARGET_TYPE_2 or "Fires" in TARGET_TYPE_2 or "Wildfire" in TARGET_TYPE_2 or "Wildfires" in TARGET_TYPE_2\
                    or "Forest" in TARGET_TYPE_2 or "fire" in TARGET_TYPE_2 or "fires" in TARGET_TYPE_2\
                    or "Fire," in TARGET_TYPE_2 or "(Nine', 'Mine', 'Fire)," in TARGET_TYPE_2:
                
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                        Event_Name_2.append(EVENT_TITLE_2)
                        Event_Latitude_2.append(EVENTS_LAT_2)
                        Event_Longitude_2.append(EVENTS_LON_2)
                        Event_Date_2.append(EVENT_DATE_2)
    
                        
                 elif "Volcano" in TARGET_TYPE_2 or "eruption" in TARGET_TYPE_2 or "Volcano," in TARGET_TYPE_2:
                        
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="orange",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                        
                        
                        Event_Name_V.append(EVENT_TITLE_2)
                        Event_Latitude_V.append(EVENTS_LAT_2)
                        Event_Longitude_V.append(EVENTS_LON_2)
                        Event_Date_V.append(EVENT_DATE_2)
    
                        
                 elif "Flood" in TARGET_TYPE_2:
                        
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="blue",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                        
                        Event_Name_FL.append(EVENT_TITLE_2)
                        Event_Latitude_FL.append(EVENTS_LAT_2)
                        Event_Longitude_FL.append(EVENTS_LON_2)
                        Event_Date_FL.append(EVENT_DATE_2)
    
                        
                        
                 elif "Earthquake" in TARGET_TYPE_2:
                        
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="green",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                        
                        Event_Name_EQ.append(EVENT_TITLE_2)
                        Event_Latitude_EQ.append(EVENTS_LAT_2)
                        Event_Longitude_EQ.append(EVENTS_LON_2)
                        Event_Date_EQ.append(EVENT_DATE_2)
    
                        
                 elif "Typhoon" in TARGET_TYPE_2 or "Hurricane" in TARGET_TYPE_2 or "Cyclone" in TARGET_TYPE_2 or "Storm" in TARGET_TYPE_2 or "Subtropical" in TARGET_TYPE_2:
                        
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="purple",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                        Event_Name_CY.append(EVENT_TITLE_2)
                        Event_Latitude_CY.append(EVENTS_LAT_2)
                        Event_Longitude_CY.append(EVENTS_LON_2)
                        Event_Date_CY.append(EVENT_DATE_2)
                        
                        
                        
                 elif "Iceberg" in TARGET_TYPE_2:
                        
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup=f"<h3><b>{EVENT_TITLE_2}</b></h3> - <h4><i><b> {EVENT_DATE_2} / {EVENTS_LAT_2} , {EVENTS_LON_2}</b></i></h4>",
                            tooltip="Show info",
                            icon=folium.Icon(color="darkblue",icon="flag")
                        ).add_to(Map_Folium_2)
                        
                 else:
                
                        folium.Marker(
                            location=[float(EVENTS_LAT_2),float(EVENTS_LON_2)],
                            popup="<b>UNDEFINED</b>",
                            tooltip="Show info"
                        ).add_to(Map_Folium_2)
                
        
             folium.TileLayer('openstreetmap').add_to(Map_Folium_2)
             folium.TileLayer('Stamen Terrain').add_to(Map_Folium_2)
             folium.TileLayer('stamenwatercolor').add_to(Map_Folium_2)
             folium.TileLayer('cartodbpositron').add_to(Map_Folium_2)
             folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_2)
             Map_Folium_2.add_child(folium.LatLngPopup())
             folium.LayerControl().add_to(Map_Folium_2)
            
             folium_static(Map_Folium_2)
    
             
             Name_Series_F = pd.Series(Event_Name_2,name="NAME")
             Latitude_Series_F = pd.Series(Event_Latitude_2,name="LATITUDE")
             Longitude_Series_F = pd.Series(Event_Longitude_2,name="LONGITUDE")
             Date_Series_2_F = pd.Series(Event_Date_2,name="STATUS")
                        
             FIRE_ALT_DATA = pd.concat([Name_Series_F,
                                                   Latitude_Series_F,
                                                   Longitude_Series_F,
                                                   Date_Series_2_F],axis=1)
             
             
             Name_Series_V = pd.Series(Event_Name_V,name="NAME")
             Latitude_Series_V = pd.Series(Event_Latitude_V,name="LATITUDE")
             Longitude_Series_V = pd.Series(Event_Longitude_V,name="LONGITUDE")
             Date_Series_2_V = pd.Series(Event_Date_V,name="STATUS")
                        
             VL_ALT_DATA = pd.concat([Name_Series_V,
                                                   Latitude_Series_V,
                                                   Longitude_Series_V,
                                                   Date_Series_2_V],axis=1)
             
             
             Name_Series_FL = pd.Series(Event_Name_FL,name="NAME")
             Latitude_Series_FL = pd.Series(Event_Latitude_FL,name="LATITUDE")
             Longitude_Series_FL = pd.Series(Event_Longitude_FL,name="LONGITUDE")
             Date_Series_2_FL = pd.Series(Event_Date_FL,name="STATUS")
                        
             FL_ALT_DATA = pd.concat([Name_Series_FL,
                                                   Latitude_Series_FL,
                                                   Longitude_Series_FL,
                                                   Date_Series_2_FL],axis=1)
             
             
             Name_Series_EQ = pd.Series(Event_Name_EQ,name="NAME")
             Latitude_Series_EQ = pd.Series(Event_Latitude_EQ,name="LATITUDE")
             Longitude_Series_EQ = pd.Series(Event_Longitude_EQ,name="LONGITUDE")
             Date_Series_2_EQ = pd.Series(Event_Date_EQ,name="STATUS")
                        
             EQ_ALT_DATA = pd.concat([Name_Series_EQ,
                                                   Latitude_Series_EQ,
                                                   Longitude_Series_EQ,
                                                   Date_Series_2_EQ],axis=1)
             
             
             Name_Series_CY = pd.Series(Event_Name_CY,name="NAME")
             Latitude_Series_CY = pd.Series(Event_Latitude_CY,name="LATITUDE")
             Longitude_Series_CY = pd.Series(Event_Longitude_CY,name="LONGITUDE")
             Date_Series_2_CY = pd.Series(Event_Date_CY,name="STATUS")
                        
             CY_ALT_DATA = pd.concat([Name_Series_CY,
                                                   Latitude_Series_CY,
                                                   Longitude_Series_CY,
                                                   Date_Series_2_CY],axis=1)
             
             
             
        st.subheader("SPECIFIC TYPE AND INFORMATION - PORTAL I")
        
    except:
        
        st.warning('YOU ARE NOT GETTING THIS ERROR DUE TO THE PROGRAM, IT MAY BE A PROBLEM WITH THE INTERNET CONNECTION OR DATA SOURCE. PLEASE WAIT AND TRY AGAIN. YOU WILL BE CONNECTING ANOTHER SOURCE, WAIT!')
        
        
    try:
    
        with st.expander("CYCLONE / STORM / TYPHOON / HURRICANE"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListTc")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            CYC_DATA_FRAME = pd.DataFrame(columns = ['NAME',
                                                     'ATT_1_CYCLONE',
                                                     'ATT_2_CYCLONE',
                                                     'ATT_3_CYCLONE'])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            NA_TAR = CONTROL_VALUE_LIST[3]
                            C_C_TAR = CONTROL_VALUE_LIST[5]
                            C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                            E_V = CONTROL_VALUE_LIST[11]
                            
                            CYC_DATA_FRAME = CYC_DATA_FRAME.append({'NAME' : NA_TAR,
                                                                    'ATT_1_CYCLONE' : C_C_TAR,
                                                                    'ATT_2_CYCLONE' : C_C_TAR_2,
                                                                    'ATT_3_CYCLONE' : E_V}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(CYC_DATA_FRAME)
            

        with st.expander("WILDFIRE"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListWF")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            WF_DATA_FRAME = pd.DataFrame(columns = ['NAME',
                                                     'DATE',
                                                     'DURATION_DAYS',
                                                     'PEOPLE_AFFECTED',
                                                     'BURNED_AREA'])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            NA_TAR = CONTROL_VALUE_LIST[3]
                            C_C_TAR = CONTROL_VALUE_LIST[5]
                            C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                            DATE_TAR_V = CONTROL_VALUE_LIST[9]
                            E_V = CONTROL_VALUE_LIST[11]
                            
                            WF_DATA_FRAME = WF_DATA_FRAME.append({'NAME' : NA_TAR,
                                                                    'DATE' : C_C_TAR,
                                                                    'DURATION_DAYS' : C_C_TAR_2,
                                                                    'PEOPLE_AFFECTED' : DATE_TAR_V,
                                                                    'BURNED_AREA' : E_V}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(WF_DATA_FRAME)
            
        

        with st.expander("DROUGHT"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListDr")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            DR_DATA_FRAME = pd.DataFrame(columns = ['NAME',
                                                     'DETAIL_1',
                                                     'DETAIL_2',
                                                     'DETAIL_3',
                                                     "DETAIL_4"])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            NA_TAR = CONTROL_VALUE_LIST[3]
                            C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                            DATE_TAR_V = CONTROL_VALUE_LIST[9]
                            E_V = CONTROL_VALUE_LIST[11]
                            E_V_2 = CONTROL_VALUE_LIST[13]
                            
                            DR_DATA_FRAME = DR_DATA_FRAME.append({'NAME' : NA_TAR,
                                                                    'DETAIL_1' : C_C_TAR_2,
                                                                    'DETAIL_2' : DATE_TAR_V,
                                                                    'DETAIL_3' : E_V,
                                                                    "DETAIL_4": E_V_2}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(DR_DATA_FRAME)
            

        with st.expander("VOLCANO"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListVo")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            VO_DATA_FRAME = pd.DataFrame(columns = ['NAME',
                                                     'DETAIL_1',
                                                     'DETAIL_2',
                                                     'DETAIL_3',
                                                     'DETAIL_4',
                                                     "DETAIL_5"])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            NA_TAR = CONTROL_VALUE_LIST[3]
                            C_C_TAR = CONTROL_VALUE_LIST[5]
                            C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                            DATE_TAR_V = CONTROL_VALUE_LIST[9]
                            E_V = CONTROL_VALUE_LIST[11]
                            E_V_2 = CONTROL_VALUE_LIST[13]
                            
                            VO_DATA_FRAME = VO_DATA_FRAME.append({'NAME' : NA_TAR,
                                                                    'DETAIL_1' : C_C_TAR,
                                                                    'DETAIL_2' : C_C_TAR_2,
                                                                    'DETAIL_3' : DATE_TAR_V,
                                                                    'DETAIL_4' : E_V,
                                                                    "DETAIL_5": E_V_2}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(VO_DATA_FRAME)
            
            

        with st.expander("FLOOD"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListFl")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            FL_DATA_FRAME = pd.DataFrame(columns = ['DEATH',
                                                     'DISPLACED',
                                                     'LOCATION',
                                                     'DATE'])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            DE_TAR = CONTROL_VALUE_LIST[3]
                            DI_TAR = CONTROL_VALUE_LIST[5]
                            LOC_TAR = CONTROL_VALUE_LIST[7]
                            DATE_TAR_F = CONTROL_VALUE_LIST[9]
                            
                            FL_DATA_FRAME = FL_DATA_FRAME.append({'DEATH' : DE_TAR,
                                                                    'DISPLACED' : DI_TAR,
                                                                    'LOCATION' : LOC_TAR,
                                                                    'DATE' : DATE_TAR_F}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(FL_DATA_FRAME)
    

        with st.expander("EARTHQUAKE"):
            
    
            SOUP_GDACS_FUNCTION = BeautifulSoup(GDACS_TARGET,"html.parser")
            X_DISASTER = SOUP_GDACS_FUNCTION.find_all("div",id="mainListEq")
            
            CONTROL_VALUE_LIST = []
      
            i_count_stop = 0
            
            EQ_DATA_FRAME = pd.DataFrame(columns = ['MAGNITUDE',
                                                     'DEPTH',
                                                     'LAT_TAR',
                                                     'LON_TAR',
                                                     'DATE',
                                                     "EFF_TAR"])
                    
            for x_att in X_DISASTER:
                
                ALERT_DETAIL_LINK = x_att.find_all("a")
                
                for x_detail_link in ALERT_DETAIL_LINK:
                    
                    LINK_AFTER_SITE = str(x_detail_link.get("href"))
          
                    SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                    SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                    SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                
                                
                    if i_count_stop <= 10:
                        
                                    
                        i_count_stop += 1
                                    
                        for x_sub_target in SUB_TARGET_SOUP:
                                         
                            FIND_TR_ALL = x_sub_target.find_all("td")
                                        
                            for x_sub_td in FIND_TR_ALL:
                                ALL_INFO_TEXT = x_sub_td.text
                                CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                
                            MAG_TAR = CONTROL_VALUE_LIST[3]
                            DEP_TAR = CONTROL_VALUE_LIST[5]
                            COOR_LAT_TAR = CONTROL_VALUE_LIST[7].split(",")[0].replace(" ","")
                            COOR_LON_TAR = CONTROL_VALUE_LIST[7].split(",")[1].replace(" ","")
                            DATE_TAR = CONTROL_VALUE_LIST[9]
                            EFF_TAR = CONTROL_VALUE_LIST[11]
                            
                            EQ_DATA_FRAME = EQ_DATA_FRAME.append({'MAGNITUDE' : MAG_TAR,
                                                                    'DEPTH' : DEP_TAR,
                                                                    'LAT_TAR' : COOR_LAT_TAR,
                                                                    'LON_TAR' : COOR_LON_TAR,
                                                                    'DATE' : DATE_TAR,
                                                                    "EFF_TAR": EFF_TAR}, 
                                           ignore_index = True)
                     
                     
                            CONTROL_VALUE_LIST = []
            
            
            st.dataframe(EQ_DATA_FRAME)
        
    except:
            
        st.info('YOU ARE NOT GETTING THIS ERROR DUE TO THE PROGRAM, IT MAY BE A PROBLEM WITH THE INTERNET CONNECTION OR DATA SOURCE. PLEASE WAIT AND TRY AGAIN.')
         

    st.subheader("SPECIFIC TYPE AND INFORMATION - PORTAL II")
    st.markdown("_USE INTERACTIVE MAP_")
    
    try:
    
        with st.expander("CYCLONE"):
                
            st.dataframe(CY_ALT_DATA)
                
        with st.expander("WILDFIRE"):
                
            st.dataframe(FIRE_ALT_DATA)
                
        with st.expander("FLOOD"):
                
            st.dataframe(FL_ALT_DATA)
                
        with st.expander("EARTHQUAKE"):
                
            st.dataframe(EQ_ALT_DATA)
                
        with st.expander("VOLCANO"):
                
            st.dataframe(VL_ALT_DATA)
            
    except:
            
        st.info('YOU ARE NOT GETTING THIS ERROR DUE TO THE PROGRAM, IT MAY BE A PROBLEM WITH THE INTERNET CONNECTION OR DATA SOURCE. PLEASE WAIT AND TRY AGAIN.')

    st.subheader("HOTSPOTS")
    st.markdown("_USE INTERACTIVE MAP_")
    
    try:
        
        with st.expander("CANADA"):
            
            READ_TARGET_CA = pd.read_csv(CANADA_FIRMS)
                
            Map_Folium_CA = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_CA['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_CA['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_CA['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_CA['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_CA['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_CA)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_CA)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_CA)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_CA)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_CA)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_CA)
            Map_Folium_CA.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_CA)
                
            folium_static(Map_Folium_CA)
            
            
        with st.expander("ALASKA"):
            
            READ_TARGET_AL = pd.read_csv(ALASKA_FIRMS)
                
            Map_Folium_AL = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range((len(READ_TARGET_AL))):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_AL['latitude'].tail(3).values[x_loop_range]),float(READ_TARGET_AL['longitude'].tail(3).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_AL['frp'].tail(3).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_AL['brightness_2'].tail(3).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_AL['acq_datetime'].tail(3).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_AL)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_AL)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_AL)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_AL)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_AL)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_AL)
            Map_Folium_AL.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_AL)
                
            folium_static(Map_Folium_AL)
            
        with st.expander("USA CONT AND HAWAII"):
            
            READ_TARGET_UCH = pd.read_csv(USA_CON_HAWAII_FIRMS)
                
            Map_Folium_UCH = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_UCH['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_UCH['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_UCH['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_UCH['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_UCH['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_UCH)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_UCH)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_UCH)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_UCH)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_UCH)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_UCH)
            Map_Folium_UCH.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_UCH)
                
            folium_static(Map_Folium_UCH)
            
            
        with st.expander("CENTRAL AMERICA"):
            
            READ_TARGET_CAME = pd.read_csv(CENTRAL_AMERICA_FIRMS)
                
            Map_Folium_CAME = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_CAME['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_CAME['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_CAME['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_CAME['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_CAME['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_CAME)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_CAME)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_CAME)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_CAME)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_CAME)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_CAME)
            Map_Folium_CAME.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_CAME)
                
            folium_static(Map_Folium_CAME)
            
        with st.expander("SOUTH AMERICA"):
            
            READ_TARGET_SOAME = pd.read_csv(SOUTH_AMERICA_FIRMS)
                
            Map_Folium_SOAME = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_SOAME['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_SOAME['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_SOAME['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_SOAME['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_SOAME['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_SOAME)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_SOAME)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_SOAME)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_SOAME)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_SOAME)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_SOAME)
            Map_Folium_SOAME.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_SOAME)
                
            folium_static(Map_Folium_SOAME)
            
        with st.expander("EUROPE"):
            
            READ_TARGET_EU = pd.read_csv(EUROPE_FIRMS)
                
            Map_Folium_EU = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_EU['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_EU['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_EU['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_EU['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_EU['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_EU)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_EU)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_EU)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_EU)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_EU)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_EU)
            Map_Folium_EU.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_EU)
                
            folium_static(Map_Folium_EU)
            
        with st.expander("NORTHERN AND CENTRAL AFRICA"):
            
            READ_TARGET_NCAFR = pd.read_csv(NORTHERN_CENTRAL_AFRICA_FIRMS)
                
            Map_Folium_NCAFR = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_NCAFR['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_NCAFR['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_NCAFR['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_NCAFR['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_NCAFR['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_NCAFR)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_NCAFR)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_NCAFR)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_NCAFR)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_NCAFR)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_NCAFR)
            Map_Folium_NCAFR.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_NCAFR)
                
            folium_static(Map_Folium_NCAFR)
            
            
        with st.expander("SOUTHERN AFRICA"):
            
            READ_TARGET_SHAFR = pd.read_csv(SOUTHERN_AFRICA_FIRMS)
                
            Map_Folium_SHAFR = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_SHAFR['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_SHAFR['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_SHAFR['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_SHAFR['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_SHAFR['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_SHAFR)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_SHAFR)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_SHAFR)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_SHAFR)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_SHAFR)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_SHAFR)
            Map_Folium_SHAFR.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_SHAFR)
                
            folium_static(Map_Folium_SHAFR)
            
            
        with st.expander("SOUTH ASIA REGION"):
            
            READ_TARGET_SOAS = pd.read_csv(SOUTH_ASIA_FIRMS)
                
            Map_Folium_SOAS = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_SOAS['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_SOAS['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_SOAS['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_SOAS['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_SOAS['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_SOAS)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_SOAS)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_SOAS)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_SOAS)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_SOAS)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_SOAS)
            Map_Folium_SOAS.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_SOAS)
                
            folium_static(Map_Folium_SOAS)
            
        with st.expander("RUSSIA AND ASIA REGION"):
            
            READ_TARGET_RAA = pd.read_csv(RUSSIA_ASIA_FIRMS)
                
            Map_Folium_RAA = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_RAA['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_RAA['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_RAA['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_RAA['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_RAA['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_RAA)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_RAA)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_RAA)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_RAA)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_RAA)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_RAA)
            Map_Folium_RAA.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_RAA)
                
            folium_static(Map_Folium_RAA)
            
            
        with st.expander("SOUTHEAST ASIA"):
            
            READ_TARGET_SOEAS = pd.read_csv(SOUTHEAST_ASIA_FIRMS)
                
            Map_Folium_SOEAS = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_SOEAS['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_SOEAS['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_SOEAS['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_SOEAS['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_SOEAS['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_SOEAS)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_SOEAS)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_SOEAS)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_SOEAS)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_SOEAS)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_SOEAS)
            Map_Folium_SOEAS.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_SOEAS)
                
            folium_static(Map_Folium_SOEAS)
            
            
        with st.expander("AUSTRALIA AND NEW-ZEALAND REGION"):
            
            READ_TARGET_ASNEZ = pd.read_csv(AUSTRALIA_NEWZEALAND_FIRMS)
                
            Map_Folium_ASNEZ = folium.Map(location=[25.,38.],
                            tiles="Stamen Toner",
                            zoom_start=2.0)
    
            for x_loop_range in range(80):
                
                
                folium.Marker(
                        location=[float(READ_TARGET_ASNEZ['latitude'].tail(80).values[x_loop_range]),float(READ_TARGET_ASNEZ['longitude'].tail(80).values[x_loop_range])],
                        popup=f"<h3><b>FRP: {READ_TARGET_ASNEZ['frp'].tail(80).values[x_loop_range]}</b></h3> - <h4><i><b> BRIGHTNESS: {READ_TARGET_ASNEZ['brightness_2'].tail(80).values[x_loop_range]}</b></i></h4> - <h5><i><b> DATE: {READ_TARGET_ASNEZ['acq_datetime'].tail(80).values[x_loop_range]}</b></i></h5>",
                        tooltip="Show info",
                        icon=folium.Icon(color="red",icon="flag")
                        ).add_to(Map_Folium_ASNEZ)
                
                
            folium.TileLayer('openstreetmap').add_to(Map_Folium_ASNEZ)
            folium.TileLayer('Stamen Terrain').add_to(Map_Folium_ASNEZ)
            folium.TileLayer('stamenwatercolor').add_to(Map_Folium_ASNEZ)
            folium.TileLayer('cartodbpositron').add_to(Map_Folium_ASNEZ)
            folium.TileLayer('cartodbdark_matter').add_to(Map_Folium_ASNEZ)
            Map_Folium_ASNEZ.add_child(folium.LatLngPopup())
            folium.LayerControl().add_to(Map_Folium_ASNEZ)
                
            folium_static(Map_Folium_ASNEZ)
        
    except:
        
        st.warning('YOU ARE NOT GETTING THIS ERROR DUE TO THE PROGRAM, IT MAY BE A PROBLEM WITH THE INTERNET CONNECTION OR DATA SOURCE. PLEASE WAIT AND TRY AGAIN. YOU WILL BE CONNECTING ANOTHER SOURCE, WAIT!')
        

        

if SELECTBOX_SIDEBAR_GENERAL == "CYCLONE - FLOOD":
    
    
    st.header("CYCLONE AND FLOOD TRACKING PANEL")
    st.markdown("**All satellite images are in real time. You can detect the formations by enlarging the images**")
    st.markdown("_CEI was established by ISCI-LAB_")
    
    st.subheader("PRECIPITABLE WATER")
    st.markdown("**LATEST RELEASE**")
    try:
        
        st.markdown("![MAP](http://tropic.ssec.wisc.edu/real-time/mtpw2/webAnims/tpw_nrl_colors/global/mimictpw_global_latest.gif)")
    except:
        st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN.")
        
    
    st.subheader("LATEST REPORT")
    
    with st.expander("CLICK TO CHECK REPORT"):
        try:
            
            TARGET_REQ_URL = "https://www.cyclocane.com/tropical-storm-risk/"
    
            REQ_TARGET = requests.get(TARGET_REQ_URL).text
            SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
            
            FIND_ALL_PRE = SOUP_TARGET.find_all("pre")
            
            LIST_ALL_RES = []
            
            for x_loop in FIND_ALL_PRE:
                
                CLEAR_OUT = x_loop.text.replace("$$","---"*10).replace("000","")
                LIST_ALL_RES.append(CLEAR_OUT)
                
            for x_num_in,x_list_in in enumerate(LIST_ALL_RES):
                
                st.text(LIST_ALL_RES[x_num_in])
            
        except:
            st.info("DATA IS NOT ACTIVE, PLEASE WAIT AND TRY AGAIN.")
        
    try:
        
        MET_HR_HREF = '<iframe src="https://www.meteoblue.com/en/weather/maps/widget?windAnimation=0&windAnimation=1&gust=0&gust=1&satellite=0&satellite=1&geoloc=detect&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=1&autowidth=auto"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 100%; height: 720px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/en/weather/maps/index?utm_source=weather_widget&utm_medium=linkus&utm_content=map&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>'
        
        st.subheader("INTERACTIVE MAP")
        st.markdown(MET_HR_HREF,unsafe_allow_html=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
    
    
    st.subheader("GENERAL TROPICAL REPORT")

        
    st.markdown("**It shows the pressure points in real time**")
    st.markdown("**EASTERN REGION**")
    try:
        
        RR_IRBW_IMAGE = Image.open(requests.get("https://www.metoc.navy.mil/jtwc/products/abpwsair.jpg",
                     stream=True).raw)
            
        st.image(RR_IRBW_IMAGE)
            
    except:
            
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
    

    st.markdown("**WESTERN REGION**")
    col_w_r_1,col_w_r_2 = st.columns(2)
    
    with col_w_r_1:
        
        st.markdown("_PART I_")
        try:
        
            RR_WERE_IMAGE = Image.open(requests.get("https://www.nhc.noaa.gov/xgtwo/two_pac_5d0.png",
                         stream=True).raw)
                
            st.image(RR_WERE_IMAGE)
            
        except:
                
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
            
        
    with col_w_r_2:
        
        st.markdown("_PART II_")
        try:
            
            RR_WERE_2_IMAGE = Image.open(requests.get("https://www.nhc.noaa.gov/xgtwo/two_atl_5d0.png",
                         stream=True).raw)
                
            st.image(RR_WERE_2_IMAGE)
                
        except:
                
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
    
    
    st.subheader("WAVELENGTHS")
    st.markdown("IR - BW")
    
    col_w1, col_w2, col_w3, col_w4, col_w5, col_w6 = st.columns(6)
    
    with col_w1:
        
        try:
        
            W1_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_a.jpg",
                     stream=True).raw)
            
            st.image(W1_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_w2:
        
        try:
        
            W2_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_b1.jpg",
                     stream=True).raw)
            
            st.image(W2_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_w3:
        
        try:
        
            W3_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_c.jpg",
                     stream=True).raw)
            
            st.image(W3_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_w4:
        
        try:
        
            W4_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_d.jpg",
                     stream=True).raw)
            
            st.image(W4_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_w5:
        
        try:
            
            W5_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_e.jpg",
                     stream=True).raw)
            
            st.image(W5_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_w6:
        
        try:
        
            W6_IRBW_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irbw_f.jpg",
                     stream=True).raw)
            
            st.image(W6_IRBW_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
        

    st.markdown("IR - COLOR")
    
    col_wc1, col_wc2, col_wc3, col_wc4, col_wc5, col_wc6 = st.columns(6)
    
    with col_wc1:
        
        try:
        
            W1_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_a.jpg",
                     stream=True).raw)
            
            st.image(W1_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wc2:
        
        try:
        
            W2_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_b1.jpg",
                     stream=True).raw)
            
            st.image(W2_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wc3:
        
        try:
        
            W3_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_c.jpg",
                     stream=True).raw)
            
            st.image(W3_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wc4:
        
        try:
        
            W4_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_d.jpg",
                     stream=True).raw)
            
            st.image(W4_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wc5:
        
        try:
            
            W5_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_e.jpg",
                     stream=True).raw)
            
            st.image(W5_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wc6:
        
        try:
        
            W6_IRC_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_ircol_f.jpg",
                     stream=True).raw)
            
            st.image(W6_IRC_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
    
    
    st.markdown("IR - WS")
    
    col_ws1, col_ws2, col_ws3, col_ws4, col_ws5, col_ws6 = st.columns(6)
    
    with col_ws1:
        
        try:
        
            W1_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_a.jpg",
                     stream=True).raw)
            
            st.image(W1_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_ws2:
        
        try:
        
            W2_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_b1.jpg",
                     stream=True).raw)
            
            st.image(W2_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_ws3:
        
        try:
        
            W3_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_c.jpg",
                     stream=True).raw)
            
            st.image(W3_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_ws4:
        
        try:
        
            W4_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_d.jpg",
                     stream=True).raw)
            
            st.image(W4_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_ws5:
        
        try:
            
            W5_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_e.jpg",
                     stream=True).raw)
            
            st.image(W5_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_ws6:
        
        try:
        
            W6_IRS_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_irnws_f.jpg",
                     stream=True).raw)
            
            st.image(W6_IRS_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")

    

    st.markdown("WATER VAPOR")
    
    col_wp1, col_wp2, col_wp3, col_wp4, col_wp5, col_wp6 = st.columns(6)
    
    with col_wp1:
        
        try:
        
            W1_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_a.jpg",
                     stream=True).raw)
            
            st.image(W1_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wp2:
        
        try:
        
            W2_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_b1.jpg",
                     stream=True).raw)
            
            st.image(W2_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wp3:
        
        try:
        
            W3_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_c.jpg",
                     stream=True).raw)
            
            st.image(W3_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wp4:
        
        try:
        
            W4_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_d.jpg",
                     stream=True).raw)
            
            st.image(W4_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wp5:
        
        try:
            
            W5_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_e.jpg",
                     stream=True).raw)
            
            st.image(W5_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")
        
    with col_wp6:
        
        try:
        
            W6_IRP_IMAGE = Image.open(requests.get("https://aviationweather.gov/data/obs/sat/intl/sat_wv_f.jpg",
                     stream=True).raw)
            
            st.image(W6_IRP_IMAGE)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE TRY AGAIN.")




if SELECTBOX_SIDEBAR_GENERAL == "VOLCANO - EARTHQUAKE":
    
    
    st.header("VOLCANO AND EARTHQUAKE TRACKING PANEL")
    st.markdown("_CEI was established by ISCI-LAB_")
    
    st.subheader("GENERAL MAP")
    
    try:
        
        VOL_EAR_HREF = """<!-- begin VolcanoWidget -->
<div id="VW_bigMap" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;z-index:999999;">
<div id="VW_backDiv" style="background:#000;filter:alpha(opacity=80);opacity:.8;height:100%;width:100%;position:absolute;top:0px;left:0px;z-index:-1;" onclick="switchFrame('VW_smallMap','VW_bigMap','enlarge','small map','600px','500px',0,-180);return false;"></div></div>
<div id="VW_smallMap" style="clear:left"><div id="VW_mCont" style="width:800px;height:800px;position:relative;margin:0;background:#fff;"><a name="VW_mCont"></a><div style="position:absolute;top:8px;right:28px;height:15px;text-align:right;vertical-align:middle;font:12px Verdana,sans-serif;font-weight:bold">[<a href="#" style="color:#bb202a" onclick="switchFrame('VW_smallMap','VW_bigMap','enlarge','small map','600px','500px',0,-180);return false;"><span id="VW_mSwitch">enlarge</span></a>]</div><iframe id="VW_iframe" width="100%" height="100%" scrolling="no" frameborder="0" marginwidth="0" marginheight="0" src="https://earthquakes.volcanodiscovery.com?title=VOLCANO%20AND%20EARTHQUAKE%20TRACKING&terrain=1&minMag=6&maxAge=24h"></iframe></div></div>
<script type="text/javascript">function switchFrame(a,b,c,d,e,f,g,h){var i=document.getElementById("VW_mCont");var j=document.getElementById("VW_mSwitch").firstChild;if(j.nodeValue==c){j.nodeValue=d}else{j.nodeValue=c}var k=i.parentNode.getAttribute("id");if(k==a){var l=b}else{var l=a}var m=i.parentNode;var n=document.getElementById(l);n.appendChild(i);m.style.display="none";n.style.display="";if(l==a){i.style.width=e;i.style.height=f;i.style.margin=0;i.style.top=""}else{i.style.width="80%";i.style.height="80%";i.style.margin="auto";i.style.top="20px"}window.location.hash="VW_mCont"}</script>
<!-- end VolcanoWidget / http://www.volcano-news.com/active-volcanoes-map/get-widget.html -->"""

        st.markdown(VOL_EAR_HREF,unsafe_allow_html=True)
        
    except:
        
        st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
    
    st.subheader("VOLCANO REPORT")
    with st.expander("CLICK TO CHECK VOLCANO REPORT"):
        
        try:
            
            Event_Name = []
            Event_Desc = []
            Event_Coor = []
                
            TARGET_REQ_URL = "https://volcano.si.edu/news/WeeklyVolcanoRSS.xml"
        
            REQ_TARGET = requests.get(TARGET_REQ_URL).text
            SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
                
            FIND_ALL_ITE = SOUP_TARGET.find_all("item")
                
    
            for x_loop in FIND_ALL_ITE:
                    
                TITLE_OUT = x_loop.find("title")
                DES_OUT = x_loop.find("description")
                COOR_OUT = x_loop.find("georss:point")
                    
                Event_Name.append(TITLE_OUT.text)
                Event_Desc.append(DES_OUT.text.replace("<p>","").replace("</p>",""))
                Event_Coor.append(COOR_OUT.text.replace("<p>","").replace("</p>",""))
                
            Name_V_Series = pd.Series(Event_Name,name="TITLE")
            DES_V_Series = pd.Series(Event_Desc,name="DESCRIPTION")
            COOR_V_Series = pd.Series(Event_Coor,name="COORDINATE")
                    
            VO_REP_DATA = pd.concat([Name_V_Series,DES_V_Series,COOR_V_Series],axis=1)
            
            st.table(VO_REP_DATA)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
            
    st.subheader("SEISMIC REPORT")
    with st.expander("CLICK TO CHECK SEISMIC REPORT"):
        
        try:
            
            EV_REG = []
            EV_LAT = []
            EV_LON = []
            EV_DEPT = []
            EV_MAG_VAL = []
            EV_MAG_TYPE = []
            EV_TIME = []
            EV_F_COUNT = []
            
            TARGET_REQ_URL = "https://www.seismicportal.eu/mtws/api/search?&format=json&downloadAsFile=false&orderby=time-desc&offset=0&limit=50"


            READ_URL = requests.get(TARGET_REQ_URL)
            READ_JSON = READ_URL.json()
        
            for x_num in range(len(READ_JSON)):
        
                NEW_JSON = READ_JSON[x_num]
 
                EV_REG.append(NEW_JSON["ev_region"])
                EV_LAT.append(NEW_JSON["ev_latitude"])
                EV_LON.append(NEW_JSON["ev_longitude"])
                EV_DEPT.append(NEW_JSON["ev_depth"])
                EV_MAG_VAL.append(NEW_JSON["ev_mag_value"])
                EV_MAG_TYPE.append(NEW_JSON["ev_mag_type"])
                EV_TIME.append(NEW_JSON["ev_event_time"])
                EV_F_COUNT.append(NEW_JSON["full_count"])
                
                
            Reg_Series = pd.Series(EV_REG,name="REGION")
            Lat_Series = pd.Series(EV_LAT,name="LAT")
            Lon_Series = pd.Series(EV_LON,name="LON")
            Dep_Series = pd.Series(EV_DEPT,name="DEPTH")
            Mag_V_Series = pd.Series(EV_MAG_VAL,name="MAGNITUDE")
            Mag_T_Series = pd.Series(EV_MAG_TYPE,name="MAG TYPE")
            T_Series = pd.Series(EV_TIME,name="TIME")
            FC_Series = pd.Series(EV_F_COUNT,name="COUNT")
                    
            SE_D_REP_DATA = pd.concat([Reg_Series,
                                     Lat_Series,
                                     Lon_Series,
                                     Dep_Series,
                                     Mag_V_Series,
                                     Mag_T_Series,
                                     T_Series,
                                     FC_Series],axis=1)
            
            st.table(SE_D_REP_DATA)
            
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")


if SELECTBOX_SIDEBAR_GENERAL == "INTERACTIVE SEARCHING":
    
    
    st.header("INTERACTIVE SEARCHING PANEL")
    st.markdown("_CEI was established by ISCI-LAB_")
    
    TOTAL_SUM_SEARCH_RATIO = st.radio("SELECT YOUR OPERATION",("GENERAL DISASTER CHECKING",
                                                               "EARTHQUAKE CHECKING",
                                                               "REAL TIME MAPPING FOR HOTPOINTS",
                                                               "WEATHER QUALITY BY COORDINATE"))
    
    
    if TOTAL_SUM_SEARCH_RATIO == "GENERAL DISASTER CHECKING":

        try:
            
            st.subheader("GENERAL DISASTER CHECKING")
            st.write("Please define your desired coordinate as latitude-longitude format. Press enter after each entry.")
            
            Latitude_Target = st.number_input('LATITUDE', -91., 91.,90., step=1., format="%.6f")
            st.write("**YOUR LATITUDE TARGET**: ", Latitude_Target)
           
        
            Longitude_Target = st.number_input('LONGITUDE', -181., 181.,-180., step=1., format="%.6f")
            st.write("**YOUR LONGITUDE TARGET**: ", Longitude_Target)
            
        
            BUT_GENERAL = st.button('LAUNCH')
            
            if BUT_GENERAL:
                
                POR_BAR = st.progress(0)

                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
    
                url='https://emergency.copernicus.eu/mapping/activations-rapid/feed'
                
                MAIN_URL = feedparser.parse(url)
                ENTRIES = MAIN_URL["entries"]
        
                TARGET_LAT = Latitude_Target
                TARGET_LON = Longitude_Target
         
                checking_value = 0
                            
                for x_range in range(len(ENTRIES)):
                        
                    CONTROL_ENTRIES = ENTRIES[x_range]
                                
                    NAME_TARGET = CONTROL_ENTRIES["iwgsem_activationname"].split("]")[1]
                    LAT_TARGET = CONTROL_ENTRIES["iwgsem_activationlocation"].split(" ")[0]
                    LON_TARGET = CONTROL_ENTRIES["iwgsem_activationlocation"].split(" ")[1]
                    DATE_TARGET = CONTROL_ENTRIES["iwgsem_activationpublished"]
                    STATUS_TARGET = CONTROL_ENTRIES["iwgsem_activationstatus"]
                                
                    if TARGET_LAT == LAT_TARGET and TARGET_LON == LON_TARGET:
                                    
                        st.success("**FOUND**")
                        st.markdown("**NAME**: " + NAME_TARGET)
                        st.markdown("**LATITUDE**: " + LAT_TARGET)
                        st.markdown("**LONGITUDE**: " + LON_TARGET)
                        st.markdown("**DATE**: " + DATE_TARGET)
                        st.markdown("**STATUS**: " + STATUS_TARGET)
                        checking_value += 1
                        
        
         
                    elif "%.2f"%float(TARGET_LAT) == "%.2f"%float(LAT_TARGET) and "%.2f"%float(TARGET_LON) == "%.2f"%float(LON_TARGET):
                        
                        st.success("**FOUND**")
                        st.markdown("**NAME**: " + NAME_TARGET)
                        st.markdown("**LATITUDE**: " + LAT_TARGET)
                        st.markdown("**LONGITUDE**: " + LON_TARGET)
                        st.markdown("**DATE**: " + DATE_TARGET)
                        st.markdown("**STATUS**: " + STATUS_TARGET)
                        checking_value += 1
                        
        
                                    
                    elif "%.f"%float(TARGET_LAT) == "%.f"%float(LAT_TARGET) and "%.f"%float(TARGET_LON) == "%.f"%float(LON_TARGET):
                                    
                        st.success("**FOUND**")
                        st.markdown("**NAME**: " + NAME_TARGET)
                        st.markdown("**LATITUDE**: " + LAT_TARGET)
                        st.markdown("**LONGITUDE**: " + LON_TARGET)
                        st.markdown("**DATE**: " + DATE_TARGET)
                        st.markdown("**STATUS**: " + STATUS_TARGET)
                        checking_value += 1
                        
                        
                    elif int(float(TARGET_LAT)) == int(float(LAT_TARGET)) and int(float(TARGET_LON)) == int(float(LON_TARGET)):
                                    
                        st.success("**FOUND**")
                        st.markdown("**NAME**: " + NAME_TARGET)
                        st.markdown("**LATITUDE**: " + LAT_TARGET)
                        st.markdown("**LONGITUDE**: " + LON_TARGET)
                        st.markdown("**DATE**: " + DATE_TARGET)
                        st.markdown("**STATUS**: " + STATUS_TARGET)
                        checking_value += 1
                        
        
        
                    
                if checking_value <= 0:
                    
                    st.info("THERE IS NO DISASTER")
                    
        except:
                
            st.warning("CHECK YOUR PROCESS AND TRY AGAIN")
            

    elif TOTAL_SUM_SEARCH_RATIO == "EARTHQUAKE CHECKING":
        
        st.subheader("EARTHQUAKE CHECKING")
        st.write("Please define your desired coordinate as latitude-longitude format. Press enter after each entry.")
        
        st.image(IMAGE_PATH_EQ_SEI)
        
        
            
        Latitude_Target_EQ = st.number_input('LATITUDE EQ', -91., 91.,90., step=1., format="%.6f")
        st.write("**YOUR LATITUDE TARGET**: ", Latitude_Target_EQ)
        
        
        Longitude_Target_EQ = st.number_input('LONGITUDE EQ', -181., 181.,-180., step=1., format="%.6f")
        st.write("**YOUR LONGITUDE TARGET**: ", Longitude_Target_EQ)
        
    
        BUT_EQ = st.button('LAUNCH EQ')
        
        
        
        if BUT_EQ:
            
            POR_BAR = st.progress(0)

            for percent_index in range(100):
                time.sleep(0.1)
                POR_BAR.progress(percent_index + 1)
            
            try:
            
            
                TARGET_LAT_EQ = Latitude_Target_EQ
                TARGET_LON_EQ = Longitude_Target_EQ
        
                url='https://ds.iris.edu/seismon/eventlist/index.phtml'
        
                MAIN_URL = requests.get(url).text
                MAIN_SOUP = BeautifulSoup(MAIN_URL,"html.parser")
                MATER_ALL = MAIN_SOUP.find_all("table",class_="tablesorter")
                    
                i_count_stop = 0
                checking_value_2 = 0
                
                for X_DETAIL in MATER_ALL:
                    
                    DETAIL_TR = X_DETAIL.find_all("tr")
                    
                    for x_det in DETAIL_TR:
                        
                        LIST_DETAIL = x_det.text.replace("\n",",").split(",")
                        i_count_stop += 1
                        
                        if 1 < i_count_stop:
        
                            if TARGET_LAT_EQ == LIST_DETAIL[2] and TARGET_LON_EQ == LIST_DETAIL[3]:
                                                
                                    st.success("**FOUND**")
                                    st.markdown("**MAGNITUDE**: " + LIST_DETAIL[4])
                                    st.markdown("**LATITUDE**: " + LIST_DETAIL[2])
                                    st.markdown("**LONGITUDE**: " + LIST_DETAIL[3])
                                    st.markdown("**DATE**: " + LIST_DETAIL[1])
                                    st.markdown("**DEPTH**: " + LIST_DETAIL[5])
                                    checking_value_2 += 1
                                    
                    
                     
                            elif "%.2f"%float(TARGET_LAT_EQ) == "%.2f"%float(LIST_DETAIL[2]) and "%.2f"%float(TARGET_LON_EQ) == "%.2f"%float(LIST_DETAIL[3]):
                                    
                                    st.success("**FOUND**")
                                    st.markdown("**MAGNITUDE**: " + LIST_DETAIL[4])
                                    st.markdown("**LATITUDE**: " + LIST_DETAIL[2])
                                    st.markdown("**LONGITUDE**: " + LIST_DETAIL[3])
                                    st.markdown("**DATE**: " + LIST_DETAIL[1])
                                    st.markdown("**DEPTH**: " + LIST_DETAIL[5])
                                    checking_value_2 += 1
                                    
                    
                                                
                            elif "%.f"%float(TARGET_LAT_EQ) == "%.f"%float(LIST_DETAIL[2]) and "%.f"%float(TARGET_LON_EQ) == "%.f"%float(LIST_DETAIL[3]):
                                                
                                    st.success("**FOUND**")
                                    st.markdown("**MAGNITUDE**: " + LIST_DETAIL[4])
                                    st.markdown("**LATITUDE**: " + LIST_DETAIL[2])
                                    st.markdown("**LONGITUDE**: " + LIST_DETAIL[3])
                                    st.markdown("**DATE**: " + LIST_DETAIL[1])
                                    st.markdown("**DEPTH**: " + LIST_DETAIL[5])
                                    checking_value_2 += 1
                                    
                                    
                            elif int(float(TARGET_LAT_EQ)) == int(float(LIST_DETAIL[2])) and int(float(TARGET_LON_EQ)) == int(float(LIST_DETAIL[3])):
                                                
                                    st.success("**FOUND**")
                                    st.markdown("**MAGNITUDE**: " + LIST_DETAIL[4])
                                    st.markdown("**LATITUDE**: " + LIST_DETAIL[2])
                                    st.markdown("**LONGITUDE**: " + LIST_DETAIL[3])
                                    st.markdown("**DATE**: " + LIST_DETAIL[1])
                                    st.markdown("**DEPTH**: " + LIST_DETAIL[5])
                                    checking_value_2 += 1
                                    
                    
                    
                                
                    if checking_value_2 <= 0:
                                
                        st.info("THERE IS NO DISASTER")
                        
            except:
                
                st.warning("CHECK YOUR PROCESS AND TRY AGAIN")
        
            

    elif TOTAL_SUM_SEARCH_RATIO == "REAL TIME MAPPING FOR HOTPOINTS":
        
        st.subheader("REAL TIME MAPPING - HOTPOINTS")
        
        try:
        
            st.write("Please define your desired coordinate as polygonal. Press enter after each entry.")
            
        
            Min_Latitude_Target_HP = st.number_input('MIN LATITUDE HP', -91., 91.,90., step=1., format="%.6f")
            st.write("**YOUR MIN LATITUDE TARGET**: ", Min_Latitude_Target_HP)
            
            Max_Latitude_Target_HP = st.number_input('MAX LATITUDE HP', -91., 91.,90., step=1., format="%.6f")
            st.write("**YOUR MAX LATITUDE TARGET**: ", Max_Latitude_Target_HP)
            
            Min_Longitude_Target_HP = st.number_input('MIN LONGITUDE HP', -181., 181.,180., step=1., format="%.6f")
            st.write("**YOUR MIN LONGITUDE TARGET**: ", Min_Longitude_Target_HP)
            
            Max_Longitude_Target_HP = st.number_input('MAX LONGITUDE HP', -181., 181.,180., step=1., format="%.6f")
            st.write("**YOUR MAX LONGITUDE TARGET**: ", Max_Longitude_Target_HP)
        
            
            BUT_COL_1, BUT_COL_2 = st.columns(2)
            
            with BUT_COL_1:
                
                
                st.markdown("_MODIS TERRA CORRECTED LIVE IMAGE - SATALLITE_")
                BUT_HP = st.button('LAUNCH TRUE COLOR HP')
        
                if BUT_HP:
                    
                    POR_BAR = st.progress(0)

                    for percent_index in range(100):
                        time.sleep(0.1)
                        POR_BAR.progress(percent_index + 1)
                    
                    IMAGE_PATH_URL = f"https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&LAYERS=MODIS_Terra_CorrectedReflectance_TrueColor,MODIS_Terra_Thermal_Anomalies_Day,Coastlines_15m,Reference_Features_15m&CRS=EPSG:4326&TIME=P0D&WRAP=DAY,DAY,X,X&BBOX={Min_Latitude_Target_HP},{Min_Longitude_Target_HP},{Max_Latitude_Target_HP},{Max_Longitude_Target_HP}&FORMAT=image/jpeg&WIDTH=1020&HEIGHT=520&AUTOSCALE=FALSE&ts=1635071104955"
                    
                    TAR_MAPPING_IMAGE = Image.open(requests.get(IMAGE_PATH_URL,stream=True).raw)
                    st.image(TAR_MAPPING_IMAGE)
                
                
                
            with BUT_COL_2:
                
                
                st.markdown("_VIIRS SNPP NIGHT THERMAL LIVE IMAGE - SATALLITE_")
                BUT_THE_HP = st.button('LAUNCH NIGHT THERMAL HP')
                
                if BUT_THE_HP:
                    
                    POR_BAR = st.progress(0)

                    for percent_index in range(100):
                        time.sleep(0.1)
                        POR_BAR.progress(percent_index + 1)
                
                    IMAGE_THERM_URL = f"https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&LAYERS=VIIRS_SNPP_DayNightBand_At_Sensor_Radiance,VIIRS_SNPP_Thermal_Anomalies_375m_Night,Coastlines_15m,Reference_Features_15m&CRS=EPSG:4326&TIME=P0D&WRAP=DAY,DAY,X,X&BBOX={Min_Latitude_Target_HP},{Min_Longitude_Target_HP},{Max_Latitude_Target_HP},{Max_Longitude_Target_HP}&FORMAT=image/jpeg&WIDTH=920&HEIGHT=464&AUTOSCALE=TRUE&ts=1636363415330"
                     
                    NIG_TAR_MAPPING_IMAGE = Image.open(requests.get(IMAGE_THERM_URL,stream=True).raw)
                    st.image(NIG_TAR_MAPPING_IMAGE)
            
        
        except:
            st.warning("CHECK YOUR PROCESS AND TRY AGAIN")
        
        
        
    if TOTAL_SUM_SEARCH_RATIO == "WEATHER QUALITY BY COORDINATE":
        

        try:
            
            st.subheader("WEATHER QUALITY CHECKING")
            st.write("Please define your desired coordinate as latitude-longitude format. Press enter after each entry.")
            
            Latitude_Target_WQ_C = st.number_input('LATITUDE WQC', -91., 91.,90., step=1., format="%.6f")
            st.write("**YOUR LATITUDE TARGET**: ", Latitude_Target_WQ_C)
            
            
            Longitude_Target_WQ_C = st.number_input('LONGITUDE WQC', -181., 181.,-180., step=1., format="%.6f")
            st.write("**YOUR LONGITUDE TARGET**: ", Longitude_Target_WQ_C)
            
            
            FORECAST_REQ_AIR = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={Latitude_Target_WQ_C}&lon={Longitude_Target_WQ_C}&appid=d8d908d1b885dd48feac38f4968e737d")
            
            GENERAL_AIR = FORECAST_REQ_AIR.json()
            MAIN_TARGET_AIR_LIST = GENERAL_AIR["list"][0]
              
            BUT_WQC = st.button('LAUNCH WQC')
            
            
            if BUT_WQC:
                
                POR_BAR = st.progress(0)

                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
                
                CO_WQC = MAIN_TARGET_AIR_LIST['components']['co']
                NO_WQC = MAIN_TARGET_AIR_LIST['components']['no']
                NO2_WQC = MAIN_TARGET_AIR_LIST['components']['no2']
                O3_WQC = MAIN_TARGET_AIR_LIST['components']['o3']
                SO2_WQC = MAIN_TARGET_AIR_LIST['components']['so2']
                PM25_WQC = MAIN_TARGET_AIR_LIST['components']['pm2_5']
                PM10_WQC = MAIN_TARGET_AIR_LIST['components']['pm10']
                NH3_WQC = MAIN_TARGET_AIR_LIST['components']['nh3']
                
                
                st.success("**FOUND**")
                st.markdown("**CARBON MONOXIDE -μg/m3**: " + str(CO_WQC))
                st.markdown("**NITROGEN MONOXIDE -μg/m3**: " + str(NO_WQC))
                st.markdown("**NITROGEN DIOXIDE -μg/m3**: " + str(NO2_WQC))
                st.markdown("**OZONE -μg/m3**: " + str(O3_WQC))
                st.markdown("**SULPHUR dioxide -μg/m3**: " + str(SO2_WQC))
                st.markdown("**FINE PARTICULATE pm2.5**: " + str(PM25_WQC))
                st.markdown("**COARSE PARTICULATE MATTER**: " + str(PM10_WQC))
                st.markdown("**AMMONIA -μg/m3**: " + str(NH3_WQC))
                
            
                
        except:
            
            st.warning("CHECK YOUR PROCESS AND TRY AGAIN")
            

                
if SELECTBOX_SIDEBAR_GENERAL == "LOCAL ALERT":
    
    COL_IMA,COL_HEA = st.columns(2)
    
    with COL_IMA:
        
        st.header("CEI")
        
    with COL_HEA:
        
        st.header("LOCAL ALERT PANEL")
        st.markdown("*This section contains the meteorological warning of each country. Other countries will be added as the development phase continues.*")
        st.markdown("_CEI was established by ISCI-LAB_")
        
        
    
    st.markdown("_Select country to check latest alerts_")
    SELECT_COUNTRY = st.selectbox("COUNTRIES",("BELGIUM",
                                               "BOSNA HERZEGOVINA",
                                               "BRAZIL",
                                               "CHINA",
                                               "CROATIA",
                                               "ESTONIA",
                                               "ECUADOR",
                                               "FINLAND",
                                               "FRANCE",
                                               "GERMANY",
                                               "GREECE",
                                               "GUYANA",
                                               "HUNGARY",
                                               "HONG KONG",
                                               "ICELAND",
                                               "ISRAEL",
                                               "ITALY",
                                               "INDIA",
                                               "INDONESIA",
                                               "LATVIA",
                                               "LITHUANIA",
                                               "KENYA",
                                               "MADAGASCAR",
                                               "MALAVI",
                                               "MONGOLIA",
                                               "MONTENEGRO",
                                               "NETHERLANDS",
                                               "NORWAY",
                                               "PORTUGAL",
                                               "RUSSIA",
                                               "SERBIA",
                                               "SLOVAKIA",
                                               "SLOVENIA",
                                               "SPAIN",
                                               "SAUDI ARABIA",
                                               "SURINAME",
                                               "SOUTH AFRICA",
                                               "TANZANIA",
                                               "TRINIDAD AND TOBAGO",
                                               "UGANDA",
                                               "ZIMBABWE",
                                               "OMAN"))
    
    
    
    
    
    
    try:
        
        if SELECT_COUNTRY == "BELGIUM":
            
            BEL_DOC = EUROPE_REGION_ALERT("belgium")
            st.table(BEL_DOC)
            
        elif SELECT_COUNTRY == "BOSNA HERZEGOVINA":
            
            BOSNA_HER_DOC = EUROPE_REGION_ALERT("bosnia-herzegovina")
            st.table(BOSNA_HER_DOC)
            
        elif SELECT_COUNTRY == "BRAZIL":
            
            BRAZIL_DOC = BRAZIL_REGION_ALERT()
            st.table(BRAZIL_DOC)
            
        elif SELECT_COUNTRY == "CHINA":
            
            CHINA_DOC = CHINA_REGION_ALERT()
            st.table(CHINA_DOC)
            
        elif SELECT_COUNTRY == "CROATIA":
            
            CROATIA_DOC = EUROPE_REGION_ALERT("croatia")
            st.table(CROATIA_DOC)
            
        elif SELECT_COUNTRY == "ESTONIA":
            
            ESTONIA_DOC = EUROPE_REGION_ALERT("estonia")
            st.table(ESTONIA_DOC)
            
        elif SELECT_COUNTRY == "ECUADOR":
            
            ECUADOR_DOC = ECUADOR_REGION_ALERT()
            st.table(ECUADOR_DOC)
            
        elif SELECT_COUNTRY == "FINLAND":
            
            FINLAND_DOC = EUROPE_REGION_ALERT("finland")
            st.table(FINLAND_DOC)
            
        elif SELECT_COUNTRY == "FRANCE":
            
            FRANCE_DOC = EUROPE_REGION_ALERT("france")
            st.table(FRANCE_DOC)
            
        elif SELECT_COUNTRY == "GERMANY":
            
            GERMANY_DOC = EUROPE_REGION_ALERT("germany")
            st.table(GERMANY_DOC)
            
        elif SELECT_COUNTRY == "GREECE":
            
            GREECE_DOC = EUROPE_REGION_ALERT("greece")
            st.table(GREECE_DOC)
            
        elif SELECT_COUNTRY == "GUYANA":
            
            GUYANA_DOC = GUYANA_REGION_ALERT()
            st.table(GUYANA_DOC)
            
        elif SELECT_COUNTRY == "HUNGARY":
            
            HUNGARY_DOC = EUROPE_REGION_ALERT("hungary")
            st.table(HUNGARY_DOC)
            
        elif SELECT_COUNTRY == "HONG KONG":
            
            HK_DOC = HONG_KONG_REGION_ALERT()
            st.table(HK_DOC)
            
        elif SELECT_COUNTRY == "ICELAND":
            
            ICELAND_DOC = EUROPE_REGION_ALERT("iceland")
            st.table(ICELAND_DOC)
            
        elif SELECT_COUNTRY == "ISRAEL":
            
            ISRAEL_DOC = EUROPE_REGION_ALERT("israel")
            st.table(ISRAEL_DOC)
            
        elif SELECT_COUNTRY == "ITALY":
            
            ITALY_DOC = EUROPE_REGION_ALERT("italy")
            st.table(ITALY_DOC)
            
        elif SELECT_COUNTRY == "INDIA":
            
            INDIA_DOC = INDIA_REGION_ALERT()
            st.table(INDIA_DOC)
            
        elif SELECT_COUNTRY == "INDONESIA":
            
            INDONESIA_DOC = INDONESIA_REGION_ALERT()
            st.table(INDONESIA_DOC)
            
        elif SELECT_COUNTRY == "LATVIA":
            
            LATVIA_DOC = EUROPE_REGION_ALERT("latvia")
            st.table(LATVIA_DOC)
            
        elif SELECT_COUNTRY == "LITHUANIA":
            
            LITHUANIA_DOC = EUROPE_REGION_ALERT("lithuania")
            st.table(LITHUANIA_DOC)
            
        elif SELECT_COUNTRY == "KENYA":
            
            KENYA_DOC = KENYA_REGION_ALERT()
            st.table(KENYA_DOC)
            
        elif SELECT_COUNTRY == "MADAGASCAR":
            
            MADAGASCAR_DOC = MADAGASCAR_REGION_ALERT()
            st.table(MADAGASCAR_DOC)
            
        elif SELECT_COUNTRY == "MALAVI":
            
            MALAVI_DOC = MALAVI_REGION_ALERT()
            st.table(MALAVI_DOC)
            
        elif SELECT_COUNTRY == "MONGOLIA":
            
            MONGOLIA_DOC = MONGOLIA_REGION_ALERT()
            st.table(MONGOLIA_DOC)
            
        elif SELECT_COUNTRY == "MONTENEGRO":
            
            MONTENEGRO_DOC = EUROPE_REGION_ALERT("montenegro")
            st.table(MONTENEGRO_DOC)
            
        elif SELECT_COUNTRY == "NETHERLANDS":
            
            NETHERLANDS_DOC = EUROPE_REGION_ALERT("netherlands")
            st.table(NETHERLANDS_DOC)
            
        elif SELECT_COUNTRY == "NORWAY":
            
            NORWAY_DOC = EUROPE_REGION_ALERT("norway")
            st.table(NORWAY_DOC)
            
        elif SELECT_COUNTRY == "PORTUGAL":
            
            PORTUGAL_DOC = EUROPE_REGION_ALERT("portugal")
            st.table(PORTUGAL_DOC)
            
        elif SELECT_COUNTRY == "RUSSIA":
            
            RUSSIA_DOC = RUSSIA_REGION_ALERT()
            st.table(RUSSIA_DOC)
            
        elif SELECT_COUNTRY == "SERBIA":
            
            SERBIA_DOC = EUROPE_REGION_ALERT("serbia")
            st.table(SERBIA_DOC)
            
        elif SELECT_COUNTRY == "SLOVAKIA":
            
            SLOVAKIA_DOC = EUROPE_REGION_ALERT("slovakia")
            st.table(SLOVAKIA_DOC)
            
        elif SELECT_COUNTRY == "SLOVENIA":
            
            SLOVENIA_DOC = EUROPE_REGION_ALERT("slovenia")
            st.table(SLOVENIA_DOC)
            
        elif SELECT_COUNTRY == "SPAIN":
            
            SPAIN_DOC = EUROPE_REGION_ALERT("spain")
            st.table(SPAIN_DOC)
            
        elif SELECT_COUNTRY == "SAUDI ARABIA":
            
            SAU_ARA_DOC = SAUDI_ARABIA_ALERT()
            st.table(SAU_ARA_DOC)
            
        elif SELECT_COUNTRY == "SURINAME":
            
            SURINAME_DOC = SURINAME_AFRICA_ALERT()
            st.table(SURINAME_DOC)
            
        elif SELECT_COUNTRY == "SOUTH AFRICA":
            
            SOU_AFRICA_DOC = SOUTH_AFRICA_ALERT()
            st.table(SOU_AFRICA_DOC)
            
        elif SELECT_COUNTRY == "TANZANIA":
            
            TANZANIA_DOC = TANZANIA_REGION_ALERT()
            st.table(TANZANIA_DOC)
            
        elif SELECT_COUNTRY == "TRINIDAD AND TOBAGO":
            
            TRA_A_TO_DOC = TRINIDAD_AND_TOBAGO_ALERT()
            st.table(TRA_A_TO_DOC)
            
        elif SELECT_COUNTRY == "UGANDA":
            
            UGANDA_DOC = UGANDA_REGION_ALERT()
            st.table(UGANDA_DOC)
            
        elif SELECT_COUNTRY == "ZIMBABWE":
            
            ZIMBABWE_DOC = ZIMBABWE_REGION_ALERT()
            st.table(ZIMBABWE_DOC)
            
        elif SELECT_COUNTRY == "OMAN":
            
            OMAN_DOC = OMAN_REGION_TARGET()
            st.table(OMAN_DOC)
            
        else:
            pass
        
    except:
        st.info("THERE IS NO RESPONSE FROM THAT COUNTRY")
     
        
    st.subheader("LISTENING LATEST ALERT")
    st.markdown("_You will see the latest notifications from local sources in a stream. Search for the location you want to check in the data._")
    st.markdown("_Server listenings are based on major disasters._")
    st.markdown("_Use bottons to run_")
    
    col_rain,col_fog,col_thunder,col_gale = st.columns(4)
    
    with col_rain:
        
        try:
        
            RAIN_BUTTON = st.button("BASED RAIN CONDITIONS")
        
        
            if RAIN_BUTTON:
                
                st.warning("PLEASE WAIT, PROCESS IS RUNNING")
                
                
                RAIN_LIST = []
                
                
                TARGET_URL = "https://severeweather.wmo.int/rain/"
            
                TAR_REQ = requests.get(TARGET_URL).text
                BS_REQ = BeautifulSoup(TAR_REQ,"html.parser")
                    
                Area_ALL = BS_REQ.find_all("area")
                    
                for x_loop_area in Area_ALL:
                    
                    
                    HREF_ALL_AREA_PATH = x_loop_area.get("href")
                    REP_DOT_RAIN = HREF_ALL_AREA_PATH.replace("./","")
                    ALL_PATH_RAIN = TARGET_URL + REP_DOT_RAIN
                        
                    NEW_TAR_REQ = requests.get(ALL_PATH_RAIN).text
                    BS_NEW_TAR = BeautifulSoup(NEW_TAR_REQ,"html.parser")
                    AREA_NEW_ALL = BS_NEW_TAR.find_all("area")
                        
                    for new_all_loop in AREA_NEW_ALL:
                            
                        NEW_HREF_TARGET = new_all_loop.get("href")
                            
                        if NEW_HREF_TARGET.startswith("javascript"):
                                
                                
                            JAVA_TAR_URL_PATH = NEW_HREF_TARGET
                            SPLIT_TAR_JAVA = JAVA_TAR_URL_PATH.split("javascript:clickPopUp('./")
                            SPLIT_COMMA_JAVA = SPLIT_TAR_JAVA[1].split(",")
                            FIN_JAVA_TAR = SPLIT_COMMA_JAVA[0].replace("'","")
                            LAST_FIN_URL_ALL = TARGET_URL + REP_DOT_RAIN
                            PATH_WITH_CLEAR = LAST_FIN_URL_ALL.replace("index.html","")
                            TOGETGER_ALL_PATH = PATH_WITH_CLEAR + FIN_JAVA_TAR
                                
                            LAST_NEW_TAR_REQ = requests.get(TOGETGER_ALL_PATH).text
                            LAST_BS_NEW_TAR = BeautifulSoup(LAST_NEW_TAR_REQ,"html.parser")
                                
                            DIV_COOR = LAST_BS_NEW_TAR.find("td")
                                
                            if DIV_COOR != None:
                                CLEAR_OUTPUT_RAIN = DIV_COOR.text.replace("\n"," ").replace("As reported from","")
                                RAIN_LIST.append(CLEAR_OUTPUT_RAIN)
                
                                
                POR_BAR = st.progress(0)
        
                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
                    
                
                RAIN_DATA_LAST = pd.DataFrame(RAIN_LIST)
                RAIN_CSV = RAIN_DATA_LAST.to_csv()
                    
                st.table(RAIN_DATA_LAST)
                
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
            
                                          
    with col_thunder:
        
        try:
        
            TH_BUTTON = st.button("BASED THUNDER CONDITIONS")
        
        
            if TH_BUTTON:
                
                st.warning("PLEASE WAIT, PROCESS IS RUNNING")
                
                
                THU_LIST = []
                
                
                TARGET_URL = "https://severeweather.wmo.int/thunder/"
            
                TAR_REQ = requests.get(TARGET_URL).text
                BS_REQ = BeautifulSoup(TAR_REQ,"html.parser")
                    
                Area_ALL = BS_REQ.find_all("area")
                    
                for x_loop_area in Area_ALL:
                    
                    
                    HREF_ALL_AREA_PATH = x_loop_area.get("href")
                    REP_DOT_RAIN = HREF_ALL_AREA_PATH.replace("./","")
                    ALL_PATH_RAIN = TARGET_URL + REP_DOT_RAIN
                        
                    NEW_TAR_REQ = requests.get(ALL_PATH_RAIN).text
                    BS_NEW_TAR = BeautifulSoup(NEW_TAR_REQ,"html.parser")
                    AREA_NEW_ALL = BS_NEW_TAR.find_all("area")
                        
                    for new_all_loop in AREA_NEW_ALL:
                            
                        NEW_HREF_TARGET = new_all_loop.get("href")
                            
                        if NEW_HREF_TARGET.startswith("javascript"):
                                
                                
                            JAVA_TAR_URL_PATH = NEW_HREF_TARGET
                            SPLIT_TAR_JAVA = JAVA_TAR_URL_PATH.split("javascript:clickPopUp('./")
                            SPLIT_COMMA_JAVA = SPLIT_TAR_JAVA[1].split(",")
                            FIN_JAVA_TAR = SPLIT_COMMA_JAVA[0].replace("'","")
                            LAST_FIN_URL_ALL = TARGET_URL + REP_DOT_RAIN
                            PATH_WITH_CLEAR = LAST_FIN_URL_ALL.replace("index.html","")
                            TOGETGER_ALL_PATH = PATH_WITH_CLEAR + FIN_JAVA_TAR
                                
                            LAST_NEW_TAR_REQ = requests.get(TOGETGER_ALL_PATH).text
                            LAST_BS_NEW_TAR = BeautifulSoup(LAST_NEW_TAR_REQ,"html.parser")
                                
                            DIV_COOR = LAST_BS_NEW_TAR.find("td")
                                
                            if DIV_COOR != None:
                                CLEAR_OUTPUT_THUNDER = DIV_COOR.text.replace("\n"," ").replace("As reported from","")
                                THU_LIST.append(CLEAR_OUTPUT_THUNDER)
                
                                
                POR_BAR = st.progress(0)
        
                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
                    
                
                TH_DATA_LAST = pd.DataFrame(THU_LIST)
                TH_CSV = TH_DATA_LAST.to_csv()
                    
                st.table(TH_DATA_LAST)
                
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
            
            
            
    with col_fog:
        
        try:
        
            FOG_BUTTON = st.button("BASED FOG CONDITIONS")
        
        
            if FOG_BUTTON:
                
                st.warning("PLEASE WAIT, PROCESS IS RUNNING")
                
                
                FOG_LIST = []
                
                
                TARGET_URL = "https://severeweather.wmo.int/fog/"
            
                TAR_REQ = requests.get(TARGET_URL).text
                BS_REQ = BeautifulSoup(TAR_REQ,"html.parser")
                    
                Area_ALL = BS_REQ.find_all("area")
                    
                for x_loop_area in Area_ALL:
                    
                    
                    HREF_ALL_AREA_PATH = x_loop_area.get("href")
                    REP_DOT_RAIN = HREF_ALL_AREA_PATH.replace("./","")
                    ALL_PATH_RAIN = TARGET_URL + REP_DOT_RAIN
                        
                    NEW_TAR_REQ = requests.get(ALL_PATH_RAIN).text
                    BS_NEW_TAR = BeautifulSoup(NEW_TAR_REQ,"html.parser")
                    AREA_NEW_ALL = BS_NEW_TAR.find_all("area")
                        
                    for new_all_loop in AREA_NEW_ALL:
                            
                        NEW_HREF_TARGET = new_all_loop.get("href")
                            
                        if NEW_HREF_TARGET.startswith("javascript"):
                                
                                
                            JAVA_TAR_URL_PATH = NEW_HREF_TARGET
                            SPLIT_TAR_JAVA = JAVA_TAR_URL_PATH.split("javascript:clickPopUp('./")
                            SPLIT_COMMA_JAVA = SPLIT_TAR_JAVA[1].split(",")
                            FIN_JAVA_TAR = SPLIT_COMMA_JAVA[0].replace("'","")
                            LAST_FIN_URL_ALL = TARGET_URL + REP_DOT_RAIN
                            PATH_WITH_CLEAR = LAST_FIN_URL_ALL.replace("index.html","")
                            TOGETGER_ALL_PATH = PATH_WITH_CLEAR + FIN_JAVA_TAR
                                
                            LAST_NEW_TAR_REQ = requests.get(TOGETGER_ALL_PATH).text
                            LAST_BS_NEW_TAR = BeautifulSoup(LAST_NEW_TAR_REQ,"html.parser")
                                
                            DIV_COOR = LAST_BS_NEW_TAR.find("td")
                                
                            if DIV_COOR != None:
                                CLEAR_OUTPUT_FOG = DIV_COOR.text.replace("\n"," ").replace("As reported from","")
                                FOG_LIST.append(CLEAR_OUTPUT_FOG)
                
                                
                POR_BAR = st.progress(0)
        
                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
                    
                
                FOG_DATA_LAST = pd.DataFrame(FOG_LIST)
                FOG_CSV = FOG_DATA_LAST.to_csv()
                    
                st.table(FOG_DATA_LAST)
                
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN")
    
            
    with col_gale:
        
        try:
        
            GALE_BUTTON = st.button("BASED GALE CONDITIONS")
        
        
            if GALE_BUTTON:
                
                st.warning("PLEASE WAIT, PROCESS IS RUNNING")
                
                
                GALE_LIST = []
                
                
                TARGET_URL = "https://severeweather.wmo.int/gale/"
            
                TAR_REQ = requests.get(TARGET_URL).text
                BS_REQ = BeautifulSoup(TAR_REQ,"html.parser")
                    
                Area_ALL = BS_REQ.find_all("area")
                    
                for x_loop_area in Area_ALL:
                    
                    
                    HREF_ALL_AREA_PATH = x_loop_area.get("href")
                    REP_DOT_RAIN = HREF_ALL_AREA_PATH.replace("./","")
                    ALL_PATH_RAIN = TARGET_URL + REP_DOT_RAIN
                        
                    NEW_TAR_REQ = requests.get(ALL_PATH_RAIN).text
                    BS_NEW_TAR = BeautifulSoup(NEW_TAR_REQ,"html.parser")
                    AREA_NEW_ALL = BS_NEW_TAR.find_all("area")
                        
                    for new_all_loop in AREA_NEW_ALL:
                            
                        NEW_HREF_TARGET = new_all_loop.get("href")
                            
                        if NEW_HREF_TARGET.startswith("javascript"):
                                
                                
                            JAVA_TAR_URL_PATH = NEW_HREF_TARGET
                            SPLIT_TAR_JAVA = JAVA_TAR_URL_PATH.split("javascript:clickPopUp('./")
                            SPLIT_COMMA_JAVA = SPLIT_TAR_JAVA[1].split(",")
                            FIN_JAVA_TAR = SPLIT_COMMA_JAVA[0].replace("'","")
                            LAST_FIN_URL_ALL = TARGET_URL + REP_DOT_RAIN
                            PATH_WITH_CLEAR = LAST_FIN_URL_ALL.replace("index.html","")
                            TOGETGER_ALL_PATH = PATH_WITH_CLEAR + FIN_JAVA_TAR
                                
                            LAST_NEW_TAR_REQ = requests.get(TOGETGER_ALL_PATH).text
                            LAST_BS_NEW_TAR = BeautifulSoup(LAST_NEW_TAR_REQ,"html.parser")
                                
                            DIV_COOR = LAST_BS_NEW_TAR.find("td")
                                
                            if DIV_COOR != None:
                                GALE_OUTPUT_FOG = DIV_COOR.text.replace("\n"," ").replace("As reported from","")
                                GALE_LIST.append(GALE_OUTPUT_FOG)
                
                                
                POR_BAR = st.progress(0)
        
                for percent_index in range(100):
                    time.sleep(0.1)
                    POR_BAR.progress(percent_index + 1)
                    
                
                GL_DATA_LAST = pd.DataFrame(GALE_LIST)
                GL_CSV = GL_DATA_LAST.to_csv()
                    
                st.table(GL_DATA_LAST)
                
        except:
            
            st.info("DATA IS NOT ACTIVE FOR NOW, PLEASE WAIT AND TRY AGAIN.")
            
        
if SELECTBOX_SIDEBAR_GENERAL == "CLIMATIC PARAMETERS":
    
    
    st.header("CLIMATIC PARAMETERS PANEL")
    st.markdown("_CEI was established by ISCI-LAB_")
    
    try:
        
        st.markdown("_Select a parameter to check latest measure_")
        SELECT_SPEC_PARAMS = st.selectbox("PARAMETERS",("mid to upper-level moisture",
                                                   "average 850 hPa horizontal divergence",
                                                   "average mean sea level pressure",
                                                   "amount of sustained deep convection",
                                                   "average weekly Reynold's SST",
                                                   "average 850 hPa relative vorticity",
                                                   "average 850 hPa horizonal temperature advection",
                                                   "tropical cyclone formation probability",
                                                   "saturation equivalent potential temperature",
                                                   "average 850-200 hPa vertical shear",
                                                   "current tropical events",
                                                   "600-hPa relative humidity",
                                                   "current water vapor kg/m2",
                                                   "current wind speed m/s",
                                                   "current rain rate mm/hr",
                                                   "current surface temperature K",
                                                   "last vegetation health - based forecast",
                                                    "last surface reflectance - based forecast",
                                                    "last fractional vegetation",
                                                    "last precipitable water index",
                                                    "last normalized difference vegetation index",
                                                    "current land surface albedo",
                                                    "rainfall estimates, hydro based",
                                                    "current ice concentration",
                                                    "current soil moisture",
                                                    "current snow depth",
                                                    "glob surface type",
                                                    "crw - global sea surface temperatures trend",
                                                    "crw - global sea surface temperatures anomalies",
                                                    "crw - global sea surface temperatures",
                                                    "crw - heating weeks",
                                                    "crw - hotspot daily",
                                                    "crw - alert daily"))
        
        
        
        if SELECT_SPEC_PARAMS == "mid to upper-level moisture":
            
            
                
            BTWM_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rBTWM_024.gif",
                 stream=True).raw)
            
            st.image(BTWM_IMAGE,use_column_width=True)
                
        elif SELECT_SPEC_PARAMS == "average 850 hPa horizontal divergence":
            
            HDIV_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rHDIV_024.gif",
                 stream=True).raw)
            
            st.image(HDIV_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "average mean sea level pressure":
            
            MSLP_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rMSLP_024.gif",
                 stream=True).raw)
            
            st.image(MSLP_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "amount of sustained deep convection":
            
            PCCD_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rPCCD_024.gif",
                 stream=True).raw)
            
            st.image(PCCD_IMAGE,use_column_width=True)
                
               
                
        elif SELECT_SPEC_PARAMS == "average weekly Reynold's SST":
            
            RSST_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rRSST_024.gif",
                 stream=True).raw)
            
            st.image(RSST_IMAGE,use_column_width=True)
                
            
                
        elif SELECT_SPEC_PARAMS == "average 850 hPa relative vorticity":
            
            RVOR_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rRVOR_024.gif",
                 stream=True).raw)
            
            st.image(RVOR_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "average 850 hPa horizonal temperature advection":
            
            TADV_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rTADV_024.gif",
                 stream=True).raw)
            
            st.image(TADV_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "tropical cyclone formation probability":
                
            TCFP_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rTCFP_024.gif",
                 stream=True).raw)
            
            st.image(TCFP_IMAGE,use_column_width=True)
                
        elif SELECT_SPEC_PARAMS == "saturation equivalent potential temperature":
            
            THDV_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rTHDV_024.gif",
                 stream=True).raw)
            
            st.image(THDV_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "average 850-200 hPa vertical shear":
                
            VSHD_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rVSHD_024.gif",
                 stream=True).raw)
            
            st.image(VSHD_IMAGE,use_column_width=True)
            
            
        elif SELECT_SPEC_PARAMS == "current tropical events":
                
            CUMP_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_cCUMP_048.gif",
                 stream=True).raw)
            
            st.image(CUMP_IMAGE,use_column_width=True)
            
            
        elif SELECT_SPEC_PARAMS == "600-hPa relative humidity":
                
            MLRH_IMAGE = Image.open(requests.get("https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/gl_rMLRH_024.gif",
                 stream=True).raw)
            
            st.image(MLRH_IMAGE,use_column_width=True)
            
            
        elif SELECT_SPEC_PARAMS == "current water vapor kg/m2":
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/water_vapor.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/water_vapor.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "current wind speed m/s":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/wind_speed.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/wind_speed.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "current rain rate mm/hr":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/rain_rate.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/rain_rate.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "current surface temperature K":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/sfctmp.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/sfctmp.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "glob surface type":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/sfctyp.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/sfctyp.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "current snow depth":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/snow_depth.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/snow_depth.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
        elif SELECT_SPEC_PARAMS == "current soil moisture":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/soil_moisture.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/soil_moisture.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "current ice concentration":
            
            
            with st.expander("Western Hemisphere"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/ice_conc.west.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Eastern Hemisphere"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/spp/ssmi/ice_conc.east.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "rainfall estimates, hydro based":
            
            
            HIDRAINES_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/Products/atmosphere/ghe/figures/GHE_7DAY_EXAMPLE.GIF",
                     stream=True).raw)
                
            st.image(HIDRAINES_IMAGE,use_column_width=True)
            
            
        elif SELECT_SPEC_PARAMS == "current land surface albedo":
            
            
            SRALBEDO_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/viirs_land/LSA/LSA_npp_DayTime.png",
                     stream=True).raw)
                
            st.image(SRALBEDO_IMAGE,use_column_width=True)
            
        elif SELECT_SPEC_PARAMS == "last normalized difference vegetation index":
            
            
            VEGNORM_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/mgvi/MNDVIWD.png",
                     stream=True).raw)
                
            st.image(VEGNORM_IMAGE,use_column_width=True)
            
            
        elif SELECT_SPEC_PARAMS == "last precipitable water index":
            
    
            
            with st.expander("North America"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDNA.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("South America"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDSA.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Alaska"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDAK.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Asia"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDAS.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Europe"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDEU.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Africa"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDAF.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
            with st.expander("Oceania Area"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/BTDOC.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "last fractional vegetation":
            
            
            with st.expander("North America"):
    
                WGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVNA.gif",
                     stream=True).raw)
                
                st.image(WGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("South America"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVSA.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Alaska"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVAK.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Asia"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVAS.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Europe"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVEU.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
            with st.expander("Africa"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVAF.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
                
            with st.expander("Oceania Area"):
                
                EGENPLOT_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/data/land/vegetation/gvi/FRVOC.gif",
                     stream=True).raw)
                
                st.image(EGENPLOT_IMAGE,use_column_width=True)
                
        elif SELECT_SPEC_PARAMS == "last surface reflectance - based forecast":
            
            
            
            SURREFFOR_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/Products/land/sr/figures/VIIRS_SR_example.png",
                     stream=True).raw)
                
            st.image(SURREFFOR_IMAGE,use_column_width=True)
            
        elif SELECT_SPEC_PARAMS == "last vegetation health - based forecast":
            
            VEGHEFOR_IMAGE = Image.open(requests.get("https://www.ospo.noaa.gov/Products/land/vvhp/figures/VVHP_VHI_example.png",
                     stream=True).raw)
                
            st.image(VEGHEFOR_IMAGE,use_column_width=True)
            
    
            
        elif SELECT_SPEC_PARAMS == "crw - alert daily":
            
            
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_baa-max-7d_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_baa-max-7d_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_baa-max-7d_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "crw - hotspot daily":
            
            
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_hs_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_hs_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_hs_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                
                
        elif SELECT_SPEC_PARAMS == "crw - heating weeks":
            
            
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_dhw_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_dhw_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_dhw_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "crw - global sea surface temperatures":
            
            
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/coraltemp_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/coraltemp_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/coraltemp_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "crw - global sea surface temperatures anomalies":
            
                    
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_ssta_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_ssta_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_ssta_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                
        elif SELECT_SPEC_PARAMS == "crw - global sea surface temperatures trend":
            
            
            with st.expander("East"):
                
                CORALREES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_sst-trend-7d_v3.1_east_current.png",
                     stream=True).raw)
                
                st.image(CORALREES_IMAGE,use_column_width=True)
                
                
            with st.expander("West"):
                
                CORALWES_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_sst-trend-7d_v3.1_west_current.png",
                     stream=True).raw)
                
                st.image(CORALWES_IMAGE,use_column_width=True)
                
                
            with st.expander("Global"):
                
                GLOBCOR_IMAGE = Image.open(requests.get("https://coralreefwatch.noaa.gov/data_current/5km/v3.1_op/daily/png/ct5km_sst-trend-7d_v3.1_global_current.png",
                     stream=True).raw)
                
                st.image(GLOBCOR_IMAGE,use_column_width=True)
                
                   
        else:
            
            pass
        
    except:
        
        st.info("DATABASE IS NOT READY FOR NOW, PLEASE TRY AGAIN")
        
    
    
   
if SELECTBOX_SIDEBAR_GENERAL == "REPORT A DISASTER":
    
    
    st.header("REPORT A DISASTER")
    st.markdown("**Please report natural disasters that you are sure of. If you are in a dangerous situation, please inform us about your situation in detail.**")
    st.markdown("_CEI was established by ISCI-LAB_")
    

    try:
        
        CONTACT_US_FORM = """
        <style>
        .btn {
          border: none;
          color: white;
          padding: 9px 22px;
          font-size: 15px;
          cursor: pointer;
        }

        .danger {background-color: #820b00;} 
        .danger:hover {background: #da190b;}
        </style>
        <form action="https://formsubmit.co/initiative.isc@gmail.com" method="POST">
          <table>
          <fieldset>
          <label for="in_name">YOUR NAME*</label><br>
          <input type="text" id="in_name" name="name" placeholder="Name" required><br>
          </fieldset>
          <fieldset>
          <label for="in_loc">YOUR DISASTER LOCATION*</label><br>
          <input type="text" id="in_loc" name="location" placeholder="Location" required><br>
          </fieldset>
          <fieldset>
          <label for="in_type">YOUR DISASTER TYPE*</label><br>
          <input type="text" id="in_type" name="type" placeholder="Type" required><br>
          </fieldset>
          <fieldset>
          <label for="in_mail">YOUR EMAIL*</label><br>
          <input type="email" id="in_mail" name="email" placeholder="Email" required><br>
          </fieldset>
          <fieldset>
          <label>YOUR SITUATION</label><br>
          <textarea rows="15" cols="60" name="situation">
          </textarea>
          </fieldset>
          <input type="hidden" name="_template" value="box">
          <input type="hidden" name="_captcha" value="true">
          <input type="hidden" name="_autoresponse" value="Your message has been forwarded to us,make sure you are safe and heed the warnings from authorities.">
          <button class="btn danger" type="submit">Send</button>
          </table>
        </form>
        """
        
        st.markdown(CONTACT_US_FORM,unsafe_allow_html=True)
        
    except:
        
        st.warning("THERE IS A CONNECTION PROBLEM, PLEASE TRY AGAIN")
    
