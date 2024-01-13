try:
        
    import glob
    import os
    import shutil
    import datetime
    import time
    from tqdm import tqdm

    #日付操作



    nowtime = datetime.datetime.now()

    FolderTime = nowtime.strftime("%m%d")

    os.mkdir(r"C:\Users\910143\Desktop\PythonF\\履歴" + "\\" + FolderTime)

    py = glob.glob(r"C:\Users\910143\Desktop\PythonF\*.py*")

    for p in py:
        print(p)
        shutil.copy(p,r"C:\Users\910143\Desktop\PythonF\履歴" + "\\" + FolderTime)
except Exception as e:
    input(e)
