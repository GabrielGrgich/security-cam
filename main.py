
#import time
#import dropbox
#import random
#import cv2

start_Time=time.time()

def snapshot():
    number=random.randint(0,100)#create random numbers for number of pictures
    vCap=cv2.VideoCapture(0)#video capture object
    result=True
    while(result):
        ret,frame=vCap.read()
        imageName="img"+str(number)+".png"#naming the picture by number image
        cv2.imwrite(imageName,frame)
        start_Time=time.time()
        result=False
    return imageName#return gives a value back to user
    print("snapshot taken")
    vCap.release()
    cv2.destroyAllWindows()

snapshot()

def uploadFile(imageName):
    accessToken='sl.BK1ENyADCfHrtW5Htrw7LQ2kHsdNm-D44ncPkGMIEaYk7CjwNlIhlEbD2mwxFtEHf_jW_O94Hv-iRGHFq4xmfpkgQwHgv487F5_2PddNqSHIHWlttlMGqgDosaWF0qqNgj6XrIAmPDM'
    file=imageName
    fileFrom=file
    fileTo="/newfolder1/"+(imageName)
    dbx=dropbox.Dropbox(accessToken)
    with open(fileFrom,"rb")as f:#read binary or rb
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)#
        print("files have been saved to cloud")

def main():
    while(True):
        if((time.time()-start_Time)>=5):
            name=snapshot()
            uploadFile(name)

main()