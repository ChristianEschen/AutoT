import torch.nn as nn
import torch.nn.functional as F
# class Net(nn.Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.conv1 = nn.Conv2d(3, 6, 5)
#         self.fc1 = nn.Linear(6 * 5 * 5, 2)
#         print('hej')
#     def forward(self, x):
#         x = F.relu(self.conv1(x))
#         x = x.view(-1, 6 * 5 * 5)
#         x = F.sigmoid(self.fc1(x))
#         #x = F.relu(self.fc2(x))
#         #x = self.fc3(x)
#         return x

class Net(nn.Module):
    def __init__(self, num_classes=2):
        super(Net, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc = nn.Linear(256*256*32, num_classes)
        
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out
