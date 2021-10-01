import os
import sys
import time
from mod.seleniumWeb import ServerWebDriver
from mod.log import LogFile
from mod.argv import argv
from mod.init import group_func_init

absdir = os.path.abspath(os.path.dirname(__file__))
logEeror = LogFile(printLog=1, file_log='error.txt')


def init():
    userPlatform = sys.platform
    if userPlatform != 'linux':
        raise NameError('platform not supported')
    operatingMod = argv()
    chromePathDir = group_func_init[userPlatform](operatingMod)
    print(chromePathDir)
    if chromePathDir:
        main(chromePathDir)
    else:
        logEeror('not file chrome')


def main(chromePathDir: str):
    driver = ServerWebDriver(chromePathDir)
    driver.run()
    html = driver.get('https://github.com/')

    with open(f'{absdir}/log/response.txt', 'w') as f:
        f.write(html)
    driver.send_keys(tupeElem='id', elem='user_email', inputStr='test@test.ru')
    driver.click(tupeElem='class', elem='width-sm-auto')


if __name__ == '__main__':
    init()
