import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define a dictionary to map English currency codes to Chinese currency names
currency_mapping = {
    "USD": "美元",
    "EUR": "欧元",
    "HKD": "港币",
    "MOP": "澳门元",
    "JPY": "日元",
    "THP": "泰国铢",
    "SGD": "新加坡元",
    "PHP": "菲律宾比索",
    "CHF": "瑞士法郎",
    "GBP": "英镑",
    "SUR": "卢布",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "NZD": "新西兰元",
}

def fetch_forex_rate(date, currency_code):
	try:
	    # 打开中国银行外汇牌价网站
		driver.get("https://www.boc.cn/sourcedb/whpj/")

		# 等待页面加载
		time.sleep(2)
	    
	    # 输入日期
		date_input = driver.find_element(By.XPATH, "//tr/td/div/input[@name='erectDate']")
		#date_input.clear()
		date_input.send_keys(date)
	    
		date_input2 = driver.find_element(By.XPATH, "//tr/td/div/input[@name='nothing']")
		#date_input2.clear()
		date_input2.send_keys(date)

	    # 输入货币代码
	    # 转换成中文
		currency_name = currency_mapping.get(currency_code, "")
		options = driver.find_elements(By.XPATH, "//tr/td/select/option")
		for option in options:
			if currency_name in option.text:
				option.click()
				break
		

		# Choose currency
		#selection = driver.find_element(By.XPATH, "//tr/td/select/option[contains(text(), '"+currency_name+"')]")
		
		button = driver.find_element(By.XPATH, "//td/input[@class='search_btn']")
		button.click()
	    
	    # 等待页面加载
		time.sleep(2)
	   
	    # 获取现汇卖出价
		forex_rate_ele = driver.find_element(By.XPATH, "//tr[@class='odd']/td[4]")
		forex_rate = forex_rate_ele.text
	    
	    # 写入result.txt文件
		with open("result.txt", "w") as f:
			f.write(f"Forex Rate: {forex_rate}")
	    
		print(forex_rate)
	        
	except NoSuchElementException:
		print("Element not found. Please check your input.")
        
	finally:
    	# 关闭浏览器
		driver.quit()		

if __name__ == "__main__":
	if len(sys.argv) != 3:
	    print("Usage: python3 yourcode.py <date> <currency_code>")
	    sys.exit(1)
	    
	date = sys.argv[1]
	currency_code = sys.argv[2]
	fetch_forex_rate(date, currency_code)