import facebook

token=''

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'],"posts")
graph.put_comment("","test")