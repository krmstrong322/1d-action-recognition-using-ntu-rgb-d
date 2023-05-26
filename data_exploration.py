import numpy as np
import pandas as pd
"""
# Load the data
data = np.load(r'skeletons/A041/S001C001P001R001A041.skeleton.npy', allow_pickle=True)
#print(data.item())
data_list = []
for i in data.item()['skel_body0']:
    data_list.append(i.flatten())
#print(len(data_list))
#print(data_list[0].flatten())
#
#print(data.item()['skel_body0'][0])
#df = pd.DataFrame(data_list)
#print(df.head())
#print(df.shape)
"""
import os
from functions import *
import tqdm as tqdm

joint_order = {
    1:"base of the spine", 2:"middle of the spine", 3:"neck", 4:"head",
    5:"left shoulder", 6:"left elbow", 7:"left wrist",
    8:"left hand", 9:"right shoulder", 10:"right elbow",
    11:"right wrist", 12:"right hand", 13:"left hip",
    14:"left knee", 15:"left ankle", 16:"left foot",
    17:"right hip", 18:"right knee", 19:"right ankle",
    20:"right foot", 21:"spine", 22:"tip of the left hand",
    23:"left thumb", 24:"tip of the right hand", 25:"right thumb"
}

joint_order_modified = {
    1: "pelvis_x", 2: "pelvis_y", 3: "pelvis_z",
    4: "spine_x", 5: "spine_y", 6: "spine_z",
    7: "neck_x", 8: "neck_y", 9: "neck_z",
    10: "head_x", 11: "head_y", 12: "head_z",
    13: "shoulder_l_x", 14: "shoulder_l_y", 15: "shoulder_l_z",
    16: "elbow_l_x", 17: "elbow_l_y", 18: "elbow_l_z",
    19: "wrist_l_x", 20: "wrist_l_y", 21: "wrist_l_z",
    22: "hand_l_x", 23: "hand_l_y", 24: "hand_l_z",
    25: "shoulder_r_x", 26: "shoulder_r_y", 27: "shoulder_r_z",
    28: "elbow_r_x", 29: "elbow_r_y", 30: "elbow_r_z",
    31: "wrist_r_x", 32: "wrist_r_y", 33: "wrist_r_z",
    34: "hand_r_x", 35: "hand_r_y", 36: "hand_r_z",
    37: "hip_l_x", 38: "hip_l_y", 39: "hip_l_z",
    40: "knee_l_x", 41: "knee_l_y", 42: "knee_l_z",
    43: "ankle_l_x", 44: "ankle_l_y", 45: "ankle_l_z",
    46: "foot_l_x", 47: "foot_l_y", 48: "foot_l_z",
    49: "hip_r_x", 50: "hip_r_y", 51: "hip_r_z",
    52: "knee_r_x", 53: "knee_r_y", 54: "knee_r_z",
    55: "ankle_r_x", 56: "ankle_r_y", 57: "ankle_r_z",
    58: "foot_r_x", 59: "foot_r_y", 60: "foot_r_z",
    61: "spine_chest_x", 62: "spine_chest_y", 63: "spine_chest_z",
    64: "handtip_l_x", 65: "handtip_l_y", 66: "handtip_l_z",
    67: "thumb_l_x", 68: "thumb_l_y", 69: "thumb_l_z",
    70: "handtip_r_x", 71: "handtip_r_y", 72: "handtip_r_z",
    73: "thumb_r_x", 74: "thumb_r_y", 75: "thumb_r_z"
}

for i in os.listdir('skeletons/'):
    for j in tqdm.tqdm(os.listdir('skeletons/{}'.format(i))):
        data = np.load('skeletons/{}/{}'.format(i,j), allow_pickle=True)
        data_list = []
        for k in data.item()['skel_body0']:
            data_list.append(k.flatten())
        try:
            df = pd.DataFrame(data_list, columns=joint_order_modified.values())
            df.to_csv('csv/{}/{}.csv'.format(i,j[:-4]), index=False)
            biomechanics_df = create_dataset_st(df)
            biomechanics_df.to_csv('biomechanics/{}/{}.csv'.format(i,j[:-4]), index=False)
        except ZeroDivisionError:
            continue
        #print('csv/{}/{}.csv'.format(i,j[:-4]))
        #print('biomechanics/{}/{}.csv'.format(i,j[:-4]))