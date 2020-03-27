# ncov-3d-globe-api
[中文文档]()

### 3d-globe 

Total Confirmed Cases by States http://pyact.com/ncov-globe/by-state.html

Total Confirmed Cases by Countries http://pyact.com/ncov-globe/by-nation.html

### COVID data api

Cases by States API(except China) http://pyact.com:5000/state-info-api

Chinese Cases by States APIhttp://pyact.com:5000/province-info-api

![byState](https://raw.githubusercontent.com/cansijyun/covid-ncov-3d-globe-api/master/readme_img/byState.gif)

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

wechat:42692305
