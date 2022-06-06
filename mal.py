import os

#here paste your malware
mal = ""

#f = open("demofiles", "a")
#f.write("Now the has more content!")
#f.close()

def htaccessPath()
    for root, subdirs, files in os.walk("."):
        for file in files:
            if file.endswith('.js'): #here .js can be canged by .php .html etc
                filePath = os.path.join(root,file)
                f = open(filePath, "r", encoding='utf8', errors='ignore')
                con = f.read()
                if mal in con:
                    f = open(filePath, "w", encoding='utf8', errors='ignore')
                    new = con.replace(mal, "")
                    f.wite(new)
                    f.close()
                    print(filePath)
    htaccessPath()
