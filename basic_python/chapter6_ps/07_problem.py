# Write a program to find out whether a given post is talking about “Anup” or not.
post=input("enter your comment...:")
if("anup"in post.lower()):
    print("this post talk about Anup")
else:
    print("this post is not talk about Anup")