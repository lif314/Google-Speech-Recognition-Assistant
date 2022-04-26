import json
from urllib.request import urlopen
"""
网易云API接口文档：https://neteasecloudmusicapi.vercel.app/#/?id=neteasecloudmusicapi
baseUrl: https://music-1247192-1307429763.ap-shanghai.run.tcloudbase.com/
"""


class NeteaseCloudMusicApi:
    def __init__(self):
        self.baseUrl = "https://music-1247192-1307429763.ap-shanghai.run.tcloudbase.com"
        # 推荐新音乐的前10首歌曲
        self.ten_song_ids = []
        #歌曲的url. id:url
        self.ten_song_urls = []
        # 歌曲的详细信息 id:name
        self.ten_song_name = []
        #
        self.id_name_url = []


    """
    功能：获取推荐新音乐【不需要登录的】
    可选参数 : limit: 取出数量 , 默认为 10 (不支持 offset)
    接口地址 : /personalized/newsong
    调用例子 : /personalized/newsong
    """
    def get_10_newsongs(self):
        r = urlopen(self.baseUrl + "/personalized/newsong")
        bytes_data = r.read()
        str_data = str(bytes_data,'utf-8')
        json_data = json.loads(str_data)
        list_data = json_data.get('result')
        for song in list_data:
            self.ten_song_ids.append(song.get("id"))
        # print(self.ten_song_ids)

    """
    功能：获取歌曲详情
    必选参数 : ids: 音乐 id, 如 ids=347230
    接口地址 : /song/detail
    调用例子 : /song/detail?ids=347230,/song/detail?ids=347230,347231
    """
    def get_song_details(self):
        list_string = map(str, self.ten_song_ids)
        ids = ','.join(list_string)
        r = urlopen(self.baseUrl + "/song/detail?ids=" + ids)
        bytes_data = r.read()
        str_data = str(bytes_data, 'utf-8')
        json_data = json.loads(str_data)
        list_data = json_data.get('songs')
        for song in list_data:
            self.ten_song_name.append({"id": song.get("id"), "name": song.get("name")})
        # print(self.ten_song_name)


    """
    功能：使用歌单详情接口后 , 能得到的音乐的 id, 但不能得到的音乐 url, 调用此接口, 传入的音乐 id( 可多个 , 用逗号隔开 ), 
        可以获取对应的音乐的 url,未登录状态或者非会员返回试听片段(返回字段包含被截取的正常歌曲的开始时间和结束时间)
    必选参数 : id : 音乐 id
    可选参数 : br: 码率,默认设置了 999000 即最大码率,如果要 320k 则可设置为 320000,其他类推
    接口地址 : /song/url
    调用例子 : /song/url?id=33894312 /song/url?id=405998841,33894312
    """
    def get_song_url(self):
        # int list to string: map
        list_string = map(str, self.ten_song_ids)
        ids = ','.join(list_string)
        r = urlopen(self.baseUrl + "/song/url?id=" + ids)
        bytes_data = r.read()
        str_data = str(bytes_data, 'utf-8')
        json_data = json.loads(str_data)
        list_data = json_data.get("data")
        for song in list_data:
            self.ten_song_urls.append({"id":song.get("id"), "url" : song.get('url')})
        # print(json_data)

    # 获取歌曲详情  id name url
    def get_new_songs_details(self):
        # 初始化对象时即获取最新推荐的音乐的id集合
        self.get_10_newsongs()
        # 根据id集合查询到歌曲的url
        self.get_song_url()
        # 根据id集合查询到歌曲的name
        self.get_song_details()
        #合并name和url
        for i in range(len(self.ten_song_name)):
            for a in self.ten_song_urls:
                if self.ten_song_name[i]['id'] == a['id']:
                    self.id_name_url.append({"id": a['id'], "name": self.ten_song_name[i]['name'], "url": a['url']})
        # {'id': 1939928579, 'name': '好好说话', 'url': 'http://m801.music.126.net/20220427014515/c4b89b5b383ab1cf4e38e7364c46fd29/jdymusi
        return self.id_name_url

if __name__ == '__main__':
    musicApi = NeteaseCloudMusicApi()
    # musicApi.get_song_url()
    # musicApi.get_10_newsongs()
    #musicApi.get_song_details()
    songs = musicApi.get_new_songs_details()
    print(songs)