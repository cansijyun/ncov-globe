# ncov-3d-globe-api
[English Doc](https://github.com/cansijyun/ncov-globe/blob/master/README.md)

### 3d 地球

累计确诊总数按省份 http://pyact.com/ncov-globe/by-state.html

累计确诊总数按国家http://pyact.com/ncov-globe/by-nation.html

### 疫情数据api

海外省级单位数据api http://pyact.com:5000/state-info-api

国内省级单位数据api http://pyact.com:5000/province-info-api

![byState](https://raw.githubusercontent.com/cansijyun/ncov-globe/master/readme/bystate.gif)

项目结构

```
├─back              //Flask后端
│  └─flask
│      ├─final      //最终数据
│      ├─mid        //中间数据
│      ├─static     //源数据
│      ├─myvenv     //ubuntu下的虚拟环境
│      ├─win-venv   //windows下的虚拟环境
│      ├─main.py    //Flask 路由和入口代码
│      └─scraper.py //定时执行的爬虫代码
├─conf              //ubuntu配置文件
│  ├─init    
│  ├─ncov.service   //ubuntu service配置(一般放在/etc/systemd/system)
│  └─nginx_conf     //ubuntu nginx配置(一般放在/etc/nginx/sites-available)
└─front             //前端文件
```



## 在windows运行代码

打开命令行

1. `cd <项目的根目录>`  
2. `cd back/flask`   
3. `source win-venv/Scripts/activate` # 激活虚拟环境activate the virtual encironment
3. `python3 run main.py`   # 后端服务器开启

nginx

5. `cd <nginx安装目录>/conf` # 打开nginx安装目录的cof文件夹
6. 编辑nginx.conf

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
7. `cd <nginx安装目录>` 

8. `start nginx`  or `nginx -s reload`



本项目是flask为后端，wengl globe为前端。

后端服务器的爬虫每2小时从丁香园和bing爬取疫情数据并清洗整合。

（后续补部署到ubuntu教程）

微信:42692305
