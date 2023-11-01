import torchvision
import torch
from torchvision import datasets, transforms
from torch.autograd import Variable
import matplotlib.pyplot as plt

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(), torch.nn.MaxPool2d(stride=2, kernel_size=2))
        self.dense = torch.nn.Sequential(torch.nn.Linear(14 * 14 * 128, 1024),
                                         torch.nn.ReLU(),
                                         torch.nn.Dropout(p=0.5),
                                         torch.nn.Linear(1024, 10))

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 14 * 14 * 128)
        x = self.dense(x)
        return x

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize(mean=[0.5], std=[0.5])])

data_test = datasets.MNIST(root="./data/", transform=transform, train=False)


data_loader_test = torch.utils.data.DataLoader(dataset=data_test,
                                          batch_size = 4,
                                          shuffle = True)


# 在CPU上加载GPU上保存的模型
model = Model()
device = torch.device('cpu')
model.load_state_dict(torch.load("./2023.10.23/codes/12_practice/model_parameter.pkl", map_location=device))

# # 在GPU上加载GPU保存的模型
# model=Model()
# device = torch.device('cuda')
# model.load_state_dict(torch.load("./2023.10.23/codes/12_practice/model_parameter.pkl"))
# model.to(device)
# # Make sure to call input = input.to(device) on any input tensors that you feed to the model

X_test, y_test = next(iter(data_loader_test))
# X_test, y_test = X_test.to(device), y_test.to(device) #如果选择了加载到GPU上的话
inputs = Variable(X_test)
pred = model(inputs)
_,pred = torch.max(pred, 1)

print("Predict Label is:", [ i for i in pred.data])
print("Real Label is:",[i for i in y_test])

img = torchvision.utils.make_grid(X_test)
img = img.cpu().numpy().transpose(1,2,0)

std = [0.5]
mean = [0.5]
img = img*std+mean
plt.imshow(img)
plt.show()
