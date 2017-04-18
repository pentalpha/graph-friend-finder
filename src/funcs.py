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

#START
#this is my token (Pitágoras)
token = "EAACEdEose0cBAOIbVNcNo8ZBSYZBqv4eI85B6SG65AE4RvaZAO7Ixkz0gPknYsg2oWAMHDZAHhEQEA8JUQlxuvmK4NyQm6lKQYAsytVB6qMwYwHzWqZB0aGhaA7Wr8M5aYKGF6wvSao2E7cvvBfaVUcZCGmcwd99juf2gG7ZBZCQod2gVXuofv6ZCioanFmzASNEZD"
#ID of "Aryan Dantas Gomes"
otherPersonID = "100002541369604"
otherUserPages = getPagesList(otherPersonID, token)
print(otherUserPages)
#cats = getCats(token)
#classf = classify(cats)
#example print classifications
#count = 0
#for page, classification in classf.items():
#    print(page + ": " + str(classification))
#    count = count + 1
#    if(count > 20):
#        break
