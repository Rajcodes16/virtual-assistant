from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def ChromeAuto():
    chrome_options=Options()

    driver=webdriver.Chrome(executable_path='', options=chrome_options)
    driver.get('https://www.google.com')

    search_input=driver.find_element_by_name('q')
    search_input.send_keys('python automation')

    search_input.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    search_results= driver.find_element_by_css_seletors('div.gh3')

    for result in search_results:
        print(result.text)

    driver.quit()

if 'minimise this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')
elif 'open history' in query:
                pyautogui.hotkey('ctrl', 'h')
elif 'open downloads' in query:
                pyautogui.hotkey('ctrl', 'j')
elif 'previous tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')