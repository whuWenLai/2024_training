def make_album(singer_name,album_name,acount=None):
    album={
        'singer_name':singer_name,
        'album_name':album_name,
    }
    if acount!=None:
        album['acount']=acount
    return album


print(make_album('xzq', 'peace and love', 4))
print(make_album('dzq', 'more love'))