import sys
from termcolor import colored
from os import listdir
from os.path import isfile, join 
arguments = len(sys.argv)
def banner():
  print (colored("""
    _______  ________   ______           __             
   /_  __/ |/ /_  __/  / ____/________ _/ /_  ___  _____
    / /  |   / / /    / / __/ ___/ __ `/ __ \/ _ \/ ___/
   / /  /   | / /    / /_/ / /  / /_/ / /_/ /  __/ /    
  /_/  /_/|_|/_/     \____/_/   \__,_/_.___/\___/_/     
                                                        
  ""","blue"))
  print (colored("==========================================","yellow"))
  print (colored("A small guide for TXT Graber","green"))
  print (colored("python txtgraber.py DirPath OutPutFile.txt","green"))
  print (colored("==========================================","yellow"))

if arguments > 3:
  print (colored("Ops! Too Much inputs","red")) 
  print (colored("==========================================","red"))   
  banner()
elif arguments == 2 or sys.argv[1] == "help":
  banner()
  
else:
  folder_path = sys.argv[1]
  outputFile = sys.argv [2]
  # get the full names of all the txt files in your folder   
  files = [join(folder_path, f) for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.endswith(".txt")] 

  f = open(outputFile, 'a')   
  

  for file in files:
      lines_seen = set() # holds lines already seen
      lines = open(file,"r").readlines() # line will be equal to the second line of the file
      for line in lines:
          if not (line.startswith("#") or line.startswith(" ")):
              f.write(line)   
  f.close()
  banner()
  print (colored("Grabed all Text in .txt files in the Directory","green"),folder_path,colored("is completed","green"))
  print (colored("You can find them in","green"),outputFile)
  # print (colored("python txtgraber.py DirPath OutPutFile.txt","green"))
