import torch.nn as nn
from torchvision import transforms
from PIL import Image

# 定义一个简单的CNN模型来执行灰度化
class GrayScaleCNN(nn.Module):
    def __init__(self):
        super(GrayScaleCNN, self).__init__()
        self.conv = nn.Conv2d(3, 1, kernel_size=1, stride=1, padding=0)  
        # 输入通道数为3，输出通道数为1，使用1x1卷积核进行灰度化

    def forward(self, x):
        return self.conv(x)

# 封装为函数，载入图像并执行灰度化，存储。
def convert_to_grayscale(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    image=image.convert("RGB")
    transform = transforms.Compose([transforms.ToTensor()])
    image = transform(image).unsqueeze(0)  # 添加批次维度

    model = GrayScaleCNN()
    gray_image = model(image)
    gray_image = gray_image.squeeze(0).squeeze(0).cpu().detach().numpy()
    gray_image = Image.fromarray((gray_image * 255).astype('uint8'), 'L')
    gray_image.save(output_image_path)


input_image_path = '2023.10.23/codes/1.png'  
output_image_path = '2023.10.23/codes/2.png' 
convert_to_grayscale(input_image_path, output_image_path)
