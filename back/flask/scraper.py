# -*- coding: utf-8 -*-
import json
import re

import requests

def get_oversea():
    resp = requests.get(url='https://www.bing.com/covid/data')
    resp=resp.json()
    with open('static/overseas.json', 'w', encoding="UTF-8") as result_file:
        json.dump(resp, result_file)


def get_china():
    resp = requests.get(url='https://3g.dxy.cn/newh5/view/pneumonia')
    resp.encoding='utf-8'
    resp = resp.text
    p1 = re.compile(r'window.getAreaStat = (.*?)}catch', re.S)
    json_str=re.findall(p1, resp)
    for i in json_str:
        print(i)
    resp_json=json.loads(json_str[0])
    print(resp_json)
    with open('static/chinaByProvice.json', 'w', encoding="UTF-8") as result_file:
        json.dump(resp_json, result_file,ensure_ascii=False)


#处理国内省份数据保存为可读数据
def parser_provinces():
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
        json.dump(new_province_list, result_file,ensure_ascii=False)

# with open('results.json', 'w', encoding="UTF-8") as result_file:
#     json.dump(data_state, result_file)

# 处理国外省份数据保存为可读数据
def parse_global_by_state():
    with open('static/overseas.json', encoding="UTF-8") as json_file:
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

#合并两个表格
def extend_two_list():
    with open('mid/byState.json', 'r', encoding="UTF-8") as result_file_one:
        states = json.load(result_file_one)
        with open('mid/newProvinces.json', 'r', encoding="UTF-8") as result_file_two:
            provinces = json.load(result_file_two)
            new_list=states+provinces
            print(new_list)
            with open('mid/twoList.json', 'w', encoding="UTF-8") as result_file:
                json.dump(new_list, result_file,ensure_ascii=False)
#获取最终分省份图
def get_final_by_state(type):
    with open('mid/twoList.json', 'r', encoding="UTF-8") as result_file_one:
        twoList = json.load(result_file_one)
        data_state=[]
        max_num=get_max_num_from_dict(twoList,'confirmed')
        print(max_num)
        for item in twoList:
            data_state.append(item['lat'])
            data_state.append(item['lng'])
            item_num = item[type] / max_num
            data_state.append(item_num)
            data_state.append(0)
    with open('final/'+type+'ByState.json', 'w', encoding="UTF-8") as result_file:
        json.dump(data_state, result_file,ensure_ascii=False)

def get_final_by_nation(type):

    with open('static/overseas.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        data_nation = []
        num = []
        for item in data['areas']:
            num.append(item['totalConfirmed'])
        max_num = max(num)
        # print("Type:", max_num)

        for item in data['areas']:
            data_nation.append(item['lat'])
            data_nation.append(item['long'])
            item_num = (item['totalConfirmed'] / max_num) * 1.3
            item_num = float("%.4f" % item_num)
            data_nation.append(item_num)
            data_nation.append(0)

    with open('final/'+type+'ByNation.json', 'w', encoding="UTF-8") as result_file:
        json.dump(data_nation, result_file)


def get_max_num_from_dict(dict,keyName):
    new_list=[]
    for item in dict:
        new_list.append(item[keyName])
    return max(new_list)



def main_scraper():
    get_oversea()
    parse_global_by_state()
    get_china()
    parser_provinces()
    get_final_by_state('confirmed')
    get_final_by_nation('confirmed')

if __name__ == '__main__':
    main_scraper()