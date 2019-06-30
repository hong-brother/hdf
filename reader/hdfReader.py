import os
import h5py

#HDF5 File Dirdory
sep = os.sep
s111_Point = os.getcwd() +sep+'..'+ sep +"resource" + sep+"s111" + sep + "111_area.h5"
print("path ="+s111_Point)

##파일 체크
isFileCheck = os.path.exists(s111_Point)

if isFileCheck :
    print("is File")
    f = h5py.File(s111_Point, 'r')
    #1. read Group
    g1 =list(f.keys())[0]
    group = f[g1]
    print(group)
    data = list(f[g1])
    data1 = data[0]
    #https: // jehoons.github.io / hdf5 - format /
    print(data)



    f.close()
else :
    print("is Not File")