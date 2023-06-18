
while chat.is_alive():
     for c in chat.get().sync_items():
         try:
            chan = c.author.name
            msg = c.message.lower()
            print(msg)
            if(chan !=BotName):
             if(msg.startswith("fun ") or (" bor ") in msg or (" fun ") in msg or (" kills ") in msg):
                 try:
                    responce = [" Fun is subjective ", " when ever u kill a person remember that there is a human behind the charector ", " you have fun? ", " yes yes good play "]
                    data = chan +" "+ responce[randrange(0, len(responce))]
                    print("fun is triggered")
                    reply(data)
                 except:
                     print(" op deggara error ")
             if(msg.startswith("op ") or (" op ") in msg or (" nt") in msg or msg.startswith("nicetry") or ("nice try") in msg or (" nt ") in msg   ):
                 try:
                    responce = ["that was cool isnt it", " its natural he is a pro  ", " well that was intense,isnt it?", " yes yes good play "]
                    data = chan +" "+ responce[randrange(0, len(responce))]
                    reply(data)
                 except:
                     print(" op deggara error ")
         except Exception as e:
            print(e)