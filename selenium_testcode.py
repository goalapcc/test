from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome('C:/Users/ZestPC/Documents/chromedriver.exe')
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('http://co-anal.kma.go.kr/auth/login') #이상기후 합동분석시스템 로그인 URL로 이동하기

#---- 로그인 방법 1 ---------
driver.find_element_by_name('j_username').send_keys('climon@apcc21.org') # 값 입력
driver.find_element_by_name('j_password').send_keys('climon21@!')
driver.find_element_by_xpath("//button[@type='submit']").click()


#---- 로그인 방법 2 ---------
'''
inputElement = driver.find_element_by_id("j_username")
inputElement.send_keys("climon@apcc21.org")
inputElement = driver.find_element_by_id("j_password")
inputElement.send_keys("climon21@!")
inputElement.submit()
'''
#-------------------



driver.get('http://co-anal.kma.go.kr/cos/korea') # Naver 페이 들어가기
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

result_img = soup.select('div > a')
result_menu = soup.select('label > input')
#result_img = soup.select('div.p_inr > div.p_info > a > span')

for n in result_img:
    #fname = n.get('href')
    print(n)
   # print(fname)
