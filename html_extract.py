# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup as BS
import re
import pickle

def main():
    #年
    y = ["94","95","96","97","98","99","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14"]
    #競馬場
    p = ["01","02","03","04","05","06","07","08","09","10"]
    #開催回
    n = ["01","02","03","04","05","06","07","08"]
    #開催日
    d = ["01","02","03","04","05","06","07","08"]
    #レース
    r = ["01","02","03","04","05","06","07","08","09","10","11","12"]

    urls = "http://keiba.yahoo.co.jp/race/result/"
    urlarray = []
    [urlarray.append(urls + year + place + num + day + race) for year in y for place in p for num in n for day in d for race in r]

    #もしそのURLが存在しなければpassするコード
    keibajou_re = re.compile("result/..(..).+")
    #ファイル命名用
    race = re.compile("(\d+)")

    for url in urlarray:
        keibajou = keibajou_re.findall(url)
        try:
            htmlfp = urllib2.urlopen(url)
            html = htmlfp.read()#.decode("utf-8", "replace")
            htmlfp.close()
            #競馬場ごとに分ける
            if keibajou == ['01']:
                sapporo = race.search(url)
                f = open(r"sapporo\sapporo_"+sapporo.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['02']:
                hakodate = race.search(url)
                f = open(r"hakodate\hakodate_"+hakodate.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['03']:
                fukushima = race.search(url)
                f = open(r"fukushima\fukushima_"+fukushima.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['04']:
                niigata = race.search(url)
                f = open(r"niigata\niigata_"+niigata.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['05']:
                tokyo = race.search(url)
                f = open(r"tokyo\tokyo_"+tokyo.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['06']:
                nakayama = race.search(url)
                f = open(r"nakayama\nakayama_"+nakayama.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['07']:
                chukyo = race.search(url)
                f = open(r"hukyo\chukyo_"+chukyo.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['08']:
                kyoto = race.search(url)
                f = open(r"kyoto\kyoto_"+kyoto.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['09']:
                hanshin = race.search(url)
                f = open(r"hanshin\hanshin_"+hanshin.group()+".txt","a")
                f.write(html)
                f.close()
            if keibajou == ['10']:
                kokura = race.search(url)
                f = open(r"kokura\kokura_"+kokura.group()+".txt","a")
                f.write(html)
                f.close()
        except:
            pass

main()
