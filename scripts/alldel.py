# alldel.py
# v. 1
# 2024 (C) DarekPages, Python 3.12.1
# Script to delete all selected files in the selected directory.
# You must pass the extension of the files to be deleted as an argument.
# ------------------------------------------------------------------------

from sys import argv, exit
from os import remove
from glob import glob
from tkinter import filedialog
from sys import path; path.append(r'ctx.py') #mark as comment if ctx.py library is placed in python shared directory
import ctx

try:
    anyext= argv[1]
except:
    print(ctx.bg_red, ctx.ft_bold_white,'ERROR ', ctx.clr)
    print('The file extension must be supplied as an argument!')
    print('> alldel.py', ctx.ft_italic_white, 'extension', ctx.clr)
    exit()

dircry= filedialog.askdirectory() #opening the directory selection window
count= 0
for lstfiles in glob(dircry+'/*.'+anyext): #file list
    count= count+1
    remove(lstfiles)    
if count>0:
    kolr= ctx.ft_red
else:
    kolr= ctx.ft_white #default chars
print('\n',ctx.ft_bold_white, ctx.bg_grey, 'alldel v. 1,', ctx.clr, ctx.ft_italic_white, ' 2024 (C) DarekPages', ctx.clr)
print('Catalog:', ctx.bg_blue, dircry, ctx.clr)
print(ctx.ft_black, ctx.bg_green, 'delete:', kolr, count, 'files .'+anyext, ctx.clr)
ar= input('- Enter key for'+ctx.ft_italic_red+' close'+ctx.clr)
