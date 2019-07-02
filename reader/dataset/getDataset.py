import os
import h5py
import numpy as np

#HDF5 File Dirdory
sep = os.sep
s111_Point = os.getcwd() + sep + '..'+sep+'..' + sep +"resource" + sep+"s111" + sep + "111_area.h5"
print("path ="+s111_Point)

##파일 체크
isFileCheck = os.path.exists(s111_Point)

if isFileCheck :
    print("is File")
    f = h5py.File(s111_Point, 'r')
    #reader dataset
    dataset = f['SurfaceCurrent/SurfaceCurrent.01/group_2019061415']
    direction =dataset['Direction']
    print('Direction============')
    print('name = {0}'.format(direction.name))
    dirArr = np.array(direction)
    print('get Value = {0}'.format(dirArr))
    print('min Value ={0}, max Value ={1}'.format(dirArr.min(),dirArr.max()))
    ############################################################################
    print('Velocity============')
    velocity = dataset['Velocity']
    print('name = {0}'.format(velocity.name))
    velArr = np.array(velocity)
    print('get Value = '.format(velArr))
    print('min Value ={0}, max Value ={1}'.format(velArr.min(), velArr.max()))




    f.close()
else :
    print("is Not File")