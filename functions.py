# -*- coding: utf-8 -*-
import telebot # Library of API bot.
from telebot import types # Types from API bot
import time
import random
import datetime
import codecs
import sys
import json
from os.path import exists
import os
import token
import user
import feedparser
#import owners
#import re
import logging
import commands
import subprocess

TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True

#######################################
#Function for feedparser
#CODE TAKEN FROM:
#https://gist.github.com/Jeshwanth/99cf05f4477ab0161349
def get_feed(url):
    try:
        feed = feedparser.parse(url)
    except:
        return 'Invalid url.'
    y = len(feed[ "items" ])
    y = 5 if y > 5 else y
    if(y < 1):
        return 'Nothing found'
    lines = ['*Feed:*']
    for x in range(y):
        lines.append('- [{}]({})'.format(feed['items'][x]['title'].replace(']', ':').replace('[', '').encode('utf-8'), feed['items'][x]['link']))
    return '\n'.join(lines)
#######################################

#Functions
@bot.message_handler(content_types=['new_chat_members'])
def command_new_user(m):
    cid = m.chat.id
    grupo = m.chat.title
    markup = types.InlineKeyboardMarkup()
    itembtnnormas = types.InlineKeyboardButton("<Click Aquí>", url="https://t.me/shelldevs_es/18")
    markup.row(itembtnnormas)

    if (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} !! A.K.A. @{2} a {3}. Te sugerimos leer las reglas.".format(m.new_chat_member.first_name, m.new_chat_member.last_name, m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido!! @{0} a {1}. No tenés nombres, podrías completar los datos. Te sugerimos leer las reglas en el mensaje anclado.".format(m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado.".format(m.new_chat_member.first_name,m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username != None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! A.K.A. @{1} a {2}. Te sugerimos leer las reglas en el mensaje anclado.".format(m.new_chat_member.last_name,m.new_chat_member.username, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0} {1} a {2}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado.".format(m.new_chat_member.first_name,m.new_chat_member.last_name,grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name == None and m.new_chat_member.last_name != None):
        bot.send_message(cid, "Bienvenido {0}!! a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado.".format(m.new_chat_member.last_name, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)
    elif (m.new_chat_member.username == None and m.new_chat_member.first_name != None and m.new_chat_member.last_name == None):
        bot.send_message(cid, "Bienvenido {0} a {1}. No tenes alias, seria mejor que te crees uno. Te sugerimos tambien leer las reglas en el mensaje anclado.".format(m.new_chat_member.first_name, grupo))
        bot.send_message(cid, "Normas:", reply_markup=markup)

@bot.message_handler(commands=['about'])
def command_acerca(m):
    cid = m.chat.id
    bot.send_message( cid, 'Acerca de @ShellDevGroupBot: Creado por NeoRanger - www.neositelinux.com')

@bot.message_handler(commands=['help'])
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message( cid, "Comandos Disponibles:\n /roll\n /id\n /command_line_tutorial\n /support\n /help\n /about\n /feed\n /neofeed\n") #

@bot.message_handler(commands=['roll'])
def command_roll(m):
    cid = m.chat.id
    bot.send_message( cid, random.randint(1,6) )

@bot.message_handler(commands=['feed'])
def command_feed(m):
    cid = m.chat.id
    url = str(m.text).split(None,1)
    try:
        print (url)
        bot.send_message(cid, get_feed(url[1]),disable_web_page_preview=True,parse_mode="markdown")
    except IndexError:
        bot.send_message( cid, "Missing Argument - Example: /feed http://www.example.com" )

@bot.message_handler(commands=['id'])
def command_id(m):
    cid = m.chat.id
    username = m.from_user.username
    uid = m.from_user.id
    bot.send_message(cid, "You are: @" + str(username)+ " " + "And your Telegram ID is: " + str(uid))

@bot.message_handler(commands=['support'])
def command_help(message):
    markup = types.InlineKeyboardMarkup()
    itembtnneo = types.InlineKeyboardButton('Developer', url="telegram.me/NeoRanger")
    itembtnblog = types.InlineKeyboardButton('URL Blog', url="https://www.neositelinux.com")
    itembtnrepo = types.InlineKeyboardButton('Repo Github', url="http://github.com/neoranger/shelldevbot")
    markup.row(itembtnneo)
    markup.row(itembtnblog)
    markup.row(itembtnrepo)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['neofeed'])
def neo_feed(m):
    cid = m.chat.id
    url = str("https://neositelinux.com/feed.xml")
    print (url)
    bot.send_message(cid, get_feed(url),disable_web_page_preview=True,parse_mode="markdown")

@bot.message_handler(commands=['command_line_tutorial'])
def command_line_tutorial(m):
    cid = m.chat.id
    bot.send_message( cid, 'https://www.youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_A')

###############################################################################
#Specials functions
#def send_message_checking_permission(m, response):
#    cid = m.chat.id
#    uid = m.from_user.id
#    if uid != user.user_id:
#        bot.send_message(cid, "You can't use the bot")
#        return
#    bot.send_message(cid, response)

@bot.message_handler(func=lambda m: True)
def response(m):
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg):
            for t in trg.keys():
                if t.lower() in m.text.lower():
                    bot.reply_to(m, trg[t])
###############################################################################
print('Functions loaded')
