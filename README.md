#  万户协同办公平台未授权访问漏洞 POC
万户ezOFFICE协同管理平台涵盖门户自定义平台、信息知识平台管理、系统管理平台功能，它以工作流引擎为底层服务，以通讯沟通平台为交流手段，以门户自定义平台为信息推送显示平台，为用户提供集成的协同工作环境。该平台存在未授权访问漏洞，攻击者可以从evoInterfaceServlet接口获得系统登录账号和用MD5加密的密码。
```
Usage:
  python3  SMART-PARK.py -h
```
![示例](https://github.com/gallopsec/WH-ezOFFICE/blob/main/poc.png)
![示例](https://github.com/gallopsec/WH-ezOFFICE/blob/main/test.png)
