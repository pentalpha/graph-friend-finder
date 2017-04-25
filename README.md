# Friends Finder Project

### Our goal is to create a tool to search new friends for a user, trying to find people with similar personalities.

- It is an app based on the Graph API;
- Gets the user's access token and uses it to search for close people and sort them acording to similaries;
- The similarities are the kinds of stuff the users like the most: art, movies, music and etc...;
- To classify types of interests we use Facebook's page categories;
- We cluster the user's likes by category, the category with more likes receives the biggest value and categories with less likes receive smaller values;
- We compare the pages the users like. When looking for similarity, a page's value is his category value;
- That means: If user X is using this tool to find new friends and user X likes a lot of music pages, this tool will classify users who like a lot of music pages too as more similar to user X;
