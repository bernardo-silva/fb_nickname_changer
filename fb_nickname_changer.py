'''
Divirtam-se a fazer spam

-Bernardo Silva
'''

import getpass
import fbchat
from random import choice

#function to MakE THis tO A strINg
def TexTO(text):
    return ''.join(choice((str.upper, str.lower))(c) for c in text)


#Login to facebook
session = fbchat.Client("email@email.com", getpass.getpass())

#Search for group by name
group = session.searchForGroups("Group name")[0]

for userID in group.participants:
	#Get user info
	user_info = session.fetchUserInfo(userID)
	#Print user full name
	print(TexTO(user_info[userID].name))
	#change the nickname
	session.changeNickname(TexTO(user_info[userID].name),userID,thread_id=group.uid,thread_type=fbchat.ThreadType.GROUP)