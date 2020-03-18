# -*- coding:UTF-8 -*-
# import urllib.request
# data = urllib.urlopen("http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2019-02-24&ed=2020-02-24&qdii=&tabSubtype=,,,,,&pi=1&pn=1000&dx=1&v=0.4504721555323028").read()
# print(data)

import requests

if __name__ == '__main__':
    target = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2019-02-25&ed=2020-02-25&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.9329848707879547'
    req = requests.get(url=target)
    print(req.text)
    print(req.text[23:-161])
    char = req.text[23:-161]
    str_list = [char]
