import time

start_time = time.time()  # 初始时间戳

import stagger
from stagger.id3 import *       # contains ID3 frame types

# Friendly names API
_friendly_names = ["title", "artist","date","album-artist", "album",
                   "track", "track-total",
                   "disc", "disc-total",
                   "grouping", "composer",
                   "genre",
                   "comment",
                   # "compilation",
                   "picture",
                   "sort-title", "sort-artist",
                   "sort-album-artist", "sort-album",
                   "sort-composer",
                   ]
tag = stagger.read_tag("/Users/alicewish/Desktop/Miranda Cosgrove - Sparks Fly 05 - Hey You (2010).mp3")

print(tag[TIT2])                                      # tag is a MutableMapping
print(tag.title)
print(tag.track)
print(tag.track_total)
print(tag.disc)
print(tag.disc_total)
print(tag.artist)
print(tag.album)
print(tag.date)

print(tag.genre)
print(tag.album_artist)

print(tag.comment)

# tag[TIT2] = TIT2(text="The Show Must Go On")   # Explicit constructor
# tag[TIT2] = "The Show Must Go On"              # Implicit constructor
# tag[TIT2] = ("Foo", "Bar", "Baz")              # Multiple strings
# tag.title = "The Battle of Evermore"           # Alternative, friendlier API
#
# tag.write()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
