# Story Generator with Python
import random
when = ['A few years ago','Yesterday','Last night','A long time ago','on 20th jan']
who = ['a rabbit', 'an elephant','a mouse','a turtle','a cat']
name = ['Ali','Miriam','Daniel','Hoouk','Starwalker']
residence = ['Barcelona','India','Germany','Venice','England']
went = ['cinema','university','seminar','school','laundry']
happened = ['made a lot of friends','eat a burger','found a secret key','solved a mistery','wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))




