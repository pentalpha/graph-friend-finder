
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
