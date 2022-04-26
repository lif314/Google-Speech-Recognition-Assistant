import urllib.request
"""
网易云API接口文档：https://neteasecloudmusicapi.vercel.app/#/?id=neteasecloudmusicapi
baseUrl: https://music-1247192-1307429763.ap-shanghai.run.tcloudbase.com/
"""

r = urllib.request.urlopen('https://music-1247192-1307429763.ap-shanghai.run.tcloudbase.com/song/url?id=405998841,33894312')
print(r.read())