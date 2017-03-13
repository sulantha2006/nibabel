from nibabel import minc2

f = minc2.load('/home/sulantha/PycharmProjects/pyVoxelStats/VoxelStatsTestData/MINC/I301481.mnc')

x = minc2.save(f, '/home/sulantha/Desktop/TestWrite.mnc')

print('F')