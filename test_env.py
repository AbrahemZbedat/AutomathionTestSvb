import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://svburger1.co.il')







driver.delete_all_cookies()
# פרטי המשתמש לשימוש חוזר
first_name = "Abrahem"
last_name = "Zbedat"
generated_email = ""
import random
def generate_random_email():
    return f"abrahem{random.randint(1000, 9999)}@gmail.com"
password = "123456"
wrong_password = "1XXXXXX2387456"







def try_wrong_data():
    try:
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        assert True, f"הופיעה הודעת שגיאה כצפוי: {alert_text}"

    except NoAlertPresentException:
        # נבדוק אם יש טקסט שגיאה בגוף העמוד
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if any(word in body_text for word in ["שגיאה", "must", "Error", "Failed"]):
            assert True, f"הופיעה הודעת שגיאה בדף כצפוי: {body_text}"
        else:
            assert False, "❌ לא הופיעה שום הודעת שגיאה למרות שהוזנו נתונים שגויים"


def try_correct_data():
    try:
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        assert False, f"הופיעה הודעת שגיאה כלא כצפוי: {alert_text}"

    except NoAlertPresentException:
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if any(word in body_text for word in ["שגיאה", "must", "Error", "Failed"]):
            assert False, f"הופיעה הודעת שגיאה כלא כצפוי בגוף הדף: {body_text}"
        elif "TensorFlow Lite" in body_text:
            print("⚠️ התעלמות משגיאת TensorFlow לא קריטית")
        else:
            pass



# פונקציית הרשמה עם פרטים תקינים
def signUp_with_correct_data():
    global generated_email
    generated_email = generate_random_email()  # יצירת אימייל חדש

    driver.get('https://svburger1.co.il/#/HomePage')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[1]").send_keys(first_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[2]").send_keys(last_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[3]").send_keys(generated_email)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[4]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[5]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/button").click()






# פונקציית הרשמה עם סיסמה לא תואמת
def signUp_with_wrong_data():
    email = generate_random_email()  # יצירת אימייל חדש
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[1]").send_keys(first_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[2]").send_keys(last_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[3]").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[4]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[5]").send_keys(wrong_password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/button").click()





def signIn_correctData():
        time.sleep(2)
        driver.get('https://svburger1.co.il/#/HomePage')

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/a[1]/button").click()
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[1]").send_keys(generated_email)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[2]").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/button").click()
        time.sleep(3)





def signIn_wrongData():
     email = generate_random_email()  # יצירת אימייל חדש

     driver.get('https://svburger1.co.il/#/HomePage')
     driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
     driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[1]").send_keys(email)
     driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/input[2]").send_keys("12ds")
     driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/form/div/button").click()




# בדיקת הרשמה תקינה
def test_signUp_with_correct_data():
    signUp_with_correct_data()
    #signIn_wrongData()
    time.sleep(3)
    try_correct_data()





def test_signUp_with_wrong_data():
    signUp_with_wrong_data()
    #signUp_with_correct_data()
    time.sleep(4)
    try_wrong_data()





# בדיקת התחברות עם פרטי הרשמה תקינים
def test_signInWithCorrectData():
    signUp_with_correct_data()
    signIn_correctData()
    #signIn_wrongData()
    time.sleep(3)
    try_correct_data()




def test_signInWithWrongData():
    signUp_with_correct_data()
    #signIn_correctData()
    signIn_wrongData()
    time.sleep(3)
    try_wrong_data()





def test_weather_correct_data():
    driver.get('https://svburger1.co.il/#/HomePage')

    driver.find_element(By.ID, "location-name").clear()
    driver.find_element(By.ID, "location-name").send_keys("Tel aviv")

    # המתן עד שהכפתור יהיה נוכח ב-DOM
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Search']"))
    )

    # בצע את הלחיצה באמצעות JavaScript
    driver.execute_script("arguments[0].click();", search_button)

    try_correct_data()



#fialed
def test_weather_wrong_data():
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.find_element(By.ID, "location-name").clear()
    driver.find_element(By.ID, "location-name").send_keys("111")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(6)
    try_wrong_data()




def test_signUp_with_empty_fields():
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    # מנסה לשלוח את הטופס בלי למלא כלום
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/button").click()
    time.sleep(6)

    # בודק שנשארנו באותו דף => סימן שלא התקבלה ההרשמה
    current_url = driver.current_url
    assert "#/SignUp" in current_url or "Sign Up" in driver.page_source, "❌ הטופס נשלח למרות ששדות ריקים"





def test_signUp_duplicate_email():
    #email = generate_random_email()  # יצירת אימייל חדש
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.implicitly_wait(10)
    # הרשמה ראשונה
    signUp_with_correct_data()
    time.sleep(6)
    # ניסיון הרשמה שוב עם אותו מייל
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[1]").send_keys(first_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[2]").send_keys(last_name)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[3]").send_keys(generated_email)  # אותו מייל
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[4]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/input[5]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/form/button").click()
    time.sleep(5)
    try_wrong_data()



def test_access_protected_page_without_login():
    driver.delete_all_cookies()  # לוודא שאין התחברות קיימת
    driver.get('https://svburger1.co.il/#/')

    time.sleep(7)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert any(word in body_text for word in ["Sign In", "התחברות", "Login"]), "I can get login without password!!!"

