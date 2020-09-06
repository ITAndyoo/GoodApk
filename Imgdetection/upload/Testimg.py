#!/usr/bin/python
from django.conf import settings
import os

import os
import sys
import zipfile
#import test2

def unzip(filename: str):
    try:
        file = zipfile.ZipFile(filename)
        dirname = filename.replace('.zip', '')
        # 如果存在与压缩包同名文件夹 提示信息并跳过
        if os.path.exists(dirname):
            print(f'{filename} dir has already existed')
            return
        else:
            # 创建文件夹，并解压
            os.mkdir(dirname)
            file.extractall(dirname)
            file.close()
            # 递归修复编码
            rename(dirname)
    except:
        print(f'{filename} unzip fail')


def rename(pwd: str, filename=''):
    """压缩包内部文件有中文名, 解压后出现乱码，进行恢复"""
    
    path = f'{pwd}/{filename}'
    if os.path.isdir(path):
        for i in os.scandir(path):
            rename(path, i.name)
    newname = filename.encode('cp437').decode('gbk')
    os.rename(path, f'{pwd}/{newname}')




def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(fullname + "\n")
                    break

def Test(dir,apkname):
    #outfile = dir + "/imgpath.txt"                     #写入的txt文件名
    outfile =  os.path.join(settings.MEDIA_ROOT,'result',apkname.split('.')[0]+"_res.txt") 
    wildcard = ".jpg .png .jpeg .bmp .tif"      #要读取的文件类型；
    file = open(outfile,"a")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir,file,wildcard, 1)
    file.close()

def Testimage(res_name):
    #res_name='2.apk'
    apkurl = os.path.join(settings.MEDIA_ROOT,'images',res_name) 
    zipurl = os.path.join(settings.MEDIA_ROOT,'images',res_name.split('.')[0]+'.zip')
    os.rename(apkurl,zipurl)
    
    unzip(zipurl)
    url = os.path.join(settings.MEDIA_ROOT,'images',res_name.split('.')[0])
    
    Test(url,res_name)

    #with open(url+'/imgpath.txt', 'r', encoding='utf-8') as file:
    #  for img_path in file.readlines() :
    #        img_path=img_path.strip('\n')
    #        test2.extract(img_path)
    #   file.close()
        
