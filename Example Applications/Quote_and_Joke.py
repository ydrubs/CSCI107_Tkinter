import tkinter
from tkinter import font, BOTH
import requests
import random

#Define Root window
root = tkinter.Tk()
root.title('Layout Experiment 1')
root.iconbitmap()
height='475'
width='475'
root.geometry(height+'x'+width)
root.resizable()
# print(list(font.families()))

#Define fonts and colors
root_color = '#FEFAE0'
quad1_color = '#90A583'
quad2_color = '#9D8420'
quad3_color = '#94B9AF'

#Functions
import requests

def get_quote():
    category_list = ['attitude', 'change', 'dreams', 'education', 'future', 'imagination', 'money', 'history']
    category = random.choice(category_list)
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY HERE'})
    if response.status_code == requests.codes.ok:
        # print(response.text)

        print(response)
        print(response.text.strip('[]'))
        quote_display = response.text.split(':',2)[1].strip(', \"author\"')
        print(quote_display)

        # print('\n\n')
        # quote_display_demo = response.text.split(':',2)
        # print(quote_display_demo)
        # print(quote_display_demo[1])
        # quote_display_demo = quote_display_demo[1].strip((', \"author\"'))
        # print(quote_display_demo)


        quote.config(text=quote_display, wraplength=430, font=('Engravers MT', 12))
    else:
        print("Error:", response.status_code, response.text)

def get_chuck_joke():
    api_url = 'https://api.api-ninjas.com/v1/chucknorris'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY HERE '})
    print(response)
    if response.status_code == requests.codes.ok:
        # print(response.text)
        joke = response.text.split(':', 2)[1].strip(' \"}')
        quote.config(text=joke, wraplength=430, font=('Engravers MT', 12))
    else:
        print("Error:", response.status_code, response.text)


frame = tkinter.Frame(root, height='200', width='200', bg=root_color)
frame.pack()

quad1 = tkinter.Frame(frame, bg = quad1_color, height=int(height)/2.25, width=int(width)/2.25)
quad1.grid(row=0, column=0, padx=5, pady=5)
quad2 = tkinter.Frame(frame, height=int(height)/2.25, width=int(width)/2.25, bg=quad2_color)
quad2.grid(row=0, column=1, padx=5, pady=5)
quad3 = tkinter.Frame(frame, height=int(height)/2, width=int(width)-40, bg=quad3_color)
quad3.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

quad1.propagate(False)
quad2.pack_propagate(False)
quad3.pack_propagate(False)
# tkinter.Button(quad2, text="Press Me").pack()
tkinter.Button(quad1, text="Get Quote", font=('Arial', 12), command=get_quote).pack(pady=60)
tkinter.Button(quad2, text="Get Chuck Norris Joke", font=('Arial', 12), command=get_chuck_joke).pack(pady=60)
quote = tkinter.Label(quad3, bg=quad3_color)
quote.pack(fill='y', ipady=60, expand=True)


#Run main window
root.mainloop()



