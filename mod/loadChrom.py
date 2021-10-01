"""
    Скачивает модуль хром под операционную систему и версию хрома
    Протестировано только под linux
"""
from mod import requ
import subprocess
import re
import os


absdir = os.path.abspath(os.path.dirname(__file__))      # путь до скрипта
pathcd = str(os.path.split(absdir)[0])                   # путь на каталог выше
dirchrome = os.path.join(pathcd, 'chrome')               # путь дрейвера


def loadChrome(versionchromeNum: str, zipName: str, pathName: str) -> any:
    """
    Скачивает драйвер хрома и возвращает путь до драйвера
    """
    dirPathName = f'{dirchrome}/{pathName}'                # путь до драйвера
    dirZipName = f'{dirchrome}/{zipName}'                  # путь до архива
    print(dirPathName)
    if os.path.isfile(dirPathName):
        return dirPathName
    googlurl = "https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=%s" % versionchromeNum
    r = requ.get(url=googlurl)
    version = re.findall(r'<Prefix>(.*?)/', r, re.DOTALL)[1]
    googlurlLoad = f'https://chromedriver.storage.googleapis.com/{version}/{zipName}'
    data = requ.post(url=googlurlLoad)
    open(f'{dirZipName}', 'wb').write(data)
    subprocess.check_output(
            f'unzip \'{dirZipName}\' -d \'{dirchrome}\'',  # распаковка архива
            shell=True
    )
    if not os.path.isfile(dirPathName):
        return 0
    return dirPathName


def chromeVersionStart(platform: str = 'linux') -> str:
    """
    Получает версию хрома с учетом операционной системы
    """
    if platform == 'linux':
        zipName = 'chromedriver_linux64.zip'
        pathName = 'chromedriver'
        output = subprocess.check_output(
            r'google-chrome --version',
            shell=True
        )
        versionchrome = (output.decode('utf-8').strip()).split(' ')[-1]
    elif platform == 'win':
        zipName = 'chromedriver_win32.zip'
    versionchromeNum = versionchrome.split('.')[0]
    return loadChrome(versionchromeNum, zipName, pathName)


if __name__ == '__main__':
    chromeVersionStart()
