# -*- coding: utf-8 -*-
import json
import re

import requests

def getOversea():
    resp = requests.get(url='https://www.bing.com/covid/data')
    resp=resp.json()
    with open('static/byState.json', 'w', encoding="UTF-8") as result_file:
        json.dump(resp, result_file)

def getChina():
    resp = requests.get(url='https://3g.dxy.cn/newh5/view/pneumonia')
    resp.encoding='utf-8'
    resp = resp.text
    p1 = re.compile(r'window.getAreaStat = (.*?)}catch', re.S)
    json_str=re.findall(p1, resp)
    for i in json_str:
        print(i)
    resp_json=json.loads(json_str[0])
    with open('static/chinaByProvice.json', 'w', encoding="") as result_file:
        json.dump(resp_json, result_file)


#处理国内省份数据保存为可读数据
def parserProvinces():
    with open('static/chinaByprovice.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        new_province_list=[]

        for item in data:
            province=item['provinceName']
            confirmedCount=item['confirmedCount']
            with open('static/newProvinces.json', encoding="UTF-8") as json_file_one:
                privinces = json.load(json_file_one)
                for priv_item in privinces:
                    if priv_item['name'] == item['provinceName']:
                        name =item['provinceName']
                        lat = priv_item['lat']
                        lng = priv_item['lng']
                        comfirmed = item['confirmedCount']
                        current = item['currentConfirmedCount']
                        new_province_list.append({'name':name,'lat':lat,'lng':lng,'confirmed':comfirmed,'current':current})
    print(new_province_list)
    with open('mid/newProvinces.json', 'w', encoding="UTF-8") as result_file:
        json.dump(new_province_list, result_file)

# with open('results.json', 'w', encoding="UTF-8") as result_file:
#     json.dump(data_state, result_file)

# 处理国外省份数据保存为可读数据
def parseGlobalByState():
    with open('static/byState.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        new_state_list = []

        for item in data['areas']:
            print(item)
            for item_state in item['areas']:
                print(item_state)
                name = item_state['id']
                lat = item_state['lat']
                lng = item_state['long']
                comfirmed = item_state['totalConfirmed']
                recovered= item_state['totalRecovered']
                death = item_state['totalDeaths']
                current=0
                try:
                    current = comfirmed-recovered-death
                except:
                    kes=0
                new_state_list.append({'name': name, 'lat': lat, 'lng': lng, 'confirmed': comfirmed, 'current': current})
    print(new_state_list)
    with open('mid/byState.json', 'w', encoding="UTF-8") as result_file:
        json.dump(new_state_list, result_file)


def extendTwoList():
    with open('mid/byState.json', 'r', encoding="UTF-8") as result_file_one:
        states = json.load(result_file_one)
        with open('mid/newProvinces.json', 'r', encoding="UTF-8") as result_file_two:
            provinces = json.load(result_file_two)
            new_list=states+provinces
            print(new_list)
            with open('mid/twoList.json', 'w', encoding="UTF-8") as result_file:
                json.dump(new_list, result_file)
def getFInalByState(type):
    with open('mid/twoList.json', 'r', encoding="UTF-8") as result_file_one:
        twoList = json.load(result_file_one)
        data_state=[]
        max_num=getMaxNumFromDIct(twoList,'confirmed')
        print(max_num)
        for item in twoList:
            data_state.append(item['lat'])
            data_state.append(item['lng'])
            item_num = item[type] / max_num
            data_state.append(item_num)
            data_state.append(0)
    with open('final/'+type+'ByState.json', 'w', encoding="UTF-8") as result_file:
        json.dump(data_state, result_file)

def getMaxNumFromDIct(dict,keyName):
    new_list=[]
    for item in dict:
        new_list.append(item[keyName])
    return max(new_list)


getFInalByState('confirmed')