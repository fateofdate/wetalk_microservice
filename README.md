## 基于UDP的聊天程序

#### 技术选择：

语言：python-3.8

数据库：sqlite3

第三方库：socket，threading, time, hashlib。

####     安装脚本:
					pyhton3 db_installer.py
					
####     服务端：

​					login_service.py
					register_service.py
					db_service.py
					wetalk_service.py
####     客户端：

					

####     数据库：

					user.db
					verify.db

####     使用教程:
1.安装依赖  
2.运行数据库脚本  
3.开启服务相关端口(根据自己情况而定建议9090 9091 9092 9093)  
4.运行db_service.py(port 9090)  
5.运行register_service.py(port 9091)  
6.运行login_service.py(port 9092)  
7.运行wetalk_service.py(port 9093)  
#### 	 运行命令：
					check port
					lsof -i:9090
					lsof -i:9091
					lsof -i:9092
					lsof -i:9093
					if occupy kill the pid or change the port
					python3 db_service.py &
					python3 register_service.py &
					python3 login_service.py &
					python3 wetalk_service.py.py &
