def make_album(singer_name,album_name,acount=None):
   album={
    'singer_name':singer_name,
    'album_name':album_name,
  }
   if acount!=None:
     album['acount']=acount
   return album

while True:
    print("enter 'q' at any time to quit")
    singer_name=input("singer_name:")
    if singer_name=='q':
        break
    album_name=input("album_name:")
    if album_name=='q':
        break
    acount=input("acount:")
    if acount=='q':
        break
    re=make_album(singer_name,album_name,acount)
    print(re)