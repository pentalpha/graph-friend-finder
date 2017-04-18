#Gets the categories of pages liked by the user
#   token       user access token
#   return      dictionary of categories found, each with it's own array of pages
#       {c1 : [page1, page2, page3...], c2 : [page4, page5], c3 : [page6]...}
def getCats(token):
    import facebook as fb
    import requests as req
    cats = new dict()
    graph = fb.GraphAPI(access_token=token, version='2.8')
    resource = graph.get_object("me/likes?fields=name,category")
    cats = new dict()
    while(True):
        try:
            for page in resource['data']:
                cat = page['category']
                if(cats[cat] == null):
                    cats[cat] = []
                cats[cat].append(page['id'])
            # Attempt to make a request to the next page of data, if it exists.
            resource=req.get(resource['paging']['next']).json()
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return cats

def getPagesList(user):
    pages = new list()

    return pages

#Classifies pages by categories, the category with more pages gets 1.0
#and the smaller categories get smaller and smaller classifications...
#   cats        dictionary of categories found, each with it's own array of pages
#       {c1 : [page1, page2, page3...], c2 : [page4, page5], c3 : [page6]...}
#   return      dictionary of pages, each with it's own classification (0.0 < classification <= 1.0)
#       {page1 : x, page2 : x, page4 : y, page6 : z}
def classify(cats):
    classification = new dict()
    biggestCat = ""
    biggestCatLen = 0
    for cat, pages in cats.iteritems():
        if(len(pages) > biggestCatLen):
            biggestCat = cat
            biggestCatLen = len(pages)
    for cat, pages in cats.iteritems():
        classify = len(pages)/biggestCatLen
        for i in len(pages)
            classification[pages[i]] = classify

    return classification

#START
token = "EAACEdEose0cBAD1aEd0H3y6aS8hQZCEs3787KaDzI5IoZCIopFgdRCpW82vQUkYkWkranW8rIO5jNTpanWudbJ6RhT8jjtrV4a0wvAFRwnS26RZB3FpdBlbZBnkznMOWWMZAgXR5WcfU6VKmeSwBjkyD6MAN0pT8HVWnnBs09kj46WZA821pVktmxEnuCvOYIi5XirZBWO9ZBdCUQRj9OmWE870amvlZCjvIZD"
cats = getCats(token)
classf = classify(cats)
