
import os
from datetime import datetime, timedelta
import shutil


def get_old_dirs(dir_path, new_path, older_than):
    try:

        for path, folders, files in os.walk(dir_path):

            for file in files[:]:
                folder_path = os.path.join(path, file)
                print(folder_path)
                # print(os.path.getmtime(folder_path))
                file_datetime = datetime.fromtimestamp(os.path.getmtime(folder_path)).strftime('%Y-%m-%d %H:%M:%S')
                # print(file_datetime)
                # print(older_than)
                if file_datetime < older_than:
                    # print(folder_path)
                    new_folder_path = os.path.join(new_path, folder)
                    print(new_folder_path)
                    shutil.move(folder_path, new_folder_path)

            for folder in folders[:]:
                folder_path = os.path.join(path, folder)
                print(folder_path)
                get_old_dirs(folder_path, new_path, older_than)
    except Exception as error:
        print("error is % " % error)


if __name__ == '__main__':
    today = datetime.today()
    ten_days1 = today - timedelta(days=10)  # replace with your respective days
    ten_days = ten_days1.strftime('%Y-%m-%d %H:%M:%S')
    actual_path = 'C:\\actual'  # replace with actual path
    old_files_path = 'C:\\old'  # replace with path for old_files

    get_old_dirs(actual_path, old_files_path, ten_days)
