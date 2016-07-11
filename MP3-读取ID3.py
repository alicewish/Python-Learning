import time

start_time = time.time()  # 初始时间戳
import eyed3
 
#----------------------------------------------------------------------
def getEyeD3Tags(path):
    """"""
    trackInfo = eyed3.Mp3AudioFile(path)
    tag = trackInfo.getTag()
    tag.link(path)
 
    print("Artist: %s" % tag.getArtist())
    print("Album: %s" % tag.getAlbum())
    print("Track: %s" % tag.getTitle())
    print("Track Length: %s" % trackInfo.getPlayTimeString())
    print("Release Year: %s" % tag.getYear())

getEyeD3Tags("/Users/alicewish/Desktop/Miranda Cosgrove - Sparks Fly 05 - Hey You (2010).mp3")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
