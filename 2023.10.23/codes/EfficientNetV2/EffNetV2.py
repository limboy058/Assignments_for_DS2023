import argparse
import os

from Evaluate import evaluate
from Train import train
from demo import demo
from Utils import classes_txt

parser = argparse.ArgumentParser(description='EfficientNetV2 arguments')
parser.add_argument('--mode', dest='mode', type=str, default='demo', help='Mode of net')
parser.add_argument('--epoch', dest='epoch', type=int, default=50, help='Epoch number of training')
parser.add_argument('--batch_size', dest='batch_size', type=int, default=512, help='Value of batch size')
parser.add_argument('--lr', dest='lr', type=float, default=0.0001, help='Value of lr')
parser.add_argument('--img_size', dest='img_size', type=int, default=32, help='reSize of input image')
parser.add_argument('--data_root', dest='data_root', type=str, default='D:/data/data/', help='Path to data')
parser.add_argument('--log_root', dest='log_root', type=str, default='2023.10.23/codes/EfficientNetV2/log/', help='Path to model.pth')
parser.add_argument('--num_classes', dest='num_classes', type=int, default=3755, help='Classes of character')
args = parser.parse_args()


if __name__ == '__main__':
    if not os.path.exists(args.data_root + 'train.txt'):
        classes_txt(args.data_root + 'train', args.data_root + 'train.txt', args.num_classes)
    if not os.path.exists(args.data_root + 'test.txt'):
        classes_txt(args.data_root + 'test', args.data_root + 'test.txt', args.num_classes)

    if args.mode == 'train':
        train(args)
    elif args.mode == 'evaluate':
        evaluate(args)
    elif args.mode == 'demo':
        demo(args)
    else:
        print('Unknown mode')
