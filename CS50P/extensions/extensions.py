types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}
s = input("File name: ")
if(s.find('.') == -1):
    print("application/octet-stream")
    exit()
s = s.strip()
s2 = s.split('.')[-1]
s2 = s2.lower()
if(types.get(s2) != None):print(types[s2])
else:print("application/octet-stream")