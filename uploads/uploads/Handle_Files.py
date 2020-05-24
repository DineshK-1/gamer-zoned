import os
os.chdir("uploads")
os.chdir("uploads")

def Handle_Uploads(Dict):
    for Key in Dict:
        name = Dict[Key].name
        data = Dict[Key].read()
        f = open(name,"wb+")
        f.write(data)
        f.close()
        