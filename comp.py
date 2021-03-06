import facebook
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['message'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
app_id = ""
app_secret = ""
# access_token = app_id + "|" + app_secret
access_token = ""
# Look at Bill Gates's profile for this example by using his Facebook id.
user = 'neuconfessions'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')
comments = graph.get_connections(posts['data'][3]['id'], 'comments', limit = "100")

#
# print(posts['data'][0]['id'])
# comments = graph.get_connections(posts['data'][1]['id'], 'comments')
# for i in range(0,50):
#     print(comments['data'][i]['message'])
count = 0
for i in range(0,100):
    count = count + 1
    try:
        print(comments['data'][i]['message'])
        with open("neuconf.txt", "a") as commentFile:

            comment = graph.get_connections(id=comments['data'][i]['id'], connection_name='comments')
            if len(comment['data']) >= 1:
                commentFile.write("Q:" + comments['data'][i]['message'] + "\n")
                print("Reply : \n")
                # print("LENGHT")
                # print(comment)
                for j in range(0,1):
                    try:
                        print(comment['data'][j]['message'])
                        commentFile.write("A:" + comment['data'][j]['message'] + "\n")
                    except IndexError:
                        pass
                    continue
            commentFile.close()
        print(count)
        print(".........................")
    except IndexError:
        pass
    continue

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
# while True:
#     try:
#         # Perform some action on each post in the collection we receive from
#         # Facebook.
#         [some_action(post=post) for post in posts['data']]
#         # Attempt to make a request to the next page of data, if it exists.
#         posts = requests.get(posts['paging']['next']).json()
#     except KeyError:
#         # When there are no more pages (['paging']['next']), break from the
#         # loop and end the script.
#         break