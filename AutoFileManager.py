import os
import shutil

data = {"img" : [".png", ".jpeg", ".jpg",".webp"], 
    "doc": [".doc", ".docx", ".pdf"],
    "setup":[".exe",".msi"],
    "Webpages": [".html"],
    "Videos" : [".mp4"],
    "Prensentation": [".ppt", ".pptx"],
    "Excel sheet" : [".xlsx"],
    "Music" : [".mp3", ".wav"],
    "Zip" : [".zip"],
    "Torrent" : [".torrent"]
    }    


os.chdir(r'C:\Users\abhie\Downloads')
cwd = os.chdir(r'C:\Users\abhie\Downloads')


for f in os.listdir(cwd):

    f_name, f_ext = os.path.splitext(f)

    for key, value in data.items():
        d = key
        if f_ext in value or f_ext.upper() in value:
            if key not in os.listdir():
                os.mkdir(d)
                shutil.move(f, d)
            else:
                shutil.move(f, d)            

        
