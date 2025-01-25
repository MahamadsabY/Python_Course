import shutil
import os
import datetime

def backup_files(source, destination):
    today_date = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today_date}")
    shutil.make_archive(backup_files_name,'gztar',source)

source = "/Users/mahamad y/Desktop/Python_for_DevOps/Chapter_14-TWS" 
destination = "/Users/mahamad y/Desktop/Python_for_DevOps\Chapter_14-TWS/backup"   

backup_files(source,destination)