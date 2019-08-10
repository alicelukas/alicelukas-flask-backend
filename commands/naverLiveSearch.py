import urllib
from urllib.request import Request
import bs4
import datetime
from selenium import webdriver

def naverLiveSearch():
  url = "https://www.naver.com/"
  html = urllib.request.urlopen(url)

  bsObj = bs4.BeautifulSoup(html, "html.parser")
  realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
  realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
  realTimeSerach3 = realTimeSerach2.find_all('li')
  ret = []

  for i in range(0, 20):
    realTimeSerach4 = realTimeSerach3[i]
    realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})

    realTimeSerach = realTimeSerach5.text.replace(' ', '')
    realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach

    ret.append({
      'text': realTimeSerach,
      'link': realURL,
    })

  # return ret
  return json.dumps(ret)


def ffff():
  return '<h1>아..?</h1>'