# graph-friend-finder
Friend recommender with Graph API.

# Weight of each page
Weight of a page is calculated seeing number of occurrences of its gender. 
Gender with highest number of occurrences (GH) -> 1.0
Other genders -> number of occurrences / GH 

# Number of pages used for a user
300 (or while time proccess allows)

# Degree of similarity 
Sum of weight of pages liked by target user and possible friend

# General idea
List of users more similar (similar a target user)
Recommendes the first 10 users (no counting who is already friend)
