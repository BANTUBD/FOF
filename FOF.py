import os, platform, time, sys
os.system('git pull')
print('[\033[1;32m✓\033[1;37m] Collecting Modules Please Wait ! ')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
import fof
