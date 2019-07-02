import os
import h5py

#HDF5 File Dirdory
sep = os.sep
s111_Point = os.getcwd() + sep + '..'+sep+'..' + sep +"resource" + sep+"s111" + sep + "111_area.h5"
print("path ="+s111_Point)

##파일 체크
isFileCheck = os.path.exists(s111_Point)

if isFileCheck :
    print("is File")
    f = h5py.File(s111_Point, 'r')
    #reader attribute
    dic = f.attrs.keys()
    for i in dic:
        print('Name = {0} ,Value ={1}'.format(i,f.attrs.get(i)))






    f.close()
else :
    print("is Not File")