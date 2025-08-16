d = {}

name = input("#enter friends name :")
lang = input("#enter langauge name :")
d.update({name: lang})
name = input("#enter friends name :")
lang = input("#enter langauge name :")
d.update({name: lang})
name = input("#enter friends name :")
lang = input("#enter langauge name :")
d.update({name: lang})
name = input("#enter friends name :")
lang = input("#enter langauge name :")
d.update({name: lang})
print(d)

# for same name of friend one after another value wiil be upadted 
# and only written 2nd or next value 
##enter friends name :harry
#enter langauge name :pythob
#enter friends name :krishn
#enter langauge name :c
#enter friends name :rohan
#enter langauge name :c
#enter friends name :rohan
#enter langauge name :ai
#{'harry': 'pythob', 'krishn': 'c', 'rohan': 'ai'}
# like this rohan name is same nut in o/p only occur 2nd lang ai
#this is because we writed.update() dictioary is updating


#this is for if key same hai to

# but what if value same in Q8 then no change