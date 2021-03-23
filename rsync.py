import os.path
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
save_path = '/Users/T3ddezz/Desktop/Save_file/'
folder_name = os.path.basename(os.path.normpath(f'{save_path}'))
neuer_ordner_name = date + '_' + folder_name
os.system(f'rsync --remove-source-files -avz --include "*.txt" {save_path} ~/Desktop/test_server/{neuer_ordner_name}')
os.system(f'find  {save_path}. -type d -empty -delete')
#os.system(f'rmdir {save_path}')
