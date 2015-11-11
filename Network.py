import urllib.parse as urlparse
import urllib.request as urllib
import xml.dom.minidom as xmlminidom


class NetWork(object):
    def __init__(self):
        self.url_base = 'http://box.zhangmen.baidu.com/x?'
        self.value = {'op': '12', 'count': '1'}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'}

    def get_music_play_url(self, music_name):
        self.value['title'] = music_name + '$$'
        self.data = urlparse.urlencode(self.value)
        self.url_full = self.url_base + self.data
        self.request = urllib.Request(self.url_full, headers=self.headers)
        self.xml_content = urllib.urlopen(self.request).read().decode('utf-8')
        self.doc = xmlminidom.parseString(self.xml_content)
        self.music_head = self.doc.getElementsByTagName('encode')[0].firstChild.data
        self.music_head = self.music_head[:self.music_head.rfind('/')]
        self.music_suffix = self.doc.getElementsByTagName('decode')[0].firstChild.data
        self.music_network_url = '%s/%s' % (self.music_head, self.music_suffix)
        return self.music_network_url

if __name__ == '__main__':
    network = NetWork()
    print(network.get_music_play_url('see you again'))
