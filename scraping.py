# -*- coding: utf-8 -*-

"""レース数
chukyo:5748
fukushima:5158
hakodate:3590
hanshin:9278
kokura:5472
kyoto:9829
nakayama:9749
niigata:5878
sapporo:3691
tokyo:9498
"""

from BeautifulSoup import BeautifulSoup as BS
import re
import pickle
import glob
import numpy

#馬場状態を抽出
def baba(keibajou, soup):
    #馬場状態
    baba = re.compile("spBg ([a-z]*)")

    for link in soup.findAll("p", id="raceTitMeta"):
        #特徴抽出
        aa = link.contents
        aa = baba.findall(str(aa))
        #競馬場ごとに分ける
        if keibajou == ['sapporo']:
            return aa
        if keibajou == ['hakodate']:
            return aa
        if keibajou == ['fukushima']:
            return aa
        if keibajou == ['niigata']:
            return aa
        if keibajou == ['tokyo']:
            return aa
        if keibajou == ['nakayama']:
            return aa
        if keibajou == ['chukyo']:
            return aa
        if keibajou == ['kyoto']:
            return aa
        if keibajou == ['hanshin']:
            return aa
        if keibajou == ['kokura']:
            return aa

#何番人気で決着したかを抽出
def ninki(keibajou, htmltxt):
    #全馬の着順人気
    ninkiba = re.compile("<td class=\"txC fntS\">(\d+)</td>")
    #特徴抽出
    aa = ninkiba.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return aa
    if keibajou == ['hakodate']:
        return aa
    if keibajou == ['fukushima']:
        return aa
    if keibajou == ['niigata']:
        return aa
    if keibajou == ['tokyo']:
        return aa
    if keibajou == ['nakayama']:
        return aa
    if keibajou == ['chukyo']:
        return aa
    if keibajou == ['kyoto']:
        return aa
    if keibajou == ['hanshin']:
        return aa
    if keibajou == ['kokura']:
        return aa

#コース、距離抽出
def distance(keibajou, htmltxt):
    #コース、距離抽出のための正規表現
    distpat = re.compile("fntSS gryB\">(\w*).+\s(.+)m \[")
    #芝→shiba、ダート→dirt、障害→shougaiに置換
    htmltxt = htmltxt.replace('芝', 'shiba')
    htmltxt = htmltxt.replace('ダート', 'dirt')
    htmltxt = htmltxt.replace('障害', 'shougai')
    #特徴抽出
    aa = distpat.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return aa
    if keibajou == ['hakodate']:
        return aa
    if keibajou == ['fukushima']:
        return aa
    if keibajou == ['niigata']:
        return aa
    if keibajou == ['tokyo']:
        return aa
    if keibajou == ['nakayama']:
        return aa
    if keibajou == ['chukyo']:
        return aa
    if keibajou == ['kyoto']:
        return aa
    if keibajou == ['hanshin']:
        return aa
    if keibajou == ['kokura']:
        return aa

#抽出
def ext(keibajou, soup, htmltxt):
    #馬場状態
    babastate = baba(keibajou, soup)
    #人気
    ninkii = ninki(keibajou, htmltxt)
    #距離
    kyori = distance(keibajou, htmltxt)
    return babastate,ninkii,kyori

    """
    #ファイルを1つずつ見る
    for file in fileglob:
        feature = []
        f0 = open(file, "r")
        htmltxt = f0.read()
        #ファイル命名用
        keibajou = file_re.findall(file)
        #HTMLテキスト抽出
        soup = BS(htmltxt)
    """

#最初に実行
def main():
    #ファイル名抽出
    fileglob = glob.glob(r"C:\comike_python\*\*.txt")
    #ファイル命名用（競馬場名）
    file_re = re.compile("comike_python\\\\.+\\\\(.+)_")

    #特徴を入れるリスト
    sapporoar = []
    hakodatear = []
    fukushimaar = []
    niigataar = []
    tokyoar = []
    nakayamaar = []
    chukyoar = []
    kyotoar = []
    hanshinar = []
    kokuraar = []

    #ファイルを1つずつ見る
    for file in fileglob:
        #featureリストを初期化
        feature = []
        #ファイル読み込み
        f0 = open(file, "r")
        htmltxt = f0.read().decode("utf-8")
        f0.close()
        #HTMLテキスト抽出
        soup = BS(htmltxt)
        #ファイル命名用(競馬場名)
        keibajou = file_re.findall(file)
        #main()から返ってきた特徴をリストに追加
        #[[特徴1,特徴2,...,特徴n],[特徴1,...,特徴n]という感じになる
        if keibajou == ['sapporo']:
            sapporoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['hakodate']:
            hakodatear.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['fukushima']:
            fukushimaar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['niigata']:
            niigataar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['tokyo']:
            tokyoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['nakayama']:
            nakayamaar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['chukyo']:
            chukyoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['kyoto']:
            kyotoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['hanshin']:
            hanshinar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['kokura']:
            kokuraar.append(ext(keibajou, soup, htmltxt))

    #保存
    #ファイル名を競馬場名_result.txtとして保存
    #札幌
    f = open(r"C:\comike_python\sapporo_result.txt","w")
    pickle.dump(sapporoar, f)
    f.close()
    #函館
    f = open(r"C:\comike_python\hakodate_result.txt","w")
    pickle.dump(hakodatear, f)
    f.close()
    #福島
    f = open(r"C:\comike_python\fukushima_result.txt","w")
    pickle.dump(fukushimaar, f)
    f.close()
    #新潟
    f = open(r"C:\comike_python\niigata_result.txt","w")
    pickle.dump(niigataar, f)
    f.close()
    #東京
    f = open(r"C:\comike_python\tokyo_result.txt","w")
    pickle.dump(tokyoar, f)
    f.close()
    #中山
    f = open(r"C:\comike_python\nakayama_result.txt","w")
    pickle.dump(nakayamaar, f)
    f.close()
    #中京
    f = open(r"C:\comike_python\chukyo_result.txt","w")
    pickle.dump(chukyoar, f)
    f.close()
    #京都
    f = open(r"C:\comike_python\kyoto_result.txt","w")
    pickle.dump(kyotoar, f)
    f.close()
    #阪神
    f = open(r"C:\comike_python\hanshin_result.txt","w")
    pickle.dump(hanshinar, f)
    f.close()
    #小倉
    f = open(r"C:\comike_python\kokura_result.txt","w")
    pickle.dump(kokuraar, f)
    f.close()




#数値の特徴ベクトル生成
def vector():
    #すべてのファイル名抽出
    f = glob.glob(r"C:\comike_python\*_result.txt")
    filemei_re = re.compile("C:\\\\comike_python\\\\([a-z]*)_")
    #すべてのファイルの内容（ベクトル）抽出
    #ファイルを１つずつ見る
    for file in f:
        f0 = open(file, "r")
        fi = pickle.load(f0)
        f0.close()
        #ファイル命名用
        filemei = filemei_re.match(file)

        #結果のベクトル（答えとなる）
        kekkavector = []
        #条件のベクトル
        termvector = []
        dic = {}
        count = 0
        t = []
        k = []
        termk = []
        #１Rごとの条件・結果を取り出し
        for ff in fi:
            termkekka = []
            #結果を取得[u'8',u'1',...,u'3']
            kekka = ff[1]
            #条件を取得['天気','馬場状態',(u'コース',u'距離')]
            term = ff[0] + ff[2]
            #数値に変換
            kekka = [int(s) for s in kekka]
            kekkavector.append(kekka)
            #タプルを辞書型に入れて番号で指定できるようにする
            #その競馬場でのコース・距離情報を全て数値に変換できる
            for s in term:
                if type(s) != tuple:
                    #同じ天気、馬場の辞書があれば飛ばす
                    if dic.has_key(s) == True:
                        pass
                    else:
                        count += 1
                        dic[s] = count

                else:
                    #同じコース、距離の辞書があれば飛ばす
                    if dic.has_key(s) == True:
                        pass
                    else:
                        count += 1
                        dic[s] = count
                #辞書の要素（数値）を入れる
                termkekka.append(dic[s])
            #結果を入れる
            termkekka.append(kekka)
            termk.append(termkekka)
        t.append(dic)
        k.append(kekkavector)
        #競馬場ごとの結果をファイル出力
        fwrite = open("C:\\comike_python\\" + filemei.group(1) + "_feature.txt", "w")
        pickle.dump(t, fwrite)
        fwrite.close()
        fwrite2 = open("C:\\comike_python\\" + filemei.group(1) + "_label.txt", "w")
        pickle.dump(k, fwrite2)
        fwrite2.close()
        fwrite3 = open("C:\\comike_python\\" + filemei.group(1) + "_finalfeature.txt", "w")
        pickle.dump(termk, fwrite3)
        fwrite3.close()

def analysis():
    #すべての特徴のファイル名抽出
    f = glob.glob(r"C:\comike_python\*_finalfeature.txt")
    #ファイルを１つずつ見る
    for file in f:
        f0 = open(file, "r")
        fi = pickle.load(f0)
        f0.close()
        #SVMなどの方法と同じようにやってみる
        #コースや馬場状態などによってどれだけ正解しているかを見る?
        """正解をつけるとその結果に限定されてしまうので教師なしが適当"""
        #[[(1,5,4)]]や[[[1,5,4]]]のように行列の要素に(1,5,4)や[1,5,4]などを指定できないか
        #sum初期化
        sum = 0
        sum2 = 0
        sum3 = 0
        #var初期化
        var = 0
        var2 = 0
        var3 = 0
        #var計算用
        lis = []
        lis2 = []
        lis3 = []
        for list in fi:
            #条件要素だけのリスト作成
            """天気のみ、馬場状態のみなど個々の条件と結果を突き合わせてみる"""
            #天気、馬場状態のみ
            list01 = [list[0],list[1]]
            #天気、コースのみ
            list02 = [list[0],list[2]]
            #馬場状態、コースのみ
            list12 = [list[1],list[2]]
            #全て
            list012 = [list[0],list[1],list[2]]
            #結果と突き合わせ
            #上位3頭のみ抽出 平均を取る？
            #1着
            for kekka in list[3][:1]:
                sum += float(kekka)
                lis.append(kekka)
            #2着
            for kekka in list[3][1:2]:
                sum2 += float(kekka)
                lis2.append(kekka)
            #3着
            for kekka in list[3][2:3]:
                sum3 += float(kekka)
                lis3.append(kekka)
        #分散計算
        numlist = numpy.array(lis)
        numlist2 = numpy.array(lis2)
        numlist3 = numpy.array(lis3)
        #1着
        var = numpy.var(numlist)
        #2着
        var2 = numpy.var(numlist2)
        #3着
        var3 = numpy.var(numlist3)
        """
        if len(fi) == 5748:
            print (u"中京　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 5158:
            print (u"福島　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 3590:
            print (u"函館　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 9278:
            print (u"阪神　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 5472:
            print (u"小倉　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 9829:
            print (u"京都　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 9749:
            print (u"中山　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 5878:
            print (u"新潟　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 3691:
            print (u"札幌　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u"　3着：" + str(sum3 / len(fi)))
        if len(fi) == 9498:
            print (u"東京　1着：" + str(sum / len(fi)) + u"　2着：" + str(sum2 / len(fi)) + u" 　3着：" + str(sum3 / len(fi)))
        """

        if len(fi) == 5748:
            print (u"中京（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 5158:
            print (u"福島（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 3590:
            print (u"函館（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 9278:
            print (u"阪神（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 5472:
            print (u"小倉（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 9829:
            print (u"京都（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 9749:
            print (u"中山（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 5878:
            print (u"新潟（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　3着：" + str(var3))
        if len(fi) == 3691:
            print (u"札幌（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u"　 3着：" + str(var3))
        if len(fi) == 9498:
            print (u"東京（分散）　1着：" + str(var) + u"　2着：" + str(var2) + u" 　3着：" + str(var3))

#特徴抽出
#main()
#特徴ベクトル作成
#vector()
#分析
analysis()

