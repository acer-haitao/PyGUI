# -*- coding utf-8 -*-
import urllib.request
import json
import os
import time
import MySQLdb
import pymysql as pymysql

response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")
hero_json = json.loads(response.read())
hero_num = len(hero_json)

#英雄数量
print(hero_json)
print("英雄数量：",str(hero_num))

#英雄皮肤数量
for i in range(1,hero_num):
    hero_name = hero_json[i]['cname']
    skin_name = hero_json[i]['skin_name'].split('|')
    skin_num = len(skin_name)
    print("英雄：",hero_name,"总共拥有:",skin_num,"款皮肤",":",skin_name)

save_dir = "D:\王者荣耀皮肤1"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

def DbinsertALIYUN():
    Strtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        db = pymysql.connect("bdm273925510.my3w.com","bdm273925510","haitao131","bdm273925510_db",charset='utf8')
    except Exception as e:
        print("数据库连接失败",e)

    # 使用cursor()方法获取操作游标
    try:
        cursor = db.cursor()
    except Exception:
        print("获取操作游标异常",Exception)
    sql = """INSERT INTO WZRY(id,name,skinname,skinurl,time) VALUES (%s,%s,%s,%s,%s) """
    try:
    # 执行sql语句
        print("Start insert ....")
        print(sql)
        print(db,cursor)
        try:
            print(str(hero_json[i]['ename']),hero_json[i]['cname'],skin_name[cnt],skin_url,Strtime)
            cursor.execute(sql,[str(hero_json[i]['ename']),hero_json[i]['cname'],skin_name[cnt],skin_url,Strtime])
        except Exception as e:
            print("执行SQL语句异常:",e)
    # 提交到数据库执行
        db.commit()
        print("Finish insert .....")
    except Exception:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
        db.close()
        print("发生异常:",Exception)

for i in range(hero_num):
    skin_name = hero_json[i]['skin_name'].split('|')
    for cnt in range(len(skin_name)):
        save_file_name = "D:\王者荣耀皮肤1\\"  +str(hero_json[i]['ename'])+'-'+ hero_json[i]['cname'] + '-' + skin_name[cnt] + '.jpg'
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(hero_json[i]['ename'])+ '/' +str(hero_json[i]['ename'])+'-bigskin-' + str(cnt+1) +'.jpg'
        id = str()
        print("正在下载第%d张图片......" % i)
        print(skin_url)
        if not os.path.exists(save_file_name):
            try:
                urllib.request.urlretrieve(skin_url,save_file_name)
                DbinsertALIYUN()
            except Exception as e:
                print("下载异常:",e)
print("图片下载完成.....")




