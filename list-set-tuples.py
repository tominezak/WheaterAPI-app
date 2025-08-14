"""
list = [] Ordnet og kan forandres - ok med duplikater
set = {} ikke ordnet og ikke foranderlig, Add/remove er ok  - ingen duplikater
tuple = () ornet og ikke foranderlig - ok med duplikater - raskere

"""

#LIST:
tall = [1, 2, 3]
print(tall[2])
print(tall[:2])
print(dir(tall)) # gir oss metoder listen kan utføre
print(help(tall))
len(tall)
print('1' in tall) # gir oss en boolean på om den finnes i lista
tall.append('6') 
tall.remove('1')
tall.insert(0, '4') #legger inn i lista på en bestemt index
tall.sort()
tall.reverse()
tall.clear()
tall.index('6')
tall.count('2') # teller forekomster av en verdi

#SET:
tall2 = {1 , 3,  4, 5}
tall2.add('8')
tall2.remove('1')
tall2.pop() #fjerner første element ( men random siden listen er uordnet)
tall2.clear()

#TUPLE:
tall3 = (1, 2, 3, 4, 5)
tall3.index('1')
tall3.count('3') # hvor mange forekomster av tallet 3
# kan iterere gjennom tuplen