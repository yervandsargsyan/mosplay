from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


def heal():
    driver.execute_script("showHPAlert();")


def snickers():
    driver.execute_script("cooldownReset('snikers');")


def tonus():
    driver.execute_script("cooldownReset('tonus');")
    heal()


def neftlenin_reset():
    driver.execute_script("NeftLenin.reset(2);")


def login(username, password):
    driver.get("http://www.moswar.ru/")
    uname = driver.find_element("id", "login-email")
    uname.send_keys(username)
    upass = driver.find_element("id", "login-password")
    upass.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[3]/div/table/tbody/tr/td/form/span').click()
    driver.execute_script("openChat();")
    if driver.current_url == "https://www.moswar.ru/player/#login":
        return True
    else:
        return False


def refresh():
    driver.refresh()


def metrofight():
    heal()
    driver.execute_script("elevatorToRatByHuntclubBadge();")
    time.sleep(1)
    driver.execute_script("metroTrackRat();")
    driver.execute_script("metroFightRat();")
    heal()


def worldtour2fight():
    driver.execute_script("Worldtour2.startFight();")
    refresh()


def worldtourfight(auto=""):
    driver.execute_script("Worldtour.startFight();")
    refresh()
    if auto:
        print("attacking boss")
    else:
        print("random attacking...")


def neftleninfight():
    heal()
    driver.execute_script("NeftLenin.viewPrize();")
    driver.execute_script("NeftLenin.attack();")
    driver.execute_script("NeftLenin.viewPreMission();")
    driver.execute_script("NeftLenin.viewPreMission2();")
    driver.execute_script("NeftLenin.skipMission();")
    driver.execute_script("NeftLenin.nextStep()")
    #driver.execute_script("NeftLenin.play();")


def bombing():
    driver.get("https://www.moswar.ru/arbat")
    time.sleep(1)
    driver.execute_script("buyPetrol(995684, this);")
    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    wait = WebDriverWait(driver, 10)
    try:
        driver.find_element(
            By.XPATH, '//*[@id="content"]/table[2]/tbody/tr/td[1]/div/div/div/form/table/tbody/tr/td[2]/button').click()

        driver.switch_to.default_content()
    except:
        driver.switch_to.default_content()
        time.sleep(30)
        bombing()


def pvp_fight_easy():
    checker = True
    driver.get("https://www.moswar.ru/alley")
    time.sleep(1)
    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchForm"]/div[1]')))
    try: driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]').click()
    except: snickers()
    time.sleep(2)
    try: driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]').click()
    except: checker = False
    if checker:
        driver.switch_to.default_content()
        time.sleep(5)
        iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]').click()
        driver.switch_to.default_content()


def pvp_fight_normal():
    driver.get("https://www.moswar.ru/alley/search/type")
    time.sleep(2)
    # driver.execute_script("iframeInit;")
    # iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    # driver.switch_to.frame(iframe)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]').click()
    # driver.switch_to.default_content()
    try:
        driver.execute_script("iframeInit;")
        iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
        driver.switch_to.frame(iframe)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]').click()
        driver.switch_to.default_content()
        time.sleep(2)
        if "fight" in driver.current_url:
            snickers()
    except: pass

def pvp_fight_hard():
    driver.get("https://www.moswar.ru/alley")
    snickers()
    driver.execute_script("iframeInit;")
    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[3]').click()
    driver.switch_to.default_content()

    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]').click()
    driver.switch_to.default_content()


def make_petrics(petrics_ammo):
    driver.get("https://www.moswar.ru/factory")
    time.sleep(3)
    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    petrics_button = driver.find_element(By.XPATH, '//*[@id="content"]/table[2]/tbody/tr[1]/td/div/div/form/p[2]/button')
    for i in range(petrics_ammo):
        petrics_button.click()
    driver.switch_to.default_content()


def get_person_info():
    def map_hp(hp_str):
        def human_format(num, round_to=2):
            magnitude = 0
            while abs(num) >= 1000:
                magnitude += 1
                num = round(num / 1000.0, round_to)
            return '{:.{}f}{}'.format(num, round_to, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])
        hp_str = hp_str[7:]
        curr_hp, max_hp = hp_str.split("/")
        curr_hp = int(curr_hp)
        max_hp = int(max_hp)
        return "Жизни: "+str(human_format(curr_hp)) + "/" + str(human_format(max_hp))

    user_information = []
    iframe = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    person_div_element = driver.find_element(By.XPATH, '//*[@id="personal"]')
    pers_information =(person_div_element.text.split("\n"))
    print(pers_information[0])
    user_information.append(pers_information[0])
    user_information.append(map_hp(pers_information[1]))
    user_information.append(pers_information[2])
    user_information.append("Тугрики: "+pers_information[6])
    user_information.append("Руда: " + pers_information[7])
    user_information.append("Нефть: " + pers_information[8])
    user_information.append("Мёд: " + pers_information[9])
    user_information.append(pers_information[10])
    driver.switch_to.default_content()
    return user_information


def moscowpoly_game(game_ammo):
    pass


def auto_travels():
    pass


def buy_red_gloves():
    pass


def buy_black_gloves():
    pass


def buy_respirator():
    pass


def buy_gasmask():
    pass


