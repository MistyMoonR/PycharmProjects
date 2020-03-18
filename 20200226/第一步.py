import requests


if __name__ == '__main__':

    target = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&qdii=&tabSubtype=,,,,,&pi=1&pn=1000'
    req = requests.get(url=target)
    # print(req.text)
    print(req.text[22:-160])