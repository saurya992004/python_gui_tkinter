from tkinter import *
from PIL import ImageTk,Image
import os
def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1





counter=1
root=Tk()
root.title('Wallpaper viewer')
root.geometry('550x750')
root.configure(background='black')
files=os.listdir('wallpapers')

img_array=[]
for file in files:
    img=Image.open(os.path.join('wallpapers',file))
    resized_image=img.resize((400,500))
    img_array.append(ImageTk.PhotoImage(resized_image))

print(img_array)
img_label=Label(root,image=img_array[0])
img_label.pack(pady=(20,30))
next_btn=Button(root,text='NEXT',bg='white',fg='black',width=45,height=4,command=rotate_img)
next_btn.pack()




root.mainloop()


