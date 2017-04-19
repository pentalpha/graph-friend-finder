#Gets the categories of pages liked by the user
#   token       user access token
#   return      dictionary of categories found, each with it's own array of pages
#       {c1 : [page1, page2, page3...], c2 : [page4, page5], c3 : [page6]...}
def getCats(token):
    from collections import defaultdict as ddict
    import facebook as fb
    import requests as req
    cats = ddict(str)
    graph = fb.GraphAPI(access_token=token, version='2.7')
    resource = graph.get_object("me/likes?fields=name,category")
    #print(resource)
    cats = dict()
    while(True):
        for page in resource['data']:
            cat = page['category']
            if not(cat in cats):
                cats[cat] = []
            cats[cat].append(page['id'])
        # Attempt to make a request to the next page of data, if it exists.
        try:
            resource=req.get(resource['paging']['next']).json()
        except KeyError:
            print("Finished getting pages")
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return cats

#Get the pages that a given user liked
#   user    id of a user
#   token   access token
#   return  array of page IDs
#       [page1, page2, page3...]
def getPagesList(user, token):
    from collections import defaultdict as ddict
    import facebook as fb
    import requests as req
    pages = list()
    graph = fb.GraphAPI(access_token=token, version='2.7')
    resource = graph.get_object(user+"/likes?fields=name")
    #print(resource)
    cats = dict()
    while(True):
        for page in resource['data']:
            pages.append(page['id'])
        # Attempt to make a request to the next page of data, if it exists.
        try:
            resource=req.get(resource['paging']['next']).json()
        except KeyError:
            print("Finished getting pages from user " + user)
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return pages

#Classifies pages by categories, the category with more pages gets 1.0
#and the smaller categories get smaller and smaller classifications...
#   cats        dictionary of categories found, each with it's own array of pages
#       {c1 : [page1, page2, page3...], c2 : [page4, page5], c3 : [page6]...}
#   return      dictionary of pages, each with it's own classification (0.0 < classification <= 1.0)
#       {page1 : x, page2 : x, page4 : y, page6 : z}
def classify(cats):
    from collections import defaultdict as ddict
    classification = ddict()
    biggestCat = ""
    biggestCatLen = 0
    for cat, pages in cats.items():
        if(len(pages) > biggestCatLen):
            biggestCat = cat
            biggestCatLen = len(pages)
    for cat, pages in cats.items():
        classify = len(pages)/biggestCatLen
        for i in pages:
            classification[i] = classify

    return classification

def similarityWith(user, classification, token):
    otherUserPages = getPagesList(user, token)
    rate = 0.0
    for page in otherUserPages:
        if page in classification:
            rate = rate + classification[page]
    return rate

# return dict { id1 : friend_name1, id2 : friend_name2 }
def getFriends(user, token):
	import facebook as fb
	import requests as req
	graph = fb.GraphAPI(access_token=token, version='2.7')
	resource = graph.get_object("/" + user + "/friends")
	friends = dict()
	while(True):
		for friend in resource['data']:
			friends[friend['id']] = friend['name']
			# Attempt to make a request to the next page of data, if it exists.
		try:
			resource=req.get(resource['paging']['next']).json()
		except KeyError:
			print("Finished getting friends from user " + user)
			# When there are no more pages (['paging']['next']), break from the
		# loop and end the script.
			break

	return friends

def getUsersDict(user, token):
    friends = getFriends(user, token)
    ffriends = dict() 
    listFFriends = []
    for idFriend in friends: 
        friendsOfFriends = getFriends(idFriend, token)
        for idUser, name in friendsOfFriends.items():
            if not idUser in ffriends and not idUser in friends:
                ffriends[idUser] = name
                listFFriends.append([idUser, name])
    
    count = 0
    while len(listFFriends) < 400 and len(listFFriends) > count:
        curruentID = listFFriends[count][0]
        friendsCurrentID = getFriends(curruentID, token)
        for idUser, name in friendsOfFriends.items():
            if not idUser in ffriends:
                ffriends[idUser] = name
                listFFriends.append([idUser, name])	
        count+=1
    return ffriends	

#START
#this is my token (Carol)
token = "EAACEdEose0cBAA4uVmBfFvWvwxotAPMlPPtQVH3aFAYJTDYHbX0Wq88DzomDRB8nmabrI64wR3GvIKRapB4CBiyaeljF4ZBskIGZBrCIWuyZAOLgswZCPaVz8VnBsBAZCFUjE0X8qoiHXGRVfq7WCUqaZAMFq8w9rgJ38ZC7xoqhrZBXI0n8wnfAhv86juY5rBgZD"
 
#ID of "Pitagoras"
#otherPersonID = "10208935375967359"

users = getUsersDict('me', token)

#otherUserPages = getPagesList(otherPersonID, token)
#print(otherUserPages)
#cats = getCats(token)
#classf = classify(cats)
#similarity = similarityWith(otherPersonID, classf, token)
#print("Similarity with " + otherPersonID + ": " + str(similarity))
#example print classifications
#count = 0
#for page, classification in classf.items():
#    print(page + ": " + str(classification))
#    count = count + 1
#    if(count > 20):
#        break
