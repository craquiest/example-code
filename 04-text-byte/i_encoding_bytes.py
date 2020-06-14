# coding: utf-8
s = 'café'
len(s)

b= s.encode('utf8')
b
len(b)
b.decode('utf8')

euro= bytes.fromhex('E2 82 AC')
euro
euro.decode('utf8')

f= lambda o:bytes.fromhex(str(o)).decode('utf8')
f(41)
f('E2 82 AC')
f('c3 a9')

g= lambda o:bytes.fromhex(str(o)).decode('utf16')
g('ac 20')
g('a9 c3')

cafe = bytes('café', encoding='utf8')
cafe
cafe[0]
cafe[1]
cafe[:1]

cafe_arr= bytearray(cafe)
cafe_arr

bytes(' ', encoding='utf8')
b' '
b' '.decode()
b'caf\xc3\xa9'.decode()
b'caf\xc3\xa9'.upper().decode()
b' '[0]

b'A'
b'A'[0]



bytes((1,0)).decode()
bytes((97,)).decode()
bytes((32,)).decode()
for x in range(255): print(str(x)+': ',bytes((x,)).decode('utf_8',errors='replace'),end='\t')

for codec in [ 'latin_1' , 'utf_8' , 'utf_16' ]:
    print ( codec , 'El Niño' . encode ( codec ), sep = ' \t ' )
    
f('c3b1')
'El Ni' +f('c3b1')+'o'
f('c3b1').encode()


city = 'São Paulo' 
city.encode('utf8')
city.encode('iso8859_1')
# city.encode('cp437')
city.encode('cp437',errors='ignore')
city.encode('cp437',errors='replace')
city.encode('cp437',errors='xmlcharrefreplace')


octets = b'Montr\xe9a1'
octets.decode('cp1252')
octets.decode('iso8859_7')
octets.decode('koi8_r')
octets.decode('utf_8')
octets.decode('utf_8',errors='replace')


u16 = 'El Niño'.encode('utf-16')
u16
list(u16)
u16le = 'El Niño'.encode('utf-16le')
list(u16le)
u16be = 'El Niño'.encode('utf-16be')
list(u16be)
