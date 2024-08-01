import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns([1,2,1])


col1.markdown(" # Welcome to my website  ")
col1.markdown(" more details on my website is here ")

upload_photo = col2.file_uploader("Upload a photo")
#camera_photo = col2.camera_input("take a pic")



col3.metric("Weight", "Kuhu ", "27 kg")
col3.metric("Weight", "Vanu", "-26 kg")
col3.metric("weight", "Dada", "36 kg")



image = col3.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGJoZzN6Z3IwemJlcTJpcjg4bDYzamxkY2J6cjRiNWF3dGFjbDlzMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aD0qikeYPBASzfy/giphy.gif', caption='Animated Image', use_column_width=True)



# Title
col2.title('square')

x = col2.slider('Select a number between 0 and 100', 0, 100)

y = x * x

# Display the result
col2.title(f" {x * x} = {y}")

