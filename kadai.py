import os.path
import glob
from traceback import print_tb

homedirectory = os.path.expanduser('~/univ_lesson/*')

def Filefind(path, extension):
  files = glob.glob(path)
  for file in files:
      if(os.path.isdir(file)):
        Filefind(file +"/*",  extension)
      if(file.endswith(extension)): #fileの拡張子が引数extensionと一致していたらprint
        print(file)

Filefind(homedirectory, ".py")