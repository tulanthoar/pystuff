fl = open( 'txt', 'r' )
print( fl.read() )
print( fl.tell() )
fl.seek( 0, 0 )
print( fl.read( 1 ) )
print( fl.read( 1 ) )
fl.close()
fl = open( 'txt', 'w' )
fl.write( 'a line written' )
fl.close()
fl = open( 'txt', 'r' )
print( fl.read() )
fl.close
fl = open( 'txt', 'a' )
fl.write( 'a line added' )
fl.close()
fl = open( 'txt', 'r' )
print( fl.read() )
nfl = open( 'newf', 'w' )
nfl.write( fl.read() )
nfl.close()
nfl = open( 'txt', 'r' )
print( nfl.read() )
nfl.close()