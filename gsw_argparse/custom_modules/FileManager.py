from pathlib import PurePath
import os
from custom_modules.FileValidator import isDir, isFile, isSymLink


class File:
    def __init__(this, filePath):
        this.name = PurePath(filePath).name
        this.absolutePath = os.path.abspath(filePath)
        this.ext = PurePath(filePath).suffix
        this.file = isFile(filePath)
        this.dir = isDir(filePath)
        this.symlink = isSymLink(filePath)
        this.parent = PurePath(filePath).parent

    def getName(this, withoutExt=False):
        if withoutExt:
            return this.name.split('.')[0]
        else:
            return this.name

    def getAbsolutePath(this):
        return this.absolutePath

    def getParent(this):
        return this.parent

    def getExt(this):
        return this.ext

    def isFile(this):
        return this.file

    def isDir(this):
        return this.dir

    def isSymLink(this):
        return this.symlink

    def __repr__(self) -> str:
        return self.name


class FileManager:
    def __init__(self):
        self.files = dict()

    def addFile(self, filePath):
        file = File(filePath)
        self.files.update({
            file.getName(): file
        })

    def removeFile(self, fileName):
        del self.files[fileName]

    def getFiles(self):
        return self.files

    def getFile(self, name):
        if name in self.files:
            return self.files[name]

    def getFileCount(self):
        return len(self.files)

    def hasFile(self):
        return len(self.files) > 0

    def __repr__(self) -> str:
        return "File Manager"


fm = FileManager()
