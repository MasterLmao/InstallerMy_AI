import requests # pip install requests
import wget,gdown # pip install wget, pip install gdown

class GoogleDriveDownload(object):
    def __init__(self) -> None:
        pass
        
    def DownloadFolder(url, dir_path):
        
        print("Check Internet Connect...")
        
        try:
            print("Start download File....")
        except Exception as e:
            if ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
                print("Please check your internet connect to device...")
                print(e)
                return None
        
        try:
            with requests.get(url) as req:
                if url.split('/')[-1] == '?usp=sharing':
                    url= url.replace('?usp=sharing','')
                    gdown.download_folder(url, output=dir_path)
                print("Folder downloaded")
        except Exception as e:
            
            print(e)
            return None
          
        
    def DownloadFile(url, dir_path):
        print("Check Internet Connect...")
        try:
            print("Start download File....")
            
        except Exception as e:
            if ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
                # print(ConnectionError)
                print("Please check your internet connect to device...")
                print(e)
                return None
        
        try:
                # url = sys.argv[1]
                file_id = url.split('/')[-2]
                # print(file_id)
                prefix = f'https://drive.google.com/uc?/export=download&id={file_id}'
                wget.download(prefix,out=dir_path)
                print(" File downloaded")
        except Exception as e:
            print(e)
            return None
        

