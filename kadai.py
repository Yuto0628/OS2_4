import sys
import os.path
import glob
from traceback import print_tb


def Filefind(path, extension):
  files = glob.glob(path)
  for file in files:
      if(os.path.isdir(file)):
        Filefind(file +"/*",  extension)
      if(file.endswith(extension)): #fileの拡張子が引数extensionと一致していたらprint
        print(file)


error_message = '引数にパスと拡張子を入力してください'
home_directory = os.path.expanduser('~/univ_lesson/*')

#fileをコマンドラインから実行時に、調べたいディレクトリのpathと拡張子を入れることで、それぞれfind_directoryとfind_extensionに格納
if(len(sys.argv) == 3):
  find_directory = os.path.expanduser(sys.argv[1])
  find_extension = sys.argv[2]
  Filefind(find_directory, find_extension)
else:
  raise Exception(error_message)