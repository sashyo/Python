
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****N10091378*****
#    Student name: *****Sasha Le*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
import tkinter as tk
# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

from pathlib import Path
#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
archive_folder = 'archive/'
def download(url = 'http://www.wikipedia.org/',
            target_filename = ('download'),
            filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

url_music_chart = 'https://kworb.net/youtube/' 
url_movie_chart = 'https://www.boxofficemojo.com/daily/chart/'
url_game_chart = 'https://thinkgaming.com/app-sales-data/'

#Downloading webpage for old list

#download(url_music_chart, archive_folder + 'music_chart_archive')
#download(url_movie_chart, archive_folder + 'movie_chart_archive')
#download(url_game_chart, archive_folder + 'game_chart_archive')


#background\text colour
gui_color = 'white'
text_color = 'black'

the_window = tk.Tk()
the_window.configure(bg = gui_color)
the_window.title('Current and Past Trends')

#Logo icons for gui
logo = "images/trending.gif"
music_logo = "images/music.gif"
movie_logo = "images/movie.gif"
game_logo = 'images/game.gif'



currenttrendlabel = Label(the_window, text = "What's Trending?",font = ('system 10 points', 48)
                          ,bg = gui_color, fg = 'Black')
currenttrendlabel.grid(row=0,column=0, columnspan=3)

#homepage Icon picture
image = tk.PhotoImage(file= logo)
label = tk.Label(image=image,bg = gui_color)
label.image = image # keep a reference!
label.grid(row=1,column=0, columnspan= 3 )

#Music Frame for previous and current buttons
music_frame = Frame(the_window, relief ="groove", borderwidth = 4,bg= gui_color)
music_frame.grid(row = 2, column = 0)

#Music image title for fram
music = tk.PhotoImage(file=music_logo)
music_label = tk.Label(music_frame,image = music, bg= gui_color)
music_title = tk.Label(music_frame,text = 'Music on YouTube',font = (20), bg = gui_color)
music_label.image = music #keep a reference !
music_label.grid(row = 0, sticky ='s')
music_title.grid(row = 0,column=1, sticky = 's')

#movie frame for buttons
movie_frame = Frame(the_window, relief = 'groove', borderwidth = 4,bg = gui_color)
movie_frame.grid(row = 2, column = 1)

#movie image title for frame
movie = tk.PhotoImage(file=movie_logo)
movie_label =tk.Label(movie_frame, image = movie,bg = gui_color)
movie_title =tk.Label(movie_frame, text = 'Movies in Cinema' , font = (20),bg = gui_color)
movie_label.image = movie
movie_label.grid(row = 0, sticky = 's')
movie_title.grid(row = 0, column = 1, sticky = 's')

#games frame for button options
game_frame = Frame(the_window, relief = 'groove', borderwidth = 4, bg = gui_color)
game_frame.grid(row = 2, column = 2)

#games image title for frame
game = tk.PhotoImage(file = game_logo)
game_label = tk.Label(game_frame, image = game, bg = gui_color)
game_title = tk.Label(game_frame, text = ' Phone Games ' , font = (20),
                         bg = gui_color)
game_label.image = game
game_label.grid(row = 0, sticky = 's')
game_title.grid(row = 0, column = 1, sticky = 's')

#frame for action buttons
action_frame = Frame(the_window, relief = 'flat', borderwidth = 2, bg = gui_color)
action_frame.grid(row =3, column = 0,columnspan = 2)
action_frame_two = Frame(the_window, relief = 'flat', borderwidth = 2, bg = gui_color)
action_frame_two.grid(row = 3, column = 1 , columnspan = 2)
###################################################################################
#intVar for checkbox
music_previous_button = IntVar()
music_current_button = IntVar()
movies_previous_button = IntVar()
movies_current_button = IntVar()
games_previous_button = IntVar()
games_current_button = IntVar()
#checkboxes for catergories

music_previous = Checkbutton(music_frame, text = 'Previous', variable = music_previous_button, bg = gui_color)
music_previous.grid( row = 1, column = 0)
music_current = Checkbutton(music_frame, text = 'Current',variable = music_current_button, bg = gui_color)
music_current.grid(row = 2, column = 0, sticky = 'w')

movies_previous = Checkbutton(movie_frame, text = 'Previous', variable = movies_previous_button, bg = gui_color)
movies_previous.grid( row = 1, column = 0)
movies_current = Checkbutton(movie_frame, text = 'Current',variable = movies_current_button, bg = gui_color)
movies_current.grid(row = 2, column = 0, sticky = 'w')

games_previous = Checkbutton(game_frame, text = 'Previous', variable = games_previous_button, bg =gui_color)
games_previous.grid( row = 1, column = 0)
games_current = Checkbutton(game_frame, text = 'Current',variable = games_current_button, bg = gui_color)
games_current.grid(row = 2, column = 0, sticky = 'w')

#image for music gui window
music_logo ='images\youtube.gif'

#music current preview
def music_current_preview():
    music_chart_page = urlopen(url_music_chart)
    html_code = music_chart_page.read().decode("UTF-8")
    # Current Music Chart
    music_list = findall('<a href="[A-z0-9]+[A-z0-9]/[A-z0-9]+[A-z0-9].html">(.*)</a>', html_code)
    #remove special characters
      #  music_list = re.sub('\U0001f5e1'," ",str(music_list))
       # music_list = re.sub('<a href=\'[A-z]+[A-z]/[A-z]+[A-z].html\'>',
         #                             "",str(music_list))    
    top_one = music_list[0]
    top_two = music_list[1]
    top_three = music_list[2]
    top_four = music_list[3]
    top_five = music_list[4]
    top_six = music_list[5]
    top_seven = music_list[6]
    top_eight = music_list[7]
    top_nine = music_list[8]
    top_ten = music_list[9]
    music_current_preview = tk.Toplevel(the_window)
    music_current_preview.configure(bg = gui_color)
    music_current_preview.title('Current Music Trends Preview')    
    musictrendlabel = Label(music_current_preview, text = "Current Music Video Youtube Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    musictrendlabel.grid(row=0,column=1)
    #music preview frame
    music_preview =Frame(music_current_preview,relief='flat',bg = gui_color)
    music_preview.grid(row=1, column=1)

    #homepage Icon picture
    image = tk.PhotoImage(file='images\youtube.gif')
    label = tk.Label(music_current_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0,sticky='e' )
    top_one_list =tk.Label(music_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(music_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(music_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(music_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(music_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(music_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(music_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(music_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(music_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(music_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')
    
#music archive preview
def music_archive_preview():
    music_chart_page = open('archive\music_chart_archive.html',encoding = 'UTF-8')
    html_code = music_chart_page.read()
    # Current Music Chart
    music_list = findall('<a href="[A-z0-9]+[A-z0-9]/[A-z0-9]+[A-z0-9].html">(.*)</a>', html_code)
    #remove special characters
      #  music_list = re.sub('\U0001f5e1'," ",str(music_list))
       # music_list = re.sub('<a href=\'[A-z]+[A-z]/[A-z]+[A-z].html\'>',
         #                             "",str(music_list))    
    top_one = music_list[0]
    top_two = music_list[1]
    top_three = music_list[2]
    top_four = music_list[3]
    top_five = music_list[4]
    top_six = music_list[5]
    top_seven = music_list[6]
    top_eight = music_list[7]
    top_nine = music_list[8]
    top_ten = music_list[9]
    music_archive_preview = tk.Toplevel(the_window)
    music_archive_preview.configure(bg = gui_color)
    music_archive_preview.title('Previous Music Trends')    
    musictrendlabel = Label(music_archive_preview, text = "Previous Music Video Youtube Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    musictrendlabel.grid(row=0,column=2)
    #music preview frame
    music_preview =Frame(music_archive_preview,relief='flat',bg = gui_color)
    music_preview.grid(row=1, column=2)
    

    #homepage Icon picture
    image = tk.PhotoImage(file='images\youtube.gif')
    label = tk.Label(music_archive_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0 )
    top_one_list =tk.Label(music_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(music_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(music_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(music_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(music_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(music_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(music_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(music_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(music_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(music_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')
    




# Extracts Current Music webpage to html
def music_chart_current_export():

    
    
        music_chart_file = open('music_chart_current_export.html','w')
        music_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Currently Trending In Music </title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            <title> What's Currently Trending In Music </title>
            </style>   
            </head>
            <body>
        ''')
        
        music_chart_page = urlopen(url_music_chart)
        html_code = music_chart_page.read().decode("UTF-8")
        music_chart_page.close()


    # Heading for Current Music Chart
        music_heading_start_tag = '<span class="pagetitle">'
        music_heading_start = html_code.find(music_heading_start_tag)
        music_heading_start = music_heading_start+ len(music_heading_start_tag)
        music_heading_end = html_code.find('</span>')
        music_heading = html_code[music_heading_start:music_heading_end]

        music_chart_file.write('<h1 align= "center">'+ music_heading +'</h1>')
        
                             
    # table contents of chart, views and likes
        music_statistics = findall('<td>(\d+,[\d+,]*)</td>',html_code)

        top_one_views = music_statistics[0]
        top_one_likes = music_statistics[1]

        top_two_views = music_statistics[2]
        top_two_likes = music_statistics[3]

        top_three_views = music_statistics[4]
        top_three_likes = music_statistics[5]

        top_four_views = music_statistics[6]
        top_four_likes = music_statistics[7]

        top_five_views = music_statistics[8]
        top_five_likes = music_statistics[9]

        top_six_views = music_statistics[10]
        top_six_likes = music_statistics[11]

        top_seven_views = music_statistics[12]
        top_seven_likes = music_statistics[13]

        top_eight_views = music_statistics[14]
        top_eight_likes = music_statistics[15]

        top_nine_views = music_statistics[16]
        top_nine_likes = music_statistics[17]

        top_ten_views = music_statistics[18]
        top_ten_likes = music_statistics[19]


    #
    # Current Music Chart
        music_list = findall('<a href="[A-z0-9]+[A-z0-9]/[A-z0-9]+[A-z0-9].html">(.*)</a>', html_code)
    #remove special characters
      #  music_list = re.sub('\U0001f5e1'," ",str(music_list))
       # music_list = re.sub('<a href=\'[A-z]+[A-z]/[A-z]+[A-z].html\'>',
         #                             "",str(music_list))    
        top_one = music_list[0]
        top_two = music_list[1]
        top_three = music_list[2]
        top_four = music_list[3]
        top_five = music_list[4]
        top_six = music_list[5]
        top_seven = music_list[6]
        top_eight = music_list[7]
        top_nine = music_list[8]
        top_ten = music_list[9]

    # writing the top 10 charts in html
        music_chart_file.write('''<table align="center"; style="width:40%">
                              <tr>
                                  <th> </th>
                                  <th align="center"> Video </th>
                                  <th align="center"> Views </th>
                                  <th align="center"> Likes </th>
                              </tr>
                              <tr>
                                  <td align="center"> 1 </td>
                              '''
                                 '<td align="center">'+ top_one +'</td>'
                                 '<td align="center">'+ top_one_views+'</td>'
                                 '<td align="center">'+ top_one_likes+'</td>'
                             '</tr>'
                             '<tr>'
                                 '<td align="center">2</td>'
                                 '<td align="center">'+top_two+'</td>'
                                 '<td align="center">'+top_two_views+'</td>'
                                 '<td align="center">'+top_two_likes+'</td>'
                             '</tr>'
                             '<tr>'
                                 '<td align="center">3</td>'
                                 '<td align="center">'+top_three+'</td>'
                                 '<td align="center">'+top_three_views+'</td>'
                                 '<td align="center">'+top_three_likes+'</td>'
                            '</tr>'
                             '<tr>'
                                 '<td align="center">4</td>'
                                 '<td align="center">'+top_four+'</td>'
                                 '<td align="center">'+top_four_views+'</td>'
                                 '<td align="center">'+top_four_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">5</td>'
                                 '<td align="center">'+top_five+'</td>'
                                 '<td align="center">'+top_five_views+'</td>'
                                 '<td align="center">'+top_five_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">6</td>'
                                 '<td align="center">'+top_six+'</td>'
                                 '<td align="center">'+top_six_views+'</td>'
                                 '<td align="center">'+top_six_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">7</td>'
                                 '<td align="center">'+top_seven+'</td>'
                                 '<td align="center">'+top_seven_views+'</td>'
                                 '<td align="center">'+top_seven_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">8</td>'
                                 '<td align="center">'+top_eight+'</td>'
                                 '<td align="center">'+top_eight_views+'</td>'
                                 '<td align="center">'+top_eight_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">9</td>'
                                 '<td align="center">'+top_nine+'</td>'
                                 '<td align="center">'+top_nine_views+'</td>'
                                 '<td align="center">'+top_nine_likes+'</td>'
                               '</tr>'
                             '<tr>'
                                 '<td align="center">10</td>'
                                 '<td align="center">'+top_ten+'</td>'
                                 '<td align="center">'+top_ten_views+'</td>'
                                 '<td align="center">'+top_ten_likes+'</td>'
                               )
                            
                           
      
        
        


                               
        
        music_chart_file.close()
# Music Previous Export
def music_previous_export():
    music_chart_file = open('music_chart_previous_export.html','w')
    music_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Previously Trending In Music</title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            </style>
                
               
            </head>
            <body>
        ''')
        
    music_chart_page = open('archive\music_chart_archive.html',encoding = 'utf-8')
    html_code = music_chart_page.read()
    music_chart_page.close()


# Heading for Previous Music Chart
    music_heading_start_tag = '<span class="pagetitle">'
    music_heading_start = html_code.find(music_heading_start_tag)
    music_heading_start = music_heading_start+ len(music_heading_start_tag)
    music_heading_end = html_code.find('</span>')
    music_heading = html_code[music_heading_start:music_heading_end]

    music_chart_file.write('<h1 align= "center">'+ music_heading +'</h1>')
    
                         
# table contents of chart, views and likes
    music_statistics = findall('<td>(\d+,[\d+,]*)</td>',html_code)

    top_one_views = music_statistics[0]
    top_one_likes = music_statistics[1]

    top_two_views = music_statistics[2]
    top_two_likes = music_statistics[3]

    top_three_views = music_statistics[4]
    top_three_likes = music_statistics[5]

    top_four_views = music_statistics[6]
    top_four_likes = music_statistics[7]

    top_five_views = music_statistics[8]
    top_five_likes = music_statistics[9]

    top_six_views = music_statistics[10]
    top_six_likes = music_statistics[11]

    top_seven_views = music_statistics[12]
    top_seven_likes = music_statistics[13]

    top_eight_views = music_statistics[14]
    top_eight_likes = music_statistics[15]

    top_nine_views = music_statistics[16]
    top_nine_likes = music_statistics[17]

    top_ten_views = music_statistics[18]
    top_ten_likes = music_statistics[19]


#
# Previous Music Chart
    music_list = findall('<a href="[A-z0-9]+[A-z0-9]/[A-z0-9]+[A-z0-9].html">(.*)</a>', html_code)[0:50]
    
#remove special characters
  #  music_list = re.sub('\U0001f5e1'," ",str(music_list))
   # music_list = re.sub('<a href=\'[A-z]+[A-z]/[A-z]+[A-z].html\'>',
     #                             "",str(music_list))    
    top_one = music_list[0]
    top_two = music_list[1]
    top_three = music_list[2]
    top_four = music_list[3]
    top_five = music_list[4]
    top_six = music_list[5]
    top_seven = music_list[6]
    top_eight = music_list[7]
    top_nine = music_list[8]
    top_ten = music_list[9]

# writing the top 10 charts in html
    music_chart_file.write('''<table align="center"; style="width:40%">
                          <tr>
                              <th> </th>
                              <th align="center"> Video </th>
                              <th align="center"> Views </th>
                              <th align="center"> Likes </th>
                          </tr>
                          <tr>
                              <td align="center"> 1 </td>
                          '''
                             '<td align="center">'+ top_one +'</td>'
                             '<td align="center">'+ top_one_views+'</td>'
                             '<td align="center">'+ top_one_likes+'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+top_two+'</td>'
                             '<td align="center">'+top_two_views+'</td>'
                             '<td align="center">'+top_two_likes+'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">3</td>'
                             '<td align="center">'+top_three+'</td>'
                             '<td align="center">'+top_three_views+'</td>'
                             '<td align="center">'+top_three_likes+'</td>'
                        '</tr>'
                        '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+top_two+'</td>'
                             '<td align="center">'+top_two_views+'</td>'
                             '<td align="center">'+top_two_likes+'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">4</td>'
                             '<td align="center">'+top_four+'</td>'
                             '<td align="center">'+top_four_views+'</td>'
                             '<td align="center">'+top_four_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">5</td>'
                             '<td align="center">'+top_five+'</td>'
                             '<td align="center">'+top_five_views+'</td>'
                             '<td align="center">'+top_five_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">6</td>'
                             '<td align="center">'+top_six+'</td>'
                             '<td align="center">'+top_six_views+'</td>'
                             '<td align="center">'+top_six_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">7</td>'
                             '<td align="center">'+top_seven+'</td>'
                             '<td align="center">'+top_seven_views+'</td>'
                             '<td align="center">'+top_seven_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">8</td>'
                             '<td align="center">'+top_eight+'</td>'
                             '<td align="center">'+top_eight_views+'</td>'
                             '<td align="center">'+top_eight_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">9</td>'
                             '<td align="center">'+top_nine+'</td>'
                             '<td align="center">'+top_nine_views+'</td>'
                             '<td align="center">'+top_nine_likes+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">10</td>'
                             '<td align="center">'+top_ten+'</td>'
                             '<td align="center">'+top_ten_views+'</td>'
                             '<td align="center">'+top_ten_likes+'</td>'
                           )
                                            
    
    music_chart_file.close()
#Current movie chart preview
def movie_current_preview():
    movie_chart_page = urlopen(url_movie_chart)
    html_code = movie_chart_page.read().decode("UTF-8")
    # Current Movie Chart
    movie_list = findall('<a href="/movies/\?page=daily&id=\w*\d*.htm">([.*:;\'A-Z0-9\s]*[\(0-9)\]]*)',html_code)
    top_one = movie_list[0]
    top_two = movie_list[1]
    top_three = movie_list[2]
    top_four = movie_list[3]
    top_five = movie_list[4]
    top_six = movie_list[5]
    top_seven = movie_list[6]
    top_eight = movie_list[7]
    top_nine = movie_list[8]
    top_ten = movie_list[9]

    movie_current_preview = tk.Toplevel(the_window)
    movie_current_preview.configure(bg = gui_color)
    movie_current_preview.title('Current Movie Trends Preview')    
    movietrendlabel = Label(movie_current_preview, text = "Current Movie Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    movietrendlabel.grid(row=0,column=1)
    #music preview frame
    movie_preview =Frame(movie_current_preview,relief='flat',bg = gui_color)
    movie_preview.grid(row=1, column=1)

    #homepage Icon picture
    image = tk.PhotoImage(file='images\cinema.gif')
    label = tk.Label(movie_current_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0,sticky='e' )
    top_one_list =tk.Label(movie_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(movie_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(movie_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(movie_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(movie_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(movie_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(movie_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(movie_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(movie_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(movie_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')   

#archive movie preview
def movie_archive_preview():
    movie_chart_page =open('archive\movie_chart_archive.html',encoding='utf-8')
    html_code = movie_chart_page.read()
    # Current Movie Chart
    movie_list = findall('<a href="/movies/\?page=daily&id=\w*\d*.htm">([.*:;\'A-Z0-9\s]*[\(0-9)\]]*)',html_code)
    top_one = movie_list[0]
    top_two = movie_list[1]
    top_three = movie_list[2]
    top_four = movie_list[3]
    top_five = movie_list[4]
    top_six = movie_list[5]
    top_seven = movie_list[6]
    top_eight = movie_list[7]
    top_nine = movie_list[8]
    top_ten = movie_list[9]

    movie_archive_preview = tk.Toplevel(the_window)
    movie_archive_preview.configure(bg = gui_color)
    movie_archive_preview.title('Previous Movie Trends Preview')    
    movietrendlabel = Label(movie_archive_preview, text = "Previous Movie Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    movietrendlabel.grid(row=0,column=1)
    #movie preview frame
    movie_preview =Frame(movie_archive_preview,relief='flat',bg = gui_color)
    movie_preview.grid(row=1, column=1)

    #homepage Icon picture
    image = tk.PhotoImage(file='images\cinema.gif')
    label = tk.Label(movie_archive_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0,sticky='e' )
    top_one_list =tk.Label(movie_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(movie_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(movie_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(movie_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(movie_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(movie_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(movie_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(movie_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(movie_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(movie_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')

    
# Current Box Movie chart

def movie_chart_current_export():

    
    
        movie_chart_file = open('movie_chart_current_export.html','w')
        movie_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Currently Trending In Cinemas </title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            <title> What's Currently Trending In Cinemas </title>
            </style>   
            </head>
            <body>
        ''')
        
        movie_chart_page = urlopen(url_movie_chart)
        html_code = movie_chart_page.read().decode("UTF-8")
        movie_chart_page.close()


    # Heading for Current Movie Chart
        movie_heading_tag = '<a href="/daily/">Daily Box Office</a>'
        movie_heading = findall(movie_heading_tag,html_code)
        fixed_movie_heading = re.sub('\[\'<a href="/daily/">',"",str(movie_heading))
        fixed_movie_heading = re.sub('</a>\'\]',"",str(fixed_movie_heading))
        movie_update_tag = '<div style="float: right">(\w*\d*.*)<'
        movie_update = findall(movie_update_tag, html_code)
        fixed_movie_update = re.sub('\[\'',"",str(movie_update))
        fixed_movie_update = re.sub('\'\]',"",str(fixed_movie_update))
    #movie daily date for gross numbers
        movie_date_tag = '<a href="/daily/chart/\?sortdate=\d+-\d+-\d+&p=.htm">[<u>]*(\w+)<br>'
        movie_date = findall(movie_date_tag, html_code)

        movie_date_one = movie_date[0]
        movie_date_two = movie_date[1]
        movie_date_three = movie_date[2]
        movie_date_four= movie_date[3]
        
    #print(fixed_movie_date)

        movie_chart_file.write('<h1 align= "center">'+
                               fixed_movie_heading +'</h1>'

                               '<h2 align= "center">'+ fixed_movie_update+'</h2>')

    
        # top 10 movie charts in cinemas
        movie_list = findall('<a href="/movies/\?page=daily&id=\w*\d*.htm">([.*:;\'A-Z0-9\s]*[\(0-9)\]]*)',html_code)
        top_one = movie_list[0]
        top_two = movie_list[1]
        top_three = movie_list[2]
        top_four = movie_list[3]
        top_five = movie_list[4]
        top_six = movie_list[5]
        top_seven = movie_list[6]
        top_eight = movie_list[7]
        top_nine = movie_list[8]
        top_ten = movie_list[9]

        


    # movie studio
        movie_studio = findall('studio=\w*\d*.htm">(\w*\d*.*)</a>'
                               ,html_code)
        
        studio_one = movie_studio[0]
        studio_two = movie_studio[1]
        studio_three = movie_studio[2]
        studio_four = movie_studio[3]
        studio_five = movie_studio[4]
        studio_six = movie_studio[5]
        studio_seven = movie_studio[6]
        studio_eight = movie_studio[7]
        studio_nine = movie_studio[8]
        studio_ten = movie_studio[9]
    
    # movie gross earnings
        movie_gross = findall('valign="top">[<b>]*[<br>]*(\$\d+,[\d+,]*|\w+\/\w+)',html_code)
        
    # top one - daily gross
        gross_one = movie_gross[0]
        gross_two = movie_gross[1]
        gross_three = movie_gross[2]
        gross_four = movie_gross[3]
    #top two - daily gross
        gross_five = movie_gross[4]
        gross_six = movie_gross[5]
        gross_seven = movie_gross[6]
        gross_eight = movie_gross[7]
    #top three - daily gross
        gross_nine = movie_gross[8]
        gross_ten = movie_gross[9]
        gross_eleven = movie_gross[10]
        gross_twelve = movie_gross[11]
    #top four - daily gross
        gross_thirteen = movie_gross[12]
        gross_fourteen = movie_gross[13]
        gross_fifteen = movie_gross[14]
        gross_sixteen = movie_gross[15]
    #top five - daily gross
        gross_seventeen = movie_gross[16]
        gross_eighteen = movie_gross[17]
        gross_ninteen = movie_gross[18]
        
        gross_twenty = movie_gross[19]
    #top six - daily gross
        gross_twentyone = movie_gross[20]
        gross_twentytwo = movie_gross[21]
        gross_twentythree = movie_gross[22]
        gross_twentyfour = movie_gross[23]
    #top seven - daily gross
        gross_twentyfive = movie_gross[24]
        gross_twentysix = movie_gross[25]
        gross_twentyseven = movie_gross[26]
        gross_twentyeight = movie_gross[27]
    #top eight - daily gross
        gross_twentynine = movie_gross[28]
        gross_thirty = movie_gross[29]
        gross_thirtyone = movie_gross[30]
        gross_thirtytwo = movie_gross[31]
    #top nine - daily gross
        gross_thirtythree = movie_gross[32]
        gross_thirtyfour = movie_gross[33]
        gross_thirtyfive = movie_gross[34]
        gross_thirtysix = movie_gross[35]
    #top ten - daily gross
        gross_thirtyseven = movie_gross[36]
        gross_thirtyeight = movie_gross[37]
        gross_thirtynine = movie_gross[38]
        gross_forty = movie_gross[39]
        
        movie_chart_file.write('<table align="center"; style="width:40%"><tr>'
                            '<th> </th>'
                            '<th align="center"> Movie </th>'
                            '<th align="center"> Studio </th>'
                            '<th align="center">'+ movie_date_one + " " +'Gross' '</th>'
                            '<th align="center">'+ movie_date_two + " " + 'Gross''</th>'
                            '<th align="center">'+ movie_date_three + " " + 'Gross''</th>'
                            '<th align="center">'+ movie_date_four + " " + 'Gross''</th>'
                               
                               
                          '</tr>'
                          '<tr>'
                              '<td align="center"> 1 </td>'
                          
                             '<td align="center">'+ top_one +'</td>'
                             '<td align="center">'+ studio_one+'</td>'
                             '<td align="center">'+ gross_one +'</td>'
                             '<td align="center">'+ gross_two +'</td>'
                             '<td align="center">'+ gross_three +'</td>'
                             '<td align="center">'+ gross_four +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+top_two+'</td>'
                             '<td align="center">'+ studio_five +'</td>'
                             '<td align="center">'+ gross_five +'</td>'
                             '<td align="center">'+ gross_six +'</td>'
                             '<td align="center">'+ gross_seven +'</td>'
                             '<td align="center">'+ gross_eight +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">3</td>'
                             '<td align="center">'+top_three+'</td>'
                             '<td align="center">'+ studio_three+'</td>'
                             '<td align="center">'+ gross_nine +'</td>'
                             '<td align="center">'+ gross_ten+'</td>'
                             '<td align="center">'+ gross_eleven +'</td>'
                             '<td align="center">'+ gross_twelve +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">4</td>'
                             '<td align="center">'+top_four+'</td>'
                             '<td align="center">'+ studio_four +'</td>'
                             '<td align="center">'+ gross_thirteen +'</td>'
                             '<td align="center">'+ gross_fourteen +'</td>'
                             '<td align="center">'+ gross_fifteen +'</td>'
                             '<td align="center">'+ gross_sixteen +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">5</td>'
                             '<td align="center">'+top_five+'</td>'
                             '<td align="center">'+ studio_five +'</td>'
                             '<td align="center">'+ gross_seventeen +'</td>'
                             '<td align="center">'+ gross_eighteen +'</td>'
                             '<td align="center">'+ gross_ninteen +'</td>'
                             '<td align="center">'+ gross_twenty +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">6</td>'
                             '<td align="center">'+top_six+'</td>'
                             '<td align="center">'+ studio_six +'</td>'
                              '<td align="center">'+ gross_twentyone +'</td>'
                             '<td align="center">'+ gross_twentytwo +'</td>'
                             '<td align="center">'+ gross_twentythree +'</td>'
                             '<td align="center">'+ gross_twentyfour+'</td>'
                          
                           '</tr>'
                         '<tr>'
                             '<td align="center">7</td>'
                             '<td align="center">'+top_seven+'</td>'
                             '<td align="center">'+ studio_seven +'</td>'
                             '<td align="center">'+ gross_twentyfive +'</td>'
                             '<td align="center">'+ gross_twentysix +'</td>'
                             '<td align="center">'+ gross_twentyseven +'</td>'
                             '<td align="center">'+ gross_twentyeight +'</td>'
                             
                           '</tr>'
                         '<tr>'
                             '<td align="center">8</td>'
                             '<td align="center">'+top_eight+'</td>'
                             '<td align="center">'+ studio_eight +'</td>'
                             '<td align="center">'+ gross_twentynine +'</td>'
                             '<td align="center">'+ gross_thirty +'</td>'
                             '<td align="center">'+ gross_thirtyone +'</td>'
                             '<td align="center">'+ gross_thirtytwo +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">9</td>'
                             '<td align="center">'+top_nine+'</td>'
                             '<td align="center">'+ studio_nine +'</td>'
                             '<td align="center">'+ gross_thirtythree +'</td>'
                             '<td align="center">'+ gross_thirtyfour +'</td>'
                             '<td align="center">'+ gross_thirtyfive +'</td>'
                             '<td align="center">'+ gross_thirtysix +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">10</td>'
                             '<td align="center">'+top_ten+'</td>'
                             '<td align="center">'+ studio_ten +'</td>'
                             '<td align="center">'+ gross_thirtyseven +'</td>'
                             '<td align="center">'+ gross_thirtyeight +'</td>'
                             '<td align="center">'+ gross_thirtynine +'</td>'
                             '<td align="center">'+ gross_forty +'</td>'
                         '</table>'
                           )

                                    
    
        movie_chart_file.close()


#Movie chart archive export
def movie_chart_archive_export():

    
    
        movie_chart_file = open('movie_chart_archive_export.html','w')
        movie_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Previously Trending In Cinemas </title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            <title> Previously Trending In Cinemas </title>
            </style>   
            </head>
            <body>
        ''')
        
        movie_chart_page =open('archive\movie_chart_archive.html', encoding = "UTF-8")
        html_code = movie_chart_page.read()
        movie_chart_page.close()


    # Heading for Archive Movie Chart
        movie_heading_tag = '<a href="/daily/">Daily Box Office</a>'
        movie_heading = findall(movie_heading_tag,html_code)
        fixed_movie_heading = re.sub('\[\'<a href="/daily/">',"",str(movie_heading))
        fixed_movie_heading = re.sub('</a>\'\]',"",str(fixed_movie_heading))
        movie_update_tag = '<div style="float: right">(\w*\d*.*)<'
        movie_update = findall(movie_update_tag, html_code)
        fixed_movie_update = re.sub('\[\'',"",str(movie_update))
        fixed_movie_update = re.sub('\'\]',"",str(fixed_movie_update))
    #movie daily date for gross numbers
        movie_date_tag = '<a href="/daily/chart/\?sortdate=\d+-\d+-\d+&p=.htm">[<u>]*(\w+)<br>'
        movie_date = findall(movie_date_tag, html_code)

        movie_date_one = movie_date[0]
        movie_date_two = movie_date[1]
        movie_date_three = movie_date[2]
        movie_date_four= movie_date[3]
        
    #print(fixed_movie_date)

        movie_chart_file.write('<h1 align= "center">'+
                               fixed_movie_heading +'</h1>'

                               '<h2 align= "center">'+ fixed_movie_update+'</h2>')

    # top 10 movie charts in cinemas
        movie_list = findall('<a href="/movies/\?page=daily&id=\w*\d*.htm">([.*:;\'A-Z0-9\s]*[\(0-9)\]]*)',html_code)
        top_one = movie_list[0]
        top_two = movie_list[1]
        top_three = movie_list[2]
        top_four = movie_list[3]
        top_five = movie_list[4]
        top_six = movie_list[5]
        top_seven = movie_list[6]
        top_eight = movie_list[7]
        top_nine = movie_list[8]
        top_ten = movie_list[9]


    # movie studio
        movie_studio = findall('studio=\w*\d*.htm">(\w*\d*.*)</a>'
                               ,html_code)
        
        studio_one = movie_studio[0]
        studio_two = movie_studio[1]
        studio_three = movie_studio[2]
        studio_four = movie_studio[3]
        studio_five = movie_studio[4]
        studio_six = movie_studio[5]
        studio_seven = movie_studio[6]
        studio_eight = movie_studio[7]
        studio_nine = movie_studio[8]
        studio_ten = movie_studio[9]
    
    # movie gross earnings
        movie_gross = findall('valign="top">[<b>]*(\$\d+,[\d+,]*)',html_code)
    # top one - daily gross
        gross_one = movie_gross[0]
        gross_two = movie_gross[1]
        gross_three = movie_gross[2]
        gross_four = movie_gross[3]
    #top two - daily gross
        gross_five = movie_gross[4]
        gross_six = movie_gross[5]
        gross_seven = movie_gross[6]
        gross_eight = movie_gross[7]
    #top three - daily gross
        gross_nine = movie_gross[8]
        gross_ten = movie_gross[9]
        gross_eleven = movie_gross[10]
        gross_twelve = movie_gross[11]
    #top four - daily gross
        gross_thirteen = movie_gross[12]
        gross_fourteen = movie_gross[13]
        gross_fifteen = movie_gross[14]
        gross_sixteen = movie_gross[15]
    #top five - daily gross
        gross_seventeen = movie_gross[16]
        gross_eighteen = movie_gross[17]
        gross_ninteen = movie_gross[18]
        gross_twenty = movie_gross[19]
    #top six - daily gross
        gross_twentyone = movie_gross[20]
        gross_twentytwo = movie_gross[21]
        gross_twentythree = movie_gross[22]
        gross_twentyfour = movie_gross[23]
    #top seven - daily gross
        gross_twentyfive = movie_gross[24]
        gross_twentysix = movie_gross[25]
        gross_twentyseven = movie_gross[26]
        gross_twentyeight = movie_gross[27]
    #top eight - daily gross
        gross_twentynine = movie_gross[28]
        gross_thirty = movie_gross[29]
        gross_thirtyone = movie_gross[30]
        gross_thirtytwo = movie_gross[31]
    #top nine - daily gross
        gross_thirtythree = movie_gross[32]
        gross_thirtyfour = movie_gross[33]
        gross_thirtyfive = movie_gross[34]
        gross_thirtysix = movie_gross[35]
    #top ten - daily gross
        gross_thirtyseven = movie_gross[36]
        gross_thirtyeight = movie_gross[37]
        gross_thirtynine = movie_gross[38]
        gross_forty = movie_gross[39]
    
        movie_chart_file.write('<table align="center"; style="width:40%"><tr>'
                            '<th> </th>'
                            '<th align="center"> Movie </th>'
                            '<th align="center"> Studio </th>'
                            '<th align="center">'+ movie_date_one + " " +'Gross' '</th>'
                            '<th align="center">'+ movie_date_two + " " + 'Gross''</th>'
                            '<th align="center">'+ movie_date_three + " " + 'Gross''</th>'
                            '<th align="center">'+ movie_date_four + " " + 'Gross''</th>'
                               
                               
                          '</tr>'
                          '<tr>'
                              '<td align="center"> 1 </td>'
                          
                             '<td align="center">'+ top_one +'</td>'
                             '<td align="center">'+ studio_one+'</td>'
                             '<td align="center">'+ gross_one +'</td>'
                             '<td align="center">'+ gross_two +'</td>'
                             '<td align="center">'+ gross_three +'</td>'
                             '<td align="center">'+ gross_four +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+top_two+'</td>'
                             '<td align="center">'+ studio_five +'</td>'
                             '<td align="center">'+ gross_five +'</td>'
                             '<td align="center">'+ gross_six +'</td>'
                             '<td align="center">'+ gross_seven +'</td>'
                             '<td align="center">'+ gross_eight +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">3</td>'
                             '<td align="center">'+top_three+'</td>'
                             '<td align="center">'+ studio_three+'</td>'
                             '<td align="center">'+ gross_nine +'</td>'
                             '<td align="center">'+ gross_ten+'</td>'
                             '<td align="center">'+ gross_eleven +'</td>'
                             '<td align="center">'+ gross_twelve +'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">4</td>'
                             '<td align="center">'+top_four+'</td>'
                             '<td align="center">'+ studio_four +'</td>'
                             '<td align="center">'+ gross_thirteen +'</td>'
                             '<td align="center">'+ gross_fourteen +'</td>'
                             '<td align="center">'+ gross_fifteen +'</td>'
                             '<td align="center">'+ gross_sixteen +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">5</td>'
                             '<td align="center">'+top_five+'</td>'
                             '<td align="center">'+ studio_five +'</td>'
                             '<td align="center">'+ gross_seventeen +'</td>'
                             '<td align="center">'+ gross_eighteen +'</td>'
                             '<td align="center">'+ gross_ninteen +'</td>'
                             '<td align="center">'+ gross_twenty +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">6</td>'
                             '<td align="center">'+top_six+'</td>'
                             '<td align="center">'+ studio_six +'</td>'
                              '<td align="center">'+ gross_twentyone +'</td>'
                             '<td align="center">'+ gross_twentytwo +'</td>'
                             '<td align="center">'+ gross_twentythree +'</td>'
                             '<td align="center">'+ gross_twentyfour+'</td>'
                          
                           '</tr>'
                         '<tr>'
                             '<td align="center">7</td>'
                             '<td align="center">'+top_seven+'</td>'
                             '<td align="center">'+ studio_seven +'</td>'
                             '<td align="center">'+ gross_twentyfive +'</td>'
                             '<td align="center">'+ gross_twentysix +'</td>'
                             '<td align="center">'+ gross_twentyseven +'</td>'
                             '<td align="center">'+ gross_twentyeight +'</td>'
                             
                           '</tr>'
                         '<tr>'
                             '<td align="center">8</td>'
                             '<td align="center">'+top_eight+'</td>'
                             '<td align="center">'+ studio_eight +'</td>'
                             '<td align="center">'+ gross_twentynine +'</td>'
                             '<td align="center">'+ gross_thirty +'</td>'
                             '<td align="center">'+ gross_thirtyone +'</td>'
                             '<td align="center">'+ gross_thirtytwo +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">9</td>'
                             '<td align="center">'+top_nine+'</td>'
                             '<td align="center">'+ studio_nine +'</td>'
                             '<td align="center">'+ gross_thirtythree +'</td>'
                             '<td align="center">'+ gross_thirtyfour +'</td>'
                             '<td align="center">'+ gross_thirtyfive +'</td>'
                             '<td align="center">'+ gross_thirtysix +'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">10</td>'
                             '<td align="center">'+top_ten+'</td>'
                             '<td align="center">'+ studio_ten +'</td>'
                             '<td align="center">'+ gross_thirtyseven +'</td>'
                             '<td align="center">'+ gross_thirtyeight +'</td>'
                             '<td align="center">'+ gross_thirtynine +'</td>'
                             '<td align="center">'+ gross_forty +'</td>'
                         '</table>'
                           )

                                    
    
        movie_chart_file.close()
#mobile game current preview
def game_current_preview():
    game_chart_page = urlopen(url_game_chart)
    html_code = game_chart_page.read().decode("UTF-8")
    game_chart_page.close()
    # Current game Chart
    game_chart_tag = '<a class="App-Teaser__link" href="/app-sales-data/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\,*\:*\;*\w*\™*]*)</a>'
    game_chart = findall(game_chart_tag, html_code)
    top_one = game_chart[0]
    top_two = game_chart[1]
    top_three = game_chart[2]
    top_four = game_chart[3]
    top_five = game_chart[4]
    top_six = game_chart[5]
    top_seven = game_chart[6]
    top_eight = game_chart[7]
    top_nine = game_chart[8]
    top_ten = game_chart[9]

    game_current_preview = tk.Toplevel(the_window)
    game_current_preview.configure(bg = gui_color)
    game_current_preview.title('Current Game Trends Preview')    
    gametrendlabel = Label(game_current_preview, text = "Current Game Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    gametrendlabel.grid(row=0,column=1)
    #game preview frame
    game_preview =Frame(game_current_preview,relief='flat',bg = gui_color)
    game_preview.grid(row=1, column=1)

    #homepage Icon picture
    image = tk.PhotoImage(file='images\smartphone.gif')
    label = tk.Label(game_current_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0,sticky='e' )
    top_one_list =tk.Label(game_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(game_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(game_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(game_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(game_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(game_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(game_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(game_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(game_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(game_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')
#mobile game archive preview

def game_archive_preview():
    game_chart_page = open('archive\game_chart_archive.html',encoding='UTF-8')
    html_code = game_chart_page.read()
    game_chart_page.close()
    # previous game Chart
    game_chart_tag = '<a class="App-Teaser__link" href="/app-sales-data/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\,*\:*\;*\w*\™*]*)</a>'
    game_chart = findall(game_chart_tag, html_code)
    top_one = game_chart[0]
    top_two = game_chart[1]
    top_three = game_chart[2]
    top_four = game_chart[3]
    top_five = game_chart[4]
    top_six = game_chart[5]
    top_seven = game_chart[6]
    top_eight = game_chart[7]
    top_nine = game_chart[8]
    top_ten = game_chart[9]

    game_archive_preview = tk.Toplevel(the_window)
    game_archive_preview.configure(bg = gui_color)
    game_archive_preview.title('Previous Game Trends Preview')    
    gametrendlabel = Label(game_archive_preview, text = "Previous Game Trends",font = ('system 10 points', 30)
                              ,bg = gui_color, fg = 'Black')
    gametrendlabel.grid(row=0,column=1)
    #game preview frame
    game_preview =Frame(game_archive_preview,relief='flat',bg = gui_color)
    game_preview.grid(row=1, column=1)

    #homepage Icon picture
    image = tk.PhotoImage(file='images\smartphone.gif')
    label = tk.Label(game_archive_preview,image=image,bg = gui_color)
    label.image = image # keep a reference!
    label.grid(row=1,column=0,sticky='e' )
    top_one_list =tk.Label(game_preview, text='[1]' + str(top_one),bg = gui_color)
    top_one_list.grid(row=0,column=2,sticky='w')
    top_two_list = tk.Label(game_preview,text='[2]' + str(top_two),bg = gui_color)
    top_two_list.grid(row=1,column=2, sticky='w')
    top_three_list=tk.Label(game_preview, text ='[3]' + str(top_three),bg = gui_color)
    top_three_list.grid(row= 2,column=2,sticky='w')
    top_four_list=tk.Label(game_preview,text ='[4]' + str(top_four),bg = gui_color)
    top_four_list.grid(row=3,column=2,sticky='w')
    top_five_list=tk.Label(game_preview,text='[5]'+str(top_five),bg = gui_color)
    top_five_list.grid(row=4,column=2,sticky='w')
    top_six_list=tk.Label(game_preview,text='[6]'+str(top_six),bg = gui_color)
    top_six_list.grid(row=5,column=2,sticky='w')
    top_seven_list=tk.Label(game_preview,text='[7]'+str(top_seven),bg = gui_color)
    top_seven_list.grid(row=6,column=2,sticky='w')
    top_eight_list=tk.Label(game_preview,text='[8]'+str(top_eight),bg = gui_color)
    top_eight_list.grid(row=7,column=2,sticky='w')
    top_nine_list=tk.Label(game_preview,text='[9]'+str(top_nine),bg = gui_color)
    top_nine_list.grid(row=8,column=2,sticky='w')
    top_ten_list=tk.Label(game_preview,text='[10]'+str(top_ten),bg = gui_color)
    top_ten_list.grid(row=9,column=2,sticky='w')
    




# Mobile Game Top 10 Chart
def game_current_export():
    game_chart_file = open('game_chart_current_export.html','w')
    game_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Currently Trending Mobile Games </title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            </style>   
            </head>
            <body>
        ''')
        
    game_chart_page = urlopen(url_game_chart)
    html_code = game_chart_page.read().decode("UTF-8")
    game_chart_page.close()

    # heading for game chart html page
    # Heading for Archive Game Chart
    game_heading_tag = 'span5">([\w+\s+]*- Games)'
    game_heading = findall(game_heading_tag,html_code)
    fixed_game_heading= re.sub('\[\'',"",str(game_heading))
    fixed_game_heading= re.sub('\'\]',"",str(fixed_game_heading))
                            
    
    game_chart_file.write('<h1 align = "center">'+ str(fixed_game_heading) + '</h1>')


    # game chart top 10
    game_chart_tag = '<a class="App-Teaser__link" href="/app-sales-data/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\,*\:*\;*\w*\™*]*)</a>'
    game_chart = findall(game_chart_tag, html_code)
    game_one = game_chart[0]
    game_two = game_chart[1]
    game_three = game_chart[2]
    game_four = game_chart[3]
    game_five = game_chart[4]
    game_six = game_chart[5]
    game_seven = game_chart[6]
    game_eight = game_chart[7]
    game_nine = game_chart[8]
    game_ten = game_chart[9]

    #game publisher
    game_publisher_tag='<td class="info table-data table-data-publisher"><a href="/app-sales-data/publisher/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\:*\;*\,*\w*\™*]*)</a>'
    game_publisher = findall(game_publisher_tag,html_code)
    publisher_one = game_publisher[0]
    publisher_two = game_publisher[1]
    publisher_three = game_publisher[2]
    publisher_four = game_publisher[3]
    publisher_five = game_publisher[4]
    publisher_six = game_publisher[5]
    publisher_seven = game_publisher[6]
    publisher_eight = game_publisher[7]
    publisher_nine = game_publisher[8]
    publisher_ten = game_publisher[9]

    #Game Price
    game_price_tag ='<td class="info table-data table-data-price">(\$*\d*\.*\w*)</td>'
    game_price = findall(game_price_tag, html_code)
    price_one = game_price[0]
    price_two = game_price[1]
    price_three = game_price[2]
    price_four = game_price[3]
    price_five = game_price[4]
    price_six = game_price[5]
    price_seven = game_price[6]
    price_eight = game_price[7]
    price_nine = game_price[8]
    price_ten = game_price[9]

    #game revenue
    game_revenue_tag = '<td class="table-data table-data-revenue">(\$[\d*\,*]*)</td>'
    game_revenue = findall(game_revenue_tag,html_code)
    rev_one = game_revenue[0]
    rev_two = game_revenue[1]
    rev_three= game_revenue[2]
    rev_four= game_revenue[3]
    rev_five = game_revenue[4]
    rev_six= game_revenue[5]
    rev_seven= game_revenue[6]
    rev_eight= game_revenue[7]
    rev_nine= game_revenue[8]
    rev_ten= game_revenue[9]

    #game new installs
    game_install_tag = '<td class="table-data table-data-installs_new">([\d*\,*]*)</td>'
    game_install = findall(game_install_tag,html_code)
    install_one = game_install[0]
    install_two = game_install[1]
    install_three = game_install[2]
    install_four = game_install[3]
    install_five = game_install[4]
    install_six= game_install[5]
    install_seven = game_install[6]
    install_eight = game_install[7]
    install_nine = game_install[8]
    install_ten = game_install[9]
    



    game_chart_file.write('''<table align="center"; style="width:40%">
                          <tr>
                              <th> </th>
                              <th align="center"> Title </th>
                              <th align="center"> Publisher </th>
                              <th align="center"> Price </th>
                              <th align="center"> Revenue </th>
                              <th align="center" title = " Installs during the day, exludes reinstalls"> New Installs</th>
                          </tr>
                          <tr>
                              <td align="center"> 1 </td>
                          '''
                             '<td align="center">'+ game_one +'</td>'
                             '<td align="center">'+ publisher_one+'</td>'
                             '<td align="center">'+price_one+'</td>'
                             '<td align="center">'+rev_one+'</td>'
                             '<td align="center">'+install_one+'</td>'
                          
                         '</tr>'
                         '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+ game_two+'</td>'
                             '<td align="center">'+publisher_two+'</td>'
                             '<td align="center">'+price_two+'</td>'
                             '<td align="center">'+rev_two+'</td>'
                             '<td align="center">'+install_two+'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">3</td>'
                             '<td align="center">'+game_three+'</td>'
                             '<td align="center">'+publisher_three+'</td>'
                             '<td align="center">'+price_three+'</td>'
                             '<td align="center">'+rev_three+'</td>'
                             '<td align="center">'+install_three+'</td>'
                        '</tr>'
                         '<tr>'
                             '<td align="center">4</td>'
                             '<td align="center">'+game_four+'</td>'
                             '<td align="center">'+publisher_four+'</td>'
                             '<td align="center">'+price_four+'</td>'
                             '<td align="center">'+rev_four+'</td>'
                             '<td align="center">'+install_four+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">5</td>'
                             '<td align="center">'+game_five+'</td>'
                             '<td align="center">'+publisher_five+'</td>'
                             '<td align="center">'+price_five+'</td>'
                             '<td align="center">'+rev_five+'</td>'
                             '<td align="center">'+install_five+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">6</td>'
                             '<td align="center">'+game_six+'</td>'
                             '<td align="center">'+publisher_six+'</td>'
                             '<td align="center">'+price_six+'</td>'
                             '<td align="center">'+rev_six+'</td>'
                             '<td align="center">'+install_six+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">7</td>'
                             '<td align="center">'+game_seven+'</td>'
                             '<td align="center">'+publisher_seven+'</td>'
                             '<td align="center">'+price_seven+'</td>'
                             '<td align="center">'+rev_seven+'</td>'
                             '<td align="center">'+install_seven+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">8</td>'
                             '<td align="center">'+game_eight+'</td>'
                             '<td align="center">'+publisher_eight+'</td>'
                             '<td align="center">'+price_eight+'</td>'
                             '<td align="center">'+rev_eight+'</td>'
                             '<td align="center">'+install_eight+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">9</td>'
                             '<td align="center">'+game_nine+'</td>'
                             '<td align="center">'+publisher_nine+'</td>'
                             '<td align="center">'+price_nine+'</td>'
                             '<td align="center">'+rev_nine+'</td>'
                             '<td align="center">'+install_nine+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">10</td>'
                             '<td align="center">'+game_ten+'</td>'
                             '<td align="center">'+publisher_ten+'</td>'
                             '<td align="center">'+price_ten+'</td>'
                             '<td align="center">'+rev_ten+'</td>'
                             '<td align="center">'+install_ten+'</td>'
                           )
# Mobile Game Archived Top 10 Chart
def game_archive_export():
    game_chart_file = open('game_chart_archive_export.html','w')
    game_chart_file.write('''<!DOCTYPE html>
        <html>
            <head>
                <title>Previously Trending Mobile Games </title>
            <style>
            table,th,td{
                border: 1px solid black;
                }
            </style>   
            </head>
            <body>
        ''')
        
    game_chart_page = open('archive\game_chart_archive.html',encoding='UTF-8')
    html_code = game_chart_page.read()
    game_chart_page.close()

    # heading for game chart html page
    # Heading for Archive Game Chart
    game_heading_tag = 'span5">([\w+\s+]*- Games)'
    game_heading = findall(game_heading_tag,html_code)
    fixed_game_heading= re.sub('\[\'',"",str(game_heading))
    fixed_game_heading= re.sub('\'\]',"",str(fixed_game_heading))
                            
    
    game_chart_file.write('<h1 align = "center">'+ str(fixed_game_heading) + '</h1>')


    # game chart top 10
    game_chart_tag = '<a class="App-Teaser__link" href="/app-sales-data/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\,*\:*\;*\w*\™*]*)</a>'
    game_chart = findall(game_chart_tag, html_code)
    game_one = game_chart[0]
    game_two = game_chart[1]
    game_three = game_chart[2]
    game_four = game_chart[3]
    game_five = game_chart[4]
    game_six = game_chart[5]
    game_seven = game_chart[6]
    game_eight = game_chart[7]
    game_nine = game_chart[8]
    game_ten = game_chart[9]

    #game publisher
    game_publisher_tag='<td class="info table-data table-data-publisher"><a href="/app-sales-data/publisher/\d*/[\w*\-*]*/">([\w*\d]*[\s*\.*\:*\;*\,*\w*\™*]*)</a>'
    game_publisher = findall(game_publisher_tag,html_code)
    publisher_one = game_publisher[0]
    publisher_two = game_publisher[1]
    publisher_three = game_publisher[2]
    publisher_four = game_publisher[3]
    publisher_five = game_publisher[4]
    publisher_six = game_publisher[5]
    publisher_seven = game_publisher[6]
    publisher_eight = game_publisher[7]
    publisher_nine = game_publisher[8]
    publisher_ten = game_publisher[9]

    #Game Price
    game_price_tag ='<td class="info table-data table-data-price">(\$*\d*\.*\w*)</td>'
    game_price = findall(game_price_tag, html_code)
    price_one = game_price[0]
    price_two = game_price[1]
    price_three = game_price[2]
    price_four = game_price[3]
    price_five = game_price[4]
    price_six = game_price[5]
    price_seven = game_price[6]
    price_eight = game_price[7]
    price_nine = game_price[8]
    price_ten = game_price[9]

    #game revenue
    game_revenue_tag = '<td class="table-data table-data-revenue">(\$[\d*\,*]*)</td>'
    game_revenue = findall(game_revenue_tag,html_code)
    rev_one = game_revenue[0]
    rev_two = game_revenue[1]
    rev_three= game_revenue[2]
    rev_four= game_revenue[3]
    rev_five = game_revenue[4]
    rev_six= game_revenue[5]
    rev_seven= game_revenue[6]
    rev_eight= game_revenue[7]
    rev_nine= game_revenue[8]
    rev_ten= game_revenue[9]

    #game new installs
    game_install_tag = '<td class="table-data table-data-installs_new">([\d*\,*]*)</td>'
    game_install = findall(game_install_tag,html_code)
    install_one = game_install[0]
    install_two = game_install[1]
    install_three = game_install[2]
    install_four = game_install[3]
    install_five = game_install[4]
    install_six= game_install[5]
    install_seven = game_install[6]
    install_eight = game_install[7]
    install_nine = game_install[8]
    install_ten = game_install[9]
    



    game_chart_file.write('''<table align="center"; style="width:40%">
                          <tr>
                              <th> </th>
                              <th align="center"> Title </th>
                              <th align="center"> Publisher </th>
                              <th align="center"> Price </th>
                              <th align="center"> Revenue </th>
                              <th align="center" title = " Installs during the day, exludes reinstalls"> New Installs </th>
                          </tr>
                          <tr>
                              <td align="center"> 1 </td>
                          '''
                             '<td align="center">'+ game_one +'</td>'
                             '<td align="center">'+ publisher_one+'</td>'
                             '<td align="center">'+price_one+'</td>'
                             '<td align="center">'+rev_one+'</td>'
                             '<td align="center">'+install_one+'</td>'
                          
                         '</tr>'
                         '<tr>'
                             '<td align="center">2</td>'
                             '<td align="center">'+ game_two+'</td>'
                             '<td align="center">'+publisher_two+'</td>'
                             '<td align="center">'+price_two+'</td>'
                             '<td align="center">'+rev_two+'</td>'
                             '<td align="center">'+install_two+'</td>'
                         '</tr>'
                         '<tr>'
                             '<td align="center">3</td>'
                             '<td align="center">'+game_three+'</td>'
                             '<td align="center">'+publisher_three+'</td>'
                             '<td align="center">'+price_three+'</td>'
                             '<td align="center">'+rev_three+'</td>'
                             '<td align="center">'+install_three+'</td>'
                        '</tr>'
                         '<tr>'
                             '<td align="center">4</td>'
                             '<td align="center">'+game_four+'</td>'
                             '<td align="center">'+publisher_four+'</td>'
                             '<td align="center">'+price_four+'</td>'
                             '<td align="center">'+rev_four+'</td>'
                             '<td align="center">'+install_four+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">5</td>'
                             '<td align="center">'+game_five+'</td>'
                             '<td align="center">'+publisher_five+'</td>'
                             '<td align="center">'+price_five+'</td>'
                             '<td align="center">'+rev_five+'</td>'
                             '<td align="center">'+install_five+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">6</td>'
                             '<td align="center">'+game_six+'</td>'
                             '<td align="center">'+publisher_six+'</td>'
                             '<td align="center">'+price_six+'</td>'
                             '<td align="center">'+rev_six+'</td>'
                             '<td align="center">'+install_six+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">7</td>'
                             '<td align="center">'+game_seven+'</td>'
                             '<td align="center">'+publisher_seven+'</td>'
                             '<td align="center">'+price_seven+'</td>'
                             '<td align="center">'+rev_seven+'</td>'
                             '<td align="center">'+install_seven+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">8</td>'
                             '<td align="center">'+game_eight+'</td>'
                             '<td align="center">'+publisher_eight+'</td>'
                             '<td align="center">'+price_eight+'</td>'
                             '<td align="center">'+rev_eight+'</td>'
                             '<td align="center">'+install_eight+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">9</td>'
                             '<td align="center">'+game_nine+'</td>'
                             '<td align="center">'+publisher_nine+'</td>'
                             '<td align="center">'+price_nine+'</td>'
                             '<td align="center">'+rev_nine+'</td>'
                             '<td align="center">'+install_nine+'</td>'
                           '</tr>'
                         '<tr>'
                             '<td align="center">10</td>'
                             '<td align="center">'+game_ten+'</td>'
                             '<td align="center">'+publisher_ten+'</td>'
                             '<td align="center">'+price_ten+'</td>'
                             '<td align="center">'+rev_ten+'</td>'
                             '<td align="center">'+install_ten+'</td>'
                           )
    

    
#interactive gui 
def export_action():
    if music_current_button.get() == 1:
        music_chart_current_export()
    if music_previous_button.get()==1:
        music_previous_export()
    if movies_current_button.get() == 1:
        movie_chart_archive_export()
    if movies_previous_button.get()==1:
        movie_chart_archive_export()
    if games_current_button.get() ==1:
        game_current_export()
    if games_previous_button.get()==1:
        game_archive_export()
def preview_action():
    if music_current_button.get() == 1:
        music_current_preview()
    if music_previous_button.get()==1:
        music_archive_preview()
    if movies_current_button.get() == 1:
        movie_current_preview()
    if movies_previous_button.get()==1:
        movie_archive_preview()
    if games_current_button.get() ==1:
        game_current_preview()
    if games_previous_button.get()==1:
        game_archive_preview()

#buttons for previewing and extractiong
action_button_preview = Button(action_frame, text = 'Preview',command = preview_action,bg = gui_color, pady = 20, padx = 70)
action_button_preview.grid(row = 0, column = 0)
action_button_export = Button(action_frame_two, text = 'Export', command = export_action, bg = gui_color,pady = 20,
                              padx = 70)
action_button_export.grid(row = 0, column = 20)
        


##
##

##### DEVELOP YOUR SOLUTION HERE #####
pass
