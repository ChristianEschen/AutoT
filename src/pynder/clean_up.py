import os
import shutil
output_folder = '/home/christian/PYNDER_PROJECT/Mined_data/'
output_folder_labels_subject =os.path.join(output_folder,'Labels_subject')#output_folder_labels ='/home/christian/PYNDER_PROJECT/Mined_data/Labels'
output_folder_img =os.path.join(output_folder,'images')#'/home/christian/PYNDER_PROJECT/Mined_data/Images'
output_folder_labels =os.path.join(output_folder,'Labels')#output_folder_labels ='/home/christian/PYNDER_PROJECT/Mined_data/Labels'
output_folder_bio =os.path.join(output_folder,'bio')#output_folder_bio='/home/christian/PYNDER_PROJECT/Mined_data/Bio'

liste=os.listdir(output_folder_labels_subject)

for folder in range(0,len(liste)):
    #print('folder',liste[folder])
    if len(os.listdir(os.path.join(output_folder_labels_subject,liste[folder]))) == 0:
        print("Directory is empty:",liste[folder])
        shutil.rmtree(os.path.join(output_folder_labels_subject,liste[folder]))
        shutil.rmtree(os.path.join(output_folder_labels,liste[folder]))
        shutil.rmtree(os.path.join(output_folder_bio,liste[folder]))
        shutil.rmtree(os.path.join(output_folder_img,liste[folder]))
    else:
        pass
       # print("Directory is not empty")