from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# change 'ip:port' with your proxy's ip and port
proxy_ip_port = '103.52.171.165:8080'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# replace "" with your chrome binary absolute path
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", desired_capabilities=capabilities)

driver.get('http://whatismyipaddress.com')

time.sleep(8)

driver.quit()
