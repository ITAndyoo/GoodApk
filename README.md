### 文档说明

* crnn_chinese_characters_rec-master文件夹

  > 1.包含了基于crnn文字识别训练crnn_main_v2.py，可以下载数据集或通过data_generator生成数据进行训练
  >
  > 2.测试文件test_crnn_dfa.py，功能是用已经训练好的模型（在trained_models下）进行图片文字提取并采用DFA算法检测敏感词

* GenReport文件夹

  > 包含了一个简单的html转pdf生成检测报告的样例

* Imgdetection文件夹

  > 包含了基于Django的项目网站部署，其中upload文件夹是用户上传的apk以及中间处理及检测处理结果

### 项目环境

> 本地：PyCharm2018.3.1
>
> 线上：Apache2.4 + AliCloud Centos7