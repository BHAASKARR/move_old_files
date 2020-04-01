# importing libraries
import os
from datetime import datetime, timedelta
import shutil


def get_old_dirs(dir_path, new_path, specific_projects, older_than):
    try:

        for path, folders, files in os.walk(dir_path):

            for file in files[:]:
                folder_path = os.path.join(path, file)
                print("file folder_path:%s" % folder_path)
                # print(os.path.getmtime(folder_path))
                file_datetime = datetime.fromtimestamp(os.path.getmtime(folder_path)).strftime('%Y-%m-%d %H:%M:%S')
                print("file_datetime %s" % file_datetime)
                print("older_than %s" % older_than)
                if file_datetime < older_than:
                    # print(folder_path)
                    new_folder_path = os.path.join(new_path, folder)
                    print(new_folder_path)
                    shutil.move(folder_path, new_folder_path)

            for folder in folders[:]:
                if folder not in specific_projects:
                    print("not required folders:%s" % folder)
                    pass
                folder_path = os.path.join(path, folder)
                print(" inside folder folder_path %s" % folder_path)
                get_old_dirs(folder_path, new_path, older_than)
    except Exception as error:
        print("error is % " % error)


if __name__ == '__main__':
    today = datetime.today()
    print("todays date %s" % today)
    ten_days1 = today - timedelta(days=10)  # replace with your respective days
    ten_days = ten_days1.strftime('%Y-%m-%d %H:%M:%S')
    print(ten_days)  # 2020-03-21 19:45:22
    actual_path = 'C:\\actual'  # replace with actual path
    old_files_path = 'C:\\old'  # replace with path for old_files
    specific_folders = ['ccr_build', 'bbr_buiild','abcd']
    
    get_old_dirs(actual_path, old_files_path, specific_folders, ten_days)
