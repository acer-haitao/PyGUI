# -*- coding utf-8 -*-
import urllib.request
import json
import os



save_dir = "D:\英雄联盟皮肤"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for i in range(142,150):
    for cnt in range(0,9):
        #save_file_name = "D:\英雄联盟皮肤\\"  +str(hero_json[i]['ename'])+'-'+ hero_json[i]['cname'] + '-' + skin_name[cnt] + '.jpg'
        save_file_name = "D:\英雄联盟皮肤\\" + str(i)+'00'+str(cnt)+'.jpg'
        #http://ossweb-img.qq.com/images/lol/web201310/skin/big143000.jpg
        skin_url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big'+str(i)+'00'+str(cnt)+'.jpg'
        print("正在下载第%d张图片......" % i)
        print(skin_url)
        if not os.path.exists(save_file_name):
            try:
                urllib.request.urlretrieve(skin_url,save_file_name)
            except:
                continue #发生异常仍继续

print("图片下载完成.....")




