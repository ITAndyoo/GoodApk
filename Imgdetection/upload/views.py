# -*- coding : utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.conf import settings
from upload.models import File
import os,subprocess

import os
import sys
import zipfile
import re
import sys
import time
from upload.Testimg import Testimage

def getAppBaseInfo(apkpath,res):
    #检查版本号等信息
    aaptinfo = subprocess.Popen("/opt/software/sdks/android/sdk/build-tools/25.0.2/aapt d badging %s" % apkpath, shell=True, stdout=subprocess.PIPE)
    output = aaptinfo.stdout.read() 
    output = bytes.decode(output)
    #print (output)
    match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)' platformBuildVersionName='\S+'").match(output)
    if not match:
        raise Exception("can't get packageinfo")

    packagename = match.group(1)
    versionCode = match.group(2)
    versionName = match.group(3)
    with open(res, 'w', encoding='utf-8') as f:
        f.write("Apk Package's Name:" + packagename + "\n" + "The Version of Code:" + versionCode + "\n" + "The Version of Apk:" + versionName + "\n")

        outList = output.split('\n')
        for line in outList:
            if line.startswith('uses-permission:'):
                f.write(line.split('=')[1] + "\n")
    #f.close()
    #def getCurrentDirApk():
    #    for dir in os.walk(os.curdir):
    #        for filename in dir[2]:
    #            if os.path.splitext(filename)[1] == '.apk':
    #                print('find apk:', filename)
    #                return filename
    #def insertFile(apkName, f):
    #    output = os.popen("/opt/software/sdks/android/sdk/build-tools/25.0.2/aapt a %s %s" % (apkName, f)).read()

#if __name__ == "__main__":
    #获得apk名
    #if len(sys.argv) == 1:
    #    apkName = getCurrentDirApk()
    #else:
    #    apkName = sys.argv[1]
    #if not apkName:
    #    print('can not find apk!!!')
    #    exit()
    #getAppBaseInfo(apkName)
    #向apk中插入文件
    #insertfile = 'insertfile.txt'
    #f = open(insertfile, "w+")

def uploadfile(request):
    
    if request.method == "GET":
        return render(request,'upload.html')
    else:
        fileName = request.FILES.get('picture')
        url = os.path.join(settings.MEDIA_ROOT,'images', fileName.name)
        read=open(url,'wb+')
        for chunk in fileName.chunks():
            read.write(chunk)
        read.close()
        #Upload Successfully
        str1=fileName.name 
        res_url = os.path.join(settings.MEDIA_ROOT,'result',str1.split(".")[0]+'_res.txt')
        #f=open(res_url,'wb+')
        
        #获取上传的apk的基本信息，输出到指定文件夹以供下载
        #res=os.popen('python3.6 ./images/Testapk2.py ./images/'+ fileName.name + ' > ./result/' + str1.split(".")[0]+'_res.txt')
        dist = {}
        dist['status'] = "Test Successfully!"
        try:
            getAppBaseInfo(url,res_url)
        except Exception :
            dist['status'] = 'Info Test Error!(Maybe this apk cannot be analyzed)'    
        #try:
        Testimage(str1)
        #except Exception :
        #    dist['status'] = 'Images Test Error!'

        #cmd='python3.6 ./images/Testapk2.py ./images/'+ fileName.name
        #cmd=cmd.split(" ")
        #Apkinfo=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE)
        #byte_content=Apkinfo.stdout.read()
        #Apkinfo
        #str_content=byte_content.decode('gbk')
        #f.write(str_content)
        #f.close()
        dist['test_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dist['apk_name'] = str1
        dist['res_link'] = res_url
        dist['res_file'] = str1.split(".")[0]+'_res.txt'

        return render(request,'upload.html',dist)
#models.File.objects.update_or_create(file=fileName)

def downloadfile(request,data):


    def file_itertor(file_name,chunk_size=512):
        with open(file_name) as f:
            while True:
                c=f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    file_name=os.path.join(settings.MEDIA_ROOT,'result',data)
    download_file= data
    response=StreamingHttpResponse(file_itertor(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(download_file)
    return response
