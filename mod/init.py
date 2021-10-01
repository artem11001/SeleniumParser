"""
    Установка хрома на сервер, пока что только под linux
"""


def linuxInit(operatingMod):
    import os
    import subprocess
    from mod.log import LogFile
    from mod.loadChrom import chromeVersionStart

    absdir = os.path.abspath(os.path.dirname(__file__))
    logEeror = LogFile(printLog=1, file_log='error.txt')

    loadOk = f'{absdir}/log/installOk.txt'

    if operatingMod == 'server' and not os.path.isfile(loadOk):
        print('init')
        dirLogFile = f'{absdir}/log/install.txt'  # файл логов загрузки
        """установка хрома и зависимостей на сервер"""
        try:
            f = open(dirLogFile, 'a')
            subprocess.check_output(
                r'sudo pip install selenium',
                stderr=f,
                shell=True)
            subprocess.check_output(
                r'sudo apt install -y libxss1 libappindicator1\
                    libindicator7',
                stderr=f,
                shell=True)
            subprocess.check_output(
                r'sudo https://dl.google.com/linux/direct/\
                    google-chrome-stable_current_amd64.deb',
                stderr=f,
                shell=True)
            subprocess.check_output(
                r'sudo dpkg -i google-chrome*.deb',
                stderr=f,
                shell=True)
            subprocess.check_output(
                r'sudo apt install -y -f',
                stderr=f,
                shell=True)
        except Exception as e:
            logEeror(e)
        else:
            open(loadOk, 'w').write('install server ok')
        finally:
            f.close()
    chromePathDir = chromeVersionStart('linux')  # путь до драйвера
    return chromePathDir


def win():
    raise NameError('platform not supported')


group_func_init = {
    'linux': linuxInit,
    'win': win
}
