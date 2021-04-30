import sys
import os
import hashlib

#read from terminal
input = sys.argv
binaryFile = input[1]

#convert to hex: search for "FFD8FFE0"
print("type", type(binaryFile))
f = open(binaryFile, "rb")
data = f.read()
# print(data)

path = os.getcwd()
print ("The current working directory is %s" % path)
try:
    os.mkdir(path + "/Sayles")
except OSError:
    print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s " % path)

count = 0

class Carver:
    def __init__(self, fType, count):
        self.fileType = fType
        self.fileCount = count

    def writeToFolder(self, data):
        name = self.fileType + str(self.fileCount) + "." + self.fileType
        f = open(os.getcwd()+"/Sayles/" + name, "wb")
        f.write(data)
        print("File Type Found: " + self.fileType)
        path = os.getcwd()+"/Sayles/"
        size = os.path.getsize(name)
        print("File size: ", size)
        print("Location offset: ")
        f.close()
    
    def createHash(self, data):
        # hasher = hashlib.md5()
        # with open('myfile.jpg', 'rb') as afile:
        #     buf = afile.read()
        #     hasher.update(buf)
        # print(hasher.hexdigest())
        md5_returned = hashlib.md5(data).hexdigest()
        print("MD%", md5_returned)
        f = open(path + "/Sayles/hashes.txt", "a")
        f.write(md5_returned + "\n")
        f.close


pdfStart = data.find(b'%PDF')
print(pdfStart)
if(pdfStart != -1):
    pdfEnd = data.find(b'EOF')
    # print("pdfEnd", pdfEnd)
    c = Carver("pdf", count)
    c.writeToFolder(data[pdfStart:pdfEnd])
    c.createHash(data[pdfStart:pdfEnd])
    count += 1



#loop till end of file




