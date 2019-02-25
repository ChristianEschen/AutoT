import matplotlib.pyplot as plt
import os
import csv
import numpy as np
import uuid
import webp
from PIL import Image
import imghdr
import shutil

def open_image(path_to_img):
    image = Image.open(path_to_img)
    return image

def write_to_csv(path,label,counts):
    with open(path,'a') as f1:
        writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
        writer.writerow([counts, label])

cpt = sum([len(files) for r, d, files in os.walk(os.path.join('data','images'))])
path =os.path.join('data','labels')
UIDs=os.listdir(path)
label_path_train = os.path.join('data','Label_list_train.csv')
if os.path.isfile(label_path_train)==True:
    os.remove(label_path_train)
label_path_val = os.path.join('data','Label_list_val.csv')
if os.path.isfile(label_path_val)==True:
    os.remove(label_path_val)
counts=[]
y=0
shutil.rmtree(os.path.join('data','images_processed_train'))
shutil.rmtree(os.path.join('data','images_processed_val'))
if os.path.isdir(os.path.join('data','images_processed_train'))==False:
    os.mkdir(os.path.join('data','images_processed_train'))
if os.path.isdir(os.path.join('data','images_processed_val'))==False:
    os.mkdir(os.path.join('data','images_processed_val'))

dim1=np.array([])
dim2=np.array([])
for i in range(0,len(UIDs)):
    label_i_path = os.path.join(path,UIDs[i])
    paths_individual_image_label =os.listdir(label_i_path)
    with open(os.path.join(label_i_path,paths_individual_image_label[0]), 'rt') as csvfile:
        label = csv.reader(csvfile, delimiter='\t',lineterminator='\n',)
        k=0
        for row in label:
            success=False
            try:
                image=open_image(os.path.join('data','images',UIDs[i],str(k)))
                success=True
                dim1=np.append(dim1,np.array(image).shape[0])
                dim2=np.append(dim2,np.array(image).shape[1])
            except:
                pass
            if success==True:
                if y<=int(cpt*0.7):
                    image.save(os.path.join(os.path.join('data','images_processed_train'),str(y)+'.jpg'))
                    write_to_csv(label_path_train,int(row[0]),y)
                elif y>int(cpt*0.7):
                    image.save(os.path.join(os.path.join('data','images_processed_val'),str(y)+'.jpg'))
                    write_to_csv(label_path_val,int(row[0]),y)
                y+=1
                print('y',y)
                k+=1
                counts.append(int(row[0]))
    print('i',i)

plt.subplot(1,2,1)
plt.hist(dim1, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram dim 1")
plt.subplot(1,2,2)
plt.hist(dim2, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram dim 2")
plt.show()

ID = range(len(counts))
print('number of positives',np.sum(np.array(counts)))
print('number of negatives',len(counts))
print('percentage positives of negatives',np.sum(np.array(counts))/len(counts))
