import tkinter
from tkcalendar import DateEntry
from tkinter import filedialog
import requests
from PIL import ImageTk, Image
from io import BytesIO
import webbrowser


#Define window
root = tkinter.Tk()
root.title('APOD Photo Viewer')

#Define fonts and colors
text_font = ('Time New Roman', 14)
nasa_blue = '#043c93'
nasa_light_blue = '#7aa5d3'
nasa_red = '#ff1923'
nasa_white = '#ffffff'
root.config(bg=nasa_blue)

#Define functions
def get_request():
    '''Get request data from NASA APOD API'''
    global response

    #Set the parameters for the request
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'YOUR KEY HERE'
    date = calender.get_date()
    querystring = {'api_key':api_key, 'date': date}

    #Call the request and turn it into a Python useable format
    response = requests.request("GET", url, params=querystring)
    response = response.json()

    #Update output labels
    set_info()

def set_info():
    '''Update output labels based on api call
    {'date': '2023-07-31', 'explanation': "Why is Phobos so dark?  Phobos, the largest and innermost of the two Martian moons, is the darkest moon in the entire Solar System.
    Its unusual orbit and color indicate that it may be a captured asteroid composed of a mixture of ice and dark rock.  The featured assigned-color picture of Phobos near
    the edge of Mars was captured in late 2021 by ESA's robot spacecraft Mars Express, currently orbiting Mars.  Phobos is a heavily cratered and barren moon, with its
    largest crater located on the far side.  From images like this, Phobos has been determined to be covered by perhaps a meter of loose dust.
    Phobos orbits so close to Mars that from some places it would appear to rise and set twice a day, while from other places it would not be visible at all.
    Phobos' orbit around Mars is continually decaying -- it will likely break up with pieces crashing to the Martian surface in about 50 million years.
    Your Sky Surprise: What picture did APOD feature on your birthday? (post 1995)",
    'hdurl': 'https://apod.nasa.gov/apod/image/2307/PhobosMars_MarsExpress_1500.jpg', 'media_type': 'image', 'service_version': 'v1', 'title': 'Phobos over Mars',
    'url': 'https://apod.nasa.gov/apod/image/2307/PhobosMars_MarsExpress_960.jpg'}
    '''

    #Update the picture date and explanation
    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'])

    #We need to use 3 images in other functions; an img, a thumb, and a full_img
    global img
    global thumb
    global full_img

    url = response['url']
    if response['media_type'] == 'image':
        #Grab the photo that is stored in our responce
        img_response = requests.get(url, stream=True)

        #Get the content of the response and use bytesIO to open it as an image
        #Keep a reference to this image as this is what we can use to save the image (Image not PhotoImage)
        #Create the full screen image for a second window
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))

        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,200))
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumbnail image
        picture_label.config(image=thumb)
    elif response['media_type'] == 'video':
        picture_label.config(text=url, image='')
        webbrowser.open(url)

def full_photo():
    '''Open the full size photo in a new window'''
    top = tkinter.Toplevel()
    top.title('Full APOD Photo')

    #Load the full image to the top window
    img_label = tkinter.Label(top, image=full_img)
    img_label.pack()

def save_photo():
    '''Save the desired photo'''
    save_name = filedialog.asksaveasfilename(initialdir='./', title='Save Image', filetypes=(('JPEG', '*.jpg'), ('All Files', '*.*')))
    img.save(save_name + '.jpg')

#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for the input frame
calender = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = tkinter.Button(input_frame, text='Submit', font=text_font, bg= nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text='Full Photo', font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = tkinter.Button(input_frame, text='Save Photo', font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = tkinter.Button(input_frame, text='Exit', font=text_font, bg=nasa_red, command=root.destroy)


calender.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Layout for the output frame
picture_date = tkinter.Label(output_frame, font=text_font, bg=nasa_white)
picture_explanation = tkinter.Label(output_frame, font=text_font, bg=nasa_white, wraplength=600)
picture_label = tkinter.Label(output_frame)

picture_date.grid(row=1, column=1, padx=10)
picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)

#Get today's photo to start with
get_request()

#Run main window
tkinter.mainloop()
