import pickle

import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from model import efficientnetv2_s

from Utils import find_max_log, has_log_file


def demo(args):
    print('==Demo EfficientNetV2===')
    testpath=open('D:/data/data/test.txt')
    transform = transforms.Compose(
            [transforms.Resize((args.img_size, args.img_size)), transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    model = efficientnetv2_s(num_classes=args.num_classes)
    model.eval()
    if has_log_file(args.log_root):
        file = find_max_log(args.log_root)
        print("Using log file: ", file)
        checkpoint = torch.load(file)
        model.load_state_dict(checkpoint['model_state_dict'])
    else:
        print("Warning: No log file")
    while 1:
        for i in range(1,100):
            path=testpath.readline()
        path=path.replace('\\','/')
        path=path.replace('\n','')
        print('Input Image: ', path)
        img = Image.open(path)
        plt.imshow(img)
        plt.axis('on') # 关掉坐标轴为 off
        plt.title('image') # 图像题目
        
        img = transform(img)
        img = img.unsqueeze(0)
        

        with torch.no_grad():
            output = model(img)
        _, pred = torch.max(output.data, 1)
        f = open('2023.10.23/codes/EfficientNetV2/char_dict.txt', 'rb')
        dic = pickle.load(f)
        for cha in dic:
            if dic[cha] == int(pred):
                print('predict: ', cha)
        plt.show()
        f.close()
