import requests
from bs4 import BeautifulSoup

def melon_chart(rank):
    # 멜론 차트 URL
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 노래 정보 추출
    songs = soup.select('#lst50')  # 상위 50곡 정보를 가지는 태그 선택
    song_dict = {}

    # 각 곡의 정보 추출
    for i, song in enumerate(songs):
        title = song.select('div.ellipsis.rank01 > span > a')[0].text
        artist = song.select('div.ellipsis.rank02 > a')[0].text
        song_dict[i + 1] = {'title': title, 'artist': artist}

    # # 결과 출력
    # for rank, info in song_dict.items():
    #     print(f"{rank}위: {info['title']} - {info['artist']}")
    return song_dict[rank]
