#!/usr/local/bin/python3

import os
import sys
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if(len(sys.argv) > 1):
    folder = sys.argv[1]
else:
    folder = "."

# capture the filenames from a folder
def ls( folder ):
    cmd = ["ls", "-l", folder]
    # print("\n\nRunning " + "".join([n + " " for n in cmd]))
    lsoutput = subprocess.check_output(cmd).decode('utf-8').split('\n')
    names = [x.split()[8] for x in lsoutput if len(x.split()) == 9]
    return names;

# class for git status result
class GitStatus: 
    def __init__(self,folder): 
        self.folder = folder
        self.branch = ""
        self.message = ""
        self.color = None
    def toInfo(self,a,b):
        result = self.folder.ljust(a) + '[' +self.branch.center(b) +'] > ' +self.message
        if self.color != None:
            result = self.color + result + bcolors.ENDC
        return result
    def __str__(self):
        result = self.toInfo(len(self.folder)+2,len(self.branch)+2)
        return result
    def process(self,output):
        msgFilter = [
            "nothing to commit, working tree clean",
            "Changes to be committed:",
            "Untracked files:",
            "Changes not staged for commit:"]
        self.message = "".join([msg.replace(':','')+", " for msg in output if msg in msgFilter] )
        self.color = bcolors.OKGREEN if self.message == msgFilter[0]+", " else bcolors.FAIL

 
# capture the filenames from a folder
def gs( folder ):
    result = GitStatus(folder)
    cmd = ["git","status"]
    # print("\n\nRunning " + "".join([n + " " for n in cmd]))
    os.chdir(folder)
    try:
        output = subprocess.check_output(cmd,stderr=subprocess.STDOUT).decode('utf-8').split('\n')
        result.branch = output[0].split()[2]
        result.process(output)
    except subprocess.CalledProcessError as err:
        # print(err.output.decode('utf-8'))
        result.message = err.output.decode('utf-8').split('\n')[0]
    # print(str(result))
    return result;

folders = ls(folder)

# print("\n\n")
# print(folders)
# print("\n\n")

results = []
for line in folders:
    # print("Processing..."+line)
    r = gs(folder+"/"+line)
    print(r.toInfo(40,16))
    results.append(r)

# print("##### RESULTS #####")
# for r in results:
#     print(r.toInfo(40,16))

