
import googlesearch                 #pip install googlesearch

import webbrowser


from googlesearch import search

query=input("enter your query:")
query1=""
list_needed=""

if 'who is' in query:       #you can use any wh word as prefix to the question
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s' 
    print('loading')
    query2=""
    list_needed=""
    str2=""
    if 'who is' in query :
        list_name=list(query)
        list_needed=list_name[7:]     # make sure you slice 1+ index than your prefix to the question
                
        for word in list_needed:  
             str2 += word   
            

        for url in search(str2, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % str2)

    
  
   





      
    
