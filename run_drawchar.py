#######################################################################################
# Draw words with drawchar function
# This Module draw 'a' to 'z' letters with the space ' ' for separation, etc
#
# * quit with "q"
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################

from drawchar import draw
from turtle import textinput

#####################################################################
# Input
#####################################################################

words = textinput('- NAME -', 'Enter the words ')
draw(words)