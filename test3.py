import re



pattern= "[^\x20-\x7E]+"




test="b'x0cPRAISE FOR RYAN HOLIDAY AND TRUST ME, I\xe2\x80\x99M LYING\n\n\xe2\x80\x9cRyan Holiday\xe2\x80\x99s absolutely brilliant expos\xc3\xa9 of the unreality of the Internet should be required reading\n\nfor every thinker in America.\xe2\x80\x9d\n\n\xe2\x80\x94Edward Jay Epstein, author of The Big Picture: Money and Power in Hollywood\n\n\xe2\x80\x9cBehind my reputation as a marketing genius there is Ryan Holiday, who I consult often and has\n\nhelped build and done more for my business than just about anyone.\xe2\x80\x9d\n\n\xe2\x80\x94Dov Charney, CEO and founder of American Apparel\n\n\xe2\x80\x9cRyan is part Machiavelli, part Ogilvy, and all results. From American Apparel to the quiet\n\ncampaigns he\xe2\x80\x99s run but not taken credit for, this whiz kid is the secret weapon you\xe2\x80\x99ve never heard of.\xe2\x80\x9d\n\n\xe2\x80\x94Tim Ferriss, author of the #1 New York Times bestseller The 4-Hour Workweek\n\n\xe2\x80\x9cThe strategies Ryan created to exploit blogs drove sales of millions of my books and made me an\ninternationally known name. The reason I am standing here while other celebrities were destroyed or\n\nbecame parodies of themselves is because of his insider knowledge.\xe2\x80\x9d\n\n\xe2\x80\x94Tucker Max, author of the #1 New York Times bestseller I Hope They Serve Beer in Hell\n\n\xe2\x80\x9cJust as I thought it would\xe2\x80\x94it takes a twentysomething media insider to blow the lid off the real\n\nworkings of today\xe2\x80\x99s so-called news media. Holiday shows exactly how a handful of dodgy bloggers\n\ncontrol the whole system and turn our collective attention into their own profit.\xe2\x80\x9d\n\n\xe2\x80\x94Andrew Keen, author of The Cult of the Amateur and Digital Vertigo\n\n\xe2\x80\x9cWhen playing for high stakes, Ryan Holiday is my secret weapon. His unique stealth manner makes\n\nhim essential for winning.\xe2\x80\x9d\n\n\xe2\x80\x94Aaron Ray, partner of the management/production company The Collective with over 150 million albums sold and $1 billion in movie revenues\n\n\xe2\x80\x9cRyan Holiday is a man you should listen to\xe2\x80\xa6."
test=test.replace(test[:2],' ')
replaced = re.sub(pattern, '', test)

print(replaced)