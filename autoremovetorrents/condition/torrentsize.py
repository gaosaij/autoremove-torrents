#-*- coding:utf-8 -*-

from .sortbase import ConditionWithSort

class TorrentSizeCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._limit = settings['limit'] * 1073741824 # limit = limit * 1GiB

    def apply(self, torrents):
        ConditionWithSort.sort_torrents(self, torrents)
        size_sum = 0
        for torrent in torrents:
            if size_sum+torrent.size < self._limit:
                size_sum += torrent.size
                self.remain.append(torrent)
            else:
                self.remove.append(torrent)