import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/i7-13620H-Processor-GeForce-Display-ANV15-51-73B9/dp/B0CMRGBXM9/ref=sr_1_3?crid=19MFQC247HA1U&dib=eyJ2IjoiMSJ9.fLF2sR163LlECSdhFtVERwqTXHt0jx2QzERR3WK-B-qR-WhZ57uLFF2vwKS2z560lTFQjk10nEq7rIdNOfWtB-EydHgjBFbxOKBsAUm07EGPSqX_e5p1fIXKPEhfjYUeO5H_kVUoc3grjBYE5pJ4cZfaxa7baYU_crO9GXlPQNxlOvw54pvmEWCpLr_qDjCKLDGjqVoDSOFpuhOpY9xBSVILPF1Yr05tBn3F_KRJZjk.H1mNVEq8XrxfrwkSyXfM4iWGjs8lYqHgSGG1VsooWlg&dib_tag=se&keywords=gaming%2Blaptop&qid=1737870784&sprefix=gaming%2Blaptip%2Caps%2C163&sr=8-3&th=1'

page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")


title_text = soup.find('span', id='productTitle').text.strip()

if title_text:
  title = f'{title_text}'
else: print('We could not find this element') 


price_whole = soup.find('span', class_='a-price-whole').text.strip()
price_fraction = soup.find('span', class_='a-price-fraction').text.strip()

if price_whole and price_fraction:
  price = f'{price_whole}{price_fraction}'
else: print('We could not find this element')


print(f'Title: {title} \n\n')
print(f'Price: ${price}')