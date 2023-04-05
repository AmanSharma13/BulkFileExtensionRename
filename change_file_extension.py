import glob
import os


for filename in glob.iglob(os.path.join(os.getcwd(), '*.webp')):
    os.rename(filename, filename[:-4] + '.jpg')
