# alldel

## Script to delete all selected files in the selected directory

A certain program produces temporary files during work that are useful as long as the work is done. However, after the work is finished, these temporary files are not deleted by this program. There is a problem with deleting files that are no longer needed, which increases with their number. Manually deleting them is out of the question, because it is easy to make a mistake and delete an important file.

I solved this problem by employing python, writing a script that was supposed to be lightweight, with easy access to it. The script was supposed to work only in the Windows environment, it is enough to operate in the command line and the capabilities of the operating system.

The script is simple, after double-clicking, a window opens to indicate the appropriate directory, in which all specified files will be deleted. The directory selection window also has a *Cancel* button, after selecting which no action takes place. At the end, an appropriate message is displayed.

![alldel img](https://github.com/user-attachments/assets/b5a55310-8e44-47e2-8b11-34e69a61cd80)

For correct operation, the script **expects an argument** in the form of the *extension* of the files we want to delete. The lack of this argument results in an error message. If a mistake occurs in the extension name, the consequences can be dire, for which I take no responsibility.

## Installation

Copy the *alldel.py* and *ctx.py* files into one directory. The *ctx.py* library is so universal that it can be placed in the *library directory* shared by python. Then, create a *shortcut* to the *alldel.py* file and open its **properties**. In the *Target element* field, add the argument of the *extension* of the files you want to delete to the launch path:

`Target element: G:\...\alldel.py tmp`

Finally, the *shortcut* created in this way can be placed on the desktop. Depending on your needs, you can set a convenient keyboard shortcut in the shortcut properties. This way, you can have a few such shortcuts for other types of files.
