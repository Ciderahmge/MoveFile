from datetime import datetime
import shutil
import glob
import os
from os import rename


filename = '0000_Summary.html' # 가져올 파일명
mfoldername = "C:\\wwwroot\\summary"
# print(mfoldername)
if os.path.isdir(mfoldername):
    shutil.rmtree(mfoldername)
    os.mkdir(mfoldername)
else :
    os.mkdir(mfoldername)

path = "c:\\Users\\kms\\Documents\\CoolCheck Reports\\" # 초기 경로
path1 = glob.glob(path + '\*') # 위 경로의 리스트 경로를 불러옴.

for i in range(0, len(path1)):
    if path1[i].endswith('.html'): # StartSummary.html 제외
        continue
    else :   
        # ext = os.path.splitext(path1[i])[-1].lower()
        path2 = path1[i] + "\\"
        temp1 = filter(os.path.isdir, glob.glob(path2)) # 모든 보고서의 폴더 필터링
        # print(temp1)
        latest_folder = max(temp1, key=os.path.getctime) + "\\" # 최근 폴더 가져옴.
        file =  latest_folder + filename # summary.html 경로 생성
        # print(file)

        
        cfilename = os.listdir(path) # 파일명 변경 변수
        shutil.copy(file, mfoldername)
        rename(mfoldername + "\\" + filename, mfoldername + "\\" + cfilename[i] + ".html")
            


    
    

    

