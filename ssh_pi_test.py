# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 23:36:17 2021

@author: Dongzhou_X99
"""
import paramiko
# 输入用户名、密码、ip等
ip = "192.168.1.105"  
port =  22
user = "pi"
password = "pi"
#创建一个ssh对象
ssh = paramiko.SSHClient()
#自动选择yes
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh.connect(ip,port,user,password,timeout = 10)
#输入linux命令
ssh.exec_command('cd Desktop/TochoRPitest; python testmotor.py')
while True:
	#等待输入命令
    temp = str(input("input:"))
    print(temp)
    stdin,stdout,stderr = ssh.exec_command(temp)
    # 输出命令执行结果
    result = stdout.read()
    print(result)
#关闭连接
ssh.close()