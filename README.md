# ncov-3d-globe-api
[中文文档](https://github.com/cansijyun/ncov-globe/blob/master/readme/README-ZH.md)

### 3d-globe 

Total Confirmed Cases by States http://pyact.com/ncov-globe/by-state.html

Total Confirmed Cases by Country http://pyact.com/ncov-globe/by-nation.html

### COVID data api

Cases by States API(except China) http://pyact.com:5000/state-info-api

Chinese Cases by States API http://pyact.com:5000/province-info-api

![byState](https://raw.githubusercontent.com/cansijyun/ncov-globe/master/readme/bystate.gif)

Directory Structure

```
├─back              //Flask
│  └─flask
│      ├─final      //globe data 
│      ├─mid        //mid-data
│      ├─static     //source data
│      ├─myvenv     //ubuntu virtual environment
│      ├─win-venv   //windows virtual environment
│      ├─main.py    //Flask main app
│      └─scraper.py //Scraper app
├─conf              //ubuntu configuration file
│  ├─init    
│  ├─ncov.service   //ubuntu service conf( /etc/systemd/system)
│  └─nginx_conf     //ubuntu nginx配置( /etc/nginx/sites-available)
└─front             //Front-end webgl globe
```

Back-end is Flask.

Python Scraper works every 2 hours. World data is from bing and Chinese data is from Dingxiangyuan.

Front-end is webgl globe.

wechat:42692305
