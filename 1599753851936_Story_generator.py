import os
#importing to have access over os

import requests
#Importing requests to make requests from url

from bs4 import BeautifulSoup
#importing BeautifulSoup to get the HTML block of website

import random
#importing random to generate random choice

from gtts import gTTS
#Importing gtts to convert text to speech


link = "https://americanliterature.com/short-short-stories"
#link containing the stories


headers={"User-Agent":"Mozilla/5.0"}
#Using Mozilla to fetch data

def Story():
    page=requests.get(link)
    #Getting request to the link
    
    s=BeautifulSoup(page.content, 'html.parser')
    #getting the html format of that link

    t=[]
    #Creating empty list
    
    t_get=s.find_all('a', class_="sslink", href=True)
    #Fetching all link in that website
    
    for title in t_get:
        t.append(title.text)
        #appending all the link in the list

    story=random.choice(t)
    #Taking the link of the story randomly
    
    story_yes=input("The story you will get is {"+story+"} (y/n)").lower()
    #Displaying story title and asking user input(y/n)
    
    
    if story_yes == 'y':
        for i in t_get:
            if i.text == story:
                #Checks the relevant story in the website and gets its link.
                
                story_l = i['href']
        creates(story_l)
        #Passing the story link to the function named creates

    elif story_yes == 'n':
        t.clear()
        #Clearing the list
        
        Story()
        #Calling main function again
        
def creates(storylink):
    lang = 'en'
    #Setting lang to English
    
    storyl = "https://americanliterature.com/"+storylink
    #appending the story link with the base link

    page = requests.get(storyl, headers=headers)
    s =BeautifulSoup(page.content, 'html.parser')
    para = s.find_all('p')
    #Getting the paragraph alone from the HTML of that website
    
    story=""

    
    for i in para:
        #print(i.text)
        story=story+str(i.text)
        #Appending the story content in the string named story
    print(story)
    
   
    choose=input("Do you want to create audio of this story?!(y/n)").lower()
    #Asking user input to create audio of the story
    
    if choose == 'y':
        speech=gTTS(text=story, lang=lang, slow=False)
        #converting story to audio
        
        speech.save("Story.mp3")
        #saving file with name Story.mp3
        
        os.system("Story.mp3")
        #Opening the file
    else:
        g=input("Want to continue reading story?!(y/n)").lower()
        if g == 'y':
            Story()
            #Calling main function again
        else:
            exit(0)
            #Program terminates

#Calling main function
Story()

