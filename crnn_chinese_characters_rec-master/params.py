import alphabets

random_sample = True
best_accuracy = 0.5
keep_ratio = False
adam = True
adadelta = False
saveInterval = 2
valInterval = 400
n_test_disp = 10
displayInterval = 1
experiment = './expr'   #训练模型保存文件夹
alphabet = alphabets.alphabet
crnn = ''
beta1 =0.5
#lr = 0.0001
lr = 0.001          #学习率
niter = 100
nh = 256
#imgW = 160
imgW = 280      #图片格式
imgH = 32
val_batchSize = 16      #测试集batch大小
#batchSize = 32         #训练集batch大小
batchSize = 32
workers = 2
std = 0.193
mean = 0.588
