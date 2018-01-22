'''
네이버에서 제공하는 영화 정보 페이지에서
현재 상영영화 중 예매순으로 정렬된 정보를 출력하는 프로그램
'''
from bs4 import BeautifulSoup
import requests

cnt = 1

url = requests.get('http://movie.naver.com/movie/running/current.nhn').text
soup = BeautifulSoup(url, "html.parser")

for classData in soup.find_all(class_="tit"):
    print(str(cnt) + "위 : " + classData.a.string)
    cnt+=1

