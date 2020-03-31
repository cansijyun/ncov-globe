# ncov-3d-globe-api

[Tutorial]()

[中文文档](https://github.com/cansijyun/ncov-globe/blob/master/readme/README_ZH.md)



## Current Support:

### 3d-globe 

- Total Confirmed Cases by State http://pyact.com/ncov-globe/by-state.html

- Total Confirmed Cases by Country http://pyact.com/ncov-globe/by-nation.html


### COVID data api

- Cases by States API(except China) http://pyact.com:5000/state-info-api

- Chinese Cases by States API http://pyact.com:5000/province-info-api


![byState](https://raw.githubusercontent.com/cansijyun/ncov-globe/master/readme/bystate.gif)

## Directory Structure:

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
│  ├─ncov.service   //ubuntu service configuration( /etc/systemd/system)
│  └─nginx_conf     //ubuntu nginx configuration( /etc/nginx/sites-available)
└─front             //Front-end webgl globe
```

Back-end : 

- Flask
- Python Scraper works every 2 hours. World data is from bing and Chinese data is from Dingxiangyuan.


Front-end :

- webgl globe
- javascript



## Running the website locally  (windows)

**Open a bash terminal/command window** and execute the following commands:

1. `cd <path-to-this-repo>`   # change to **root of this repo**
2. `cd back/flask`   
3.  `source win-venv/Scripts/activate` # activate the virtual encironment
4. `python3 run main.py`   # start back-end server

Start  nginx (you shoud download the nginx before)

5. `cd <path-to-nginx>/conf` # change to nginx conf directory
6. edit this nginx.conf

```
	server {
		listen       8888; #port  
		server_name  localhost ; 
        location / {
			root   <path-to-this-repo>/front/webgl-globe-master;
            index  globe/index.html;
        }
    }
```
7. `cd <path-to-nginx>` 

8. `start nginx`  or `nginx -s reload`

 


## Contributing to the repo:

wechat:42692305
