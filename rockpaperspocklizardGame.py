{\rtf1\ansi\ansicpg1252\cocoartf1187\cocoasubrtf340
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 # Rock-paper-scissors-lizard-Spock template\
\
import random\
\
# The key idea of this program is to equate the strings\
# "rock", "paper", "scissors", "lizard", "Spock" to numbers\
# as follows:\
#\
# 0 - rock\
# 1 - Spock\
# 1 - paper\
# 3 - lizard\
# 4 - scissors\
\
# helper functions\
def number_to_name(number):\
    \
    # fill in your code below\
    \
    if number == 0:\
        name = "ROCK"\
    elif number == 1:\
        name = "SPOCK"\
    elif number == 2:\
        name = "PAPER"\
    elif number == 3:\
        name = "LIZARD"\
    else:\
        name = " "\
    return name\
    \
    # convert number to a name using if/elif/else\
    # don't forget to return the result!\
\
    \
def name_to_number(name):\
    # fill in your code below\
    if name == "ROCK":\
        number = 0\
    elif name == "SPOCK":\
        number = 1\
    elif name == "PAPER":\
        number = 2\
    elif name == "LIZARD":\
        number = 3\
    else:\
        number = 4\
    return number\
    # convert name to number using if/elif/else\
    # don't forget to return the result!\
\
\
def rpsls(name): \
    # fill in your code below\
    \
    # convert name to player_number using name_to_number\
    player_number = name_to_number(name)\
    \
    # compute random guess for comp_number using random.randrange()\
    comp_number = random.randrange(0, 5)\
    \
    # compute difference of player_number and comp_number modulo five\
    winner_player = (player_number - comp_number) % 5\
    \
    # use if/elif/else to determine winner\
    \
    # convert comp_number to name using number_to_name\
    \
    #comp_number = number_to_name(name)\
    \
    # print results\
    print " "\
    print "Players Choose:", name, player_number\
    print "Computer Choose:", number_to_name(comp_number), comp_number\
    \
    \
    if(comp_number + 1) % 5 == player_number:\
        print "YOU WIN!"\
    elif(comp_number + 2) %5 == player_number:\
        print "YOU WIN!"\
    else:\
        print "Computer Wins, wow you are loser."\
        \
# test your code\
rpsls("ROCK")\
rpsls("SPOCK")\
rpsls("PAPER")\
rpsls("LIZARD")\
rpsls("SCISSORS")\
\
# always remember to check your completed program against the grading rubric\
#for Coursea.org Mini-Project\
\
\
}