import os
print('Exist:', os.access('/Users/aidaaarik/Documents/ghujik.py', os.F_OK))
print('Readable:', os.access('/Users/aidaaarik/Documents/ghujik.py', os.R_OK))
print('Writable:', os.access('/Users/aidaaarik/Documents/ghujik.py', os.W_OK))
print('Executable:', os.access('/Users/aidaaarik/Documents/ghujik.py', os.X_OK))