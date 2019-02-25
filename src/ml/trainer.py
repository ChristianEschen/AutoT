import matplotlib.pyplot as plt
import torch
import os
from torch.utils import data
import numpy as np
from data_loader import TinderDataLoader
from torchvision import transforms
from Networks import Net
import torch.nn as nn
import torch.optim as optim
import torchvision
from visdom import Visdom
import time
train_transform = transforms.Compose([
        transforms.RandomCrop((1024,1024), padding=0, pad_if_needed=True),
        transforms.Resize((224,224), interpolation=2),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])
# CUDA for PyTorch
use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")
#cudnn.benchmark = True

# Parameters
params = {'batch_size': 4,
          'shuffle': True,
          'num_workers': 0}
max_epochs = 100

# Datasets
# Training
train_images = 'data/images_processed_train'
labels='data/Label_list_train.csv'
train_images='/home/christian/Projects/AutoT/data/images_processed_train'
labels='/home/christian/Projects/AutoT/data/Label_list_train.csv'

# Validation
val_images = 'data/images_processed_val'
labels_val='data/Label_list_val.csv'
val_images='/home/christian/Projects/AutoT/data/images_processed_val'
labels_val='/home/christian/Projects/AutoT/data/Label_list_val.csv'

# Generators
training_set = TinderDataLoader(labels,train_images,transform=train_transform)
training_generator = data.DataLoader(training_set, batch_size=params['batch_size'],
                        shuffle=True, num_workers=params['num_workers'])

# Generators
validation_set = TinderDataLoader(labels_val,val_images,transform=train_transform)
validation_generator = data.DataLoader(validation_set, batch_size=params['batch_size'],
                        shuffle=True, num_workers=params['num_workers'])

data_loaders = {"train": training_generator , "val": validation_generator}
data_lengths = {"train": len(training_generator), "val": len(validation_generator)}
viz = Visdom(port=6025, server='localhost')
#net = Net()
net = torchvision.models.resnet152(pretrained=False, num_classes=2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
print('start for loop')
for epoch in range(max_epochs):
    epoch_start_time = time.time()
    iter_data_time = time.time()
    epoch_iter=0
    for phase in ['train', 'val']:
        if phase == 'train':
            #optimizer = scheduler(optimizer, epoch)
            net.train(True)  # Set model to training mode
        else:
            net.train(False)  # Set model to evaluate mode

        running_loss = 0.0
        for i, data in enumerate(training_generator, 0):
            print('sube',i)
            print('len',len(training_generator))
            iter_start_time = time.time()
            
            epoch_iter+=params['batch_size']
            inputs = data['image']
            labels = data['label']

            if phase=='train':
                optimizer.zero_grad()
            outputs = net(inputs)

            loss = criterion(outputs, labels.long())
            if phase=='train':
                loss.backward()
                optimizer.step()
            viz.line(
                X=np.array([epoch + 1]),
                Y=np.array([loss.detach().numpy()]),
                win="test",
                opts={
                        'title':phase+'loss'},
                name='Line1',
                update='append',
            )

        # with torch.set_grad_enabled(False):
        #     for j, data_val in enumerate(validation_generator, 0):
        #         # Transfer to GPU
        #         inputs_val = data_val['image']
        #         labels_val = data_val['label']
        #         outputs_val = net(inputs_val)
        #         loss_val = criterion(outputs_val, labels_val.long())            
        #         # Model computations
        #         viz.line(
        #         X=np.array([i + 1]),
        #         Y=np.array([loss_val.detach().numpy()]),
        #         win="test2",
        #         opts={
        #                 'title':' val loss'},
        #         name='Line2',
        #         update='append',
        #     )