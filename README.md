二维码扫描分析工具
==========

原理是生成二维码的时候前面加入一个重定向的动作. 这里生成的二维码首先会访问分析的链接地址, 将访问者的时间,地址和客户端类型记录下来,然后转向目标地址.

基于tornado框架,异步进行重定向.数据最后存入MongoDB中.

idea来自曹大公众号(caoz的梦呓,caozsay).

## 使用

1. 安装MongoDB
2. pip install -r requirements.txt
3. 修改settings.py中的ip地址
3. 运行python app.py