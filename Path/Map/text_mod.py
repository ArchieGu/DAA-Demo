import os
fileDir = '/Users/tianyuli/Documents/BUAA/创新港工作/china/'
replace_list1 = [      
                    [","," "],
                    [";"," "],
                    [" ",""]
                ]
def listFiles(dirPath):
    fileList=[]
    for root,dirs,files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root,fileObj).replace("\\","/"))
    return fileList

def replace_content():
    fileList = listFiles(fileDir)
    for fileObj in fileList:
        if fileObj[-4:] == '.txt':
            print('1')
            f = open(fileObj,mode='r+',newline='')#newline=''表示不更改换行符
            all_the_lines=f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                newline=line
                for rp in range(len(replace_list1)):
                    newline=newline.replace(replace_list1[rp][0], replace_list1[rp][1])
                f.write(newline)
            f.close()

if __name__=='__main__':
    replace_content()