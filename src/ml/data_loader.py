import torch
from torch.utils import data
import PIL
import os
import pandas as pd
from PIL import Image
import csv
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import numpy as np
class TinderDataLoader(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.csv_file= csv_file
        self.root_dir = root_dir
        self.transform = transform

        self.label_list=[]
        with open(self.csv_file, "rt") as csvfile:
            label = csv.reader(csvfile, delimiter='\t',lineterminator='\n',)
            for row in label:
                self.label_list.append(row)
    def __len__(self):
        return len(self.label_list)

    def __getitem__(self, idx):
        image=Image.open(os.path.join(self.root_dir,self.label_list[idx-1][0])+'.jpg')
        label= self.label_list[idx-1][1]
        label=torch.from_numpy(np.asarray(label).astype('float32'))

        if self.transform:
            image = self.transform(image)
        sample = {'image': image, 'label': label}


        return sample