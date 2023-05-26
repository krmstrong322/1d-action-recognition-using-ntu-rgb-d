import pandas as pd
import numpy as np
import scipy
from tqdm import tqdm
import os

def rotational_velocity(rotation):
    r_vel = []
    for i in range(len(rotation)-1):
        r_vel.append((rotation[i+1] - rotation[i]) / (i+1 - i))
    return r_vel

def rotational_accel(rot_vel):
    r_accel = []
    for i in range(len(rot_vel)-1):
        r_accel.append((rot_vel[i+1] - rot_vel[i]) / (i+1 - i))
    return r_accel

def work_done_NEW(biomechanic, lb=None, ub=None):
    wd_list =[]
    for i in range(len(biomechanic)):
        wd_list.append((biomechanic[i] - min(biomechanic)))
    if lb and ub is not None:
        work_done = np.trapz(wd_list[lb:ub])
    else:
        work_done = np.trapz(wd_list)
    return work_done

def range_of_motion(input):
    return max(input) - min(input)

def mean(input):
    return np.mean(input)

def median(input):
    return np.median(input)

def std(input):
    return np.std(input)

def smoothness(input):
    return np.std(np.gradient(input))

def variance(input):
    return np.var(input)

def skewness(input):
    return scipy.stats.skew(input)

def kurtosis(input):
    return scipy.stats.kurtosis(input)

def energy(input):
    return np.sum(np.square(input))

def create_dict(input):
    return dict(zip(['range_of_motion', 'mean', 'median', 'std', 'smoothness', 
                     'impulse', 'variance', 'skewness', 'kurtosis', 'energy'], 
                    [range_of_motion(input), mean(input), median(input), std(input), smoothness(input),
                     work_done_NEW(rotational_accel(rotational_velocity(input))), variance(input), 
                     skewness(input), kurtosis(input), energy(input)]))

final_processed_data = {}

for i in os.listdir('biomechanics/'):
    for j in tqdm(os.listdir('biomechanics/{}'.format(i))):
        data = pd.read_csv('biomechanics/{}/{}'.format(i,j))
        processed_data = {}
        for k in data.columns.to_list()[:-1]:
            processed_data[k] = create_dict(data[k].to_list())
        processed_df = pd.DataFrame(processed_data)
        flat_list = processed_df.values.flatten().tolist()
        flat_list.append(str(j[16:-13]))
        final_processed_data[j] = flat_list
final_processed_df = pd.DataFrame(final_processed_data)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(df.fruit)
df['categorical_label'] = le.transform(df.fruit)


print(final_processed_df.T.shape)
final_processed_df.T.to_csv('biomechanics_processed.csv', index=False)



            
"""data = pd.read_csv('biomechanics/A041/S001C001P001R001A041.skeleton.csv')
for i in data.columns.to_list()[:-1]:
    final_processed_data[i] = final_processed_data[i] = create_dict(data[i].to_list())

df = pd.DataFrame(final_processed_data)
print(df)
flat_list = df.values.flatten().tolist()
print(len(flat_list))"""