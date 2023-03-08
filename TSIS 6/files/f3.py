import os
print("Test a path exists or not:")
path = r'/Users/aidaaarik/Desktop/PP3'
print(os.path.exists(path))
path = r'/Users/aidaaarik/Desktop/PP2'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))