import os

pathArr = []

def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        if os.path.isdir(path):
            print_files_in_dir(path, prefix)
        else:
            if path.find('.png') == -1 and path.find('.pcm') == -1 and path.find('.gif') == -1 and path.find('.jpg') == -1:
                pathArr.append(prefix+path)

def findData(filePath):
    id = []
    func = []

    print(filePath)
    f = open(filePath,"r", encoding='utf-8');

    lines = f.readlines()
    for line in lines:
        if(line.find("id:") != -1 or line.find("id :") != -1):
            str = ""
            str = line.split(":")
            data = str[1].strip()
            id.append(data)

        if(line.find("function") != -1):
            str = ""
            str = line.replace("function","")
            str = str.strip()
            str = str.split("(")
            func.append(str[0])
    f.close()

    for idName in id:
        for funcName in func:
            if idName == funcName:
                print("*********")
                print(filePath)
                print(idName)

if __name__ == "__main__":
    root_dir = "Y:\qml-webos-framework\sysbus"
    print_files_in_dir(root_dir, "")

    for path in pathArr:
        findData(path)
