"""
Обертка над сенениумом
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from mod import option


class WebDriver():
    def __init__(self,
                 chromePathDir: str,
                 userAget: str = option.defaultUserAgent) -> None:
        self.chromePathDir = chromePathDir
        self.userAget = userAget
        self.optionsDirv = webdriver.ChromeOptions()

    def option(self, args):
        """добавление опций"""
        for opt in args:
            print(opt)
            self.optionsDirv.add_argument(opt)

    def run(self):
        """инициализация драйвера"""
        self.ojbdirver = webdriver.Chrome(chrome_options=self.optionsDirv,
                                          executable_path=self.chromePathDir)

    def get(self, getUrl: str):
        """открытие ссылки и возвращение ответа"""
        self.ojbdirver.set_page_load_timeout(option.max_load_timeout)
        self.ojbdirver.implicitly_wait(option.i_wait)
        try:
            self.ojbdirver.get(getUrl)
        except TimeoutException:
            return self.TimeoutExceptionErr()
        else:
            return self.ojbdirver.page_source

    def isElemenId(self, elem: str) -> int:
        """проверка на наличие элемена"""
        length = self.ojbdirver.find_elements_by_id(elem)
        if length:
            return length
        else:
            return 0

    def isElemenClass(self, elem: str) -> int:
        """проверка на наличие элемена"""
        length = self.ojbdirver.find_elements_by_class_name(elem)
        if length:
            return length
        else:
            return 0

    def listClass(self, elem: str) -> any:
        """возвращает массив элементов, 0 если нет"""
        if not self.isElemenClass(elem):
            return 0
        else:
            self.ojbdirver.find_elements_by_class_name(elem)

    def listid(self, elem: str) -> any:
        """возвращает массив элементов, 0 если нет"""
        if not self.isElemenId(elem):
            return 0
        else:
            self.ojbdirver.find_elements_by_id(elem)

    def addProxy(self, proxy: str) -> None:
        """смена ip"""
        self.option(proxy)

    def AddUserAget(self, AddUserAget: str) -> None:
        """смена юзер агента"""
        self.option(AddUserAget)

    def TimeoutExceptionErr(self) -> str:
        """обработка ошибок времяни загрузки страницы"""
        return 'TimeoutException'

    def click(self, tupeElem: str, elem: str, id: int = 0) -> int:
        """кликает на элементы, возвращает 0 если элемента нет"""
        if tupeElem == 'class':
            if not self.isElemenClass(elem):
                return 0
            self.ojbdirver.find_elements_by_class_name(elem)[id].click()
            self.ojbdirver.implicitly_wait(option.i_wait)
            return 1
        elif tupeElem == 'id':
            if not self.isElemenId(elem):
                return 0
            self.ojbdirver.find_elements_by_id(elem)[id].click()
            self.ojbdirver.implicitly_wait(option.i_wait)
            return 1

    def send_keys(self, tupeElem: str, elem: str, inputStr: str):
        if tupeElem == 'class':
            if not self.isElemenClass(elem):
                return 0
            self.ojbdirver.find_elements_by_class_name(elem)[0].clear()
            self.ojbdirver.find_elements_by_class_name(elem)[0].send_keys(
                inputStr)
            self.ojbdirver.implicitly_wait(option.i_wait)
            return 1
        elif tupeElem == 'id':
            if not self.isElemenId(elem):
                return 0
            self.ojbdirver.find_elements_by_id(elem)[0].clear()
            self.ojbdirver.find_elements_by_id(elem)[0].send_keys(inputStr)
            self.ojbdirver.implicitly_wait(option.i_wait)
            return 1

    def close(self):
        self.ojbdirver.close()
        self.ojbdirver.quit()


class ServerWebDriver(WebDriver):
    """Добавляет настройки для сервера"""
    def __init__(self, chromePathDir: str,
                 userAget: str = option.defaultUserAgent) -> None:
        super().__init__(chromePathDir, userAget=userAget)
        self.option(option.defaultOptServer)
