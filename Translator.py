import tkinter as tk
def translate_to_hindi(st):
      from googletrans import Translator 
      translator=Translator() 
      
      output=translator.translate(st[0],src='en',dest='hi').text #translate function 
      print(output)

      import mysql.connector

     # Connect to database
      mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="___________",
      database="Db1"
      )
      cur=mydb.cursor()
      #insert the query  into table
      s="INSERT INTO Translators (Sentence) VALUES(%s)"
      q1=(st)
      cur.execute(s,q1)
      # commit the changes
      mydb.commit()
      return output
# Define function to be called when button is clicked
def button_click():
    input_text = input_entry.get()
    st=[]
    st.append(input_text)
    text=translate_to_hindi(st)
    output_text = "Translation: " + text
    output_label.config(text=output_text)

# Create the main window
root = tk.Tk()
root.title("English to Hindi translator")

# Increase font size for all widgets
font_size = 16
font_style = ("Arial", font_size)

# Create the label for displaying text
display_label = tk.Label(root, text="Enter the sentence you want to translate:", font=font_style)
display_label.pack(pady=20)

# Create the entry widget for input
input_entry = tk.Entry(root, font=font_style)
input_entry.pack(pady=10)

# Create the button widget
button = tk.Button(root, text="Go", font=font_style, command=button_click)
button.pack(pady=20)

# Create the label for displaying output
output_label = tk.Label(root, text="", font=font_style)
output_label.pack(pady=10)

# Increase gap between widgets
root.geometry("1200x600+100+200")

# Start the main event loop
root.mainloop()
