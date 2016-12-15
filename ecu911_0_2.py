#--------------------------------------------------
#
#Bot ECU 911 Release 0 build 2
#
#--------------------------------------------------
import telebot
import psycopg2
import ast
import logging
import json
import urllib.request
import os
from telebot import types

fo = open("token.txt", "r+")
token = fo.read(45);
fo.close()
bot = telebot.TeleBot(token)

#-----CENTROS----
markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('Samborondon')
itembtn2 = types.KeyboardButton('Quito')
itembtn3 = types.KeyboardButton('Cuenca')
markup.add(itembtn1, itembtn2, itembtn3)

def texto_camaras(texto):
	#return [sumT, auxA, auxC, auxM]
	respuesta = [0,0,0,0]
	texto_respuesta = '''No se pudo obtener los datos.
		Favor intentar más tarde.
		'''
	try:
		connect_str = "dbname='TELEGRAM' user='postgres' host='localhost' password='jose.123456'"
		# use our connection values to establish a connection
		conn = psycopg2.connect(connect_str)
		# create a psycopg2 cursor that can execute queries
		cursor = conn.cursor()
		# run a SELECT statement - no data in there, but we can try it
		cursor.execute("""SELECT total, operativas, caidas, mantenimiento FROM camaras WHERE centro = %(centro)s;""",{'centro':texto})
		respuesta = cursor.fetchall()
		print (respuesta)
		texto_respuesta = '''Centro: ''' + texto +'''
			Total de Camaras: ''' + str(respuesta[0][0]) + '''
			Camaras Operativas: ''' + str(respuesta[0][1]) + '''
			Camaras No Operativas: ''' + str(respuesta[0][2]) + '''
			Camaras en Mantenimiento: ''' + str(respuesta[0][3]) +'''
			'''
		#conn.commit()
		cursor.close()
	except Exception as e:
		print(e)
	return (texto_respuesta)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Listado de camaras y fichas.")
	bot.send_message(message.chat.id, "Escoger un centro:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	#print (message)

@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
	pass

@bot.inline_handler(lambda query: query.query == 'camaras')
def query_text(inline_query):
	try:
		sambo = types.InlineQueryResultArticle('1', 'Samborondon', types.InputTextMessageContent(texto_camaras("SAMBORONDON")))
		quito = types.InlineQueryResultArticle('2', 'Quito', types.InputTextMessageContent(texto_camaras("QUITO")))
		cuenca = types.InlineQueryResultArticle('3', 'Cuenca', types.InputTextMessageContent(texto_camaras("CUENCA")))
		ambato = types.InlineQueryResultArticle('4', 'Ambato', types.InputTextMessageContent(texto_camaras("AMBATO")))
		porto = types.InlineQueryResultArticle('5', 'Portoviejo', types.InputTextMessageContent(texto_camaras("PORTOVIEJO")))
		ibarra = types.InlineQueryResultArticle('6', 'Ibarra', types.InputTextMessageContent(texto_camaras("IBARRA")))
		macha = types.InlineQueryResultArticle('7', 'Machala', types.InputTextMessageContent(texto_camaras("MACHALA")))
		esme = types.InlineQueryResultArticle('8', 'Esmeraldas', types.InputTextMessageContent(texto_camaras("ESMERALDAS")))
		tulcan = types.InlineQueryResultArticle('9', 'Tulcan', types.InputTextMessageContent(texto_camaras("TULCAN")))
		nueva = types.InlineQueryResultArticle('10', 'Nueva Loja', types.InputTextMessageContent(texto_camaras("NUEVA LOJA")))
		santo = types.InlineQueryResultArticle('11', 'Santo Domingo', types.InputTextMessageContent(texto_camaras("SANTO DOMINGO")))
		baba = types.InlineQueryResultArticle('12', 'Babahoyo', types.InputTextMessageContent(texto_camaras("BABAHOYO")))
		gala = types.InlineQueryResultArticle('13', 'Galapagos', types.InputTextMessageContent(texto_camaras("GALAPAGOS")))
		macas = types.InlineQueryResultArticle('14', 'Macas', types.InputTextMessageContent(texto_camaras("MACAS")))
		rio = types.InlineQueryResultArticle('15', 'Riobamba', types.InputTextMessageContent(texto_camaras("RIOBAMBA")))
		loja = types.InlineQueryResultArticle('16', 'Loja', types.InputTextMessageContent(texto_camaras("LOJA")))
		bot.answer_inline_query(inline_query.id, [sambo, quito, cuenca, ambato, porto, ibarra, macha, esme, tulcan, nueva, santo, baba, gala, macas, rio, loja])
	except Exception as e:
		print(e)

@bot.inline_handler(lambda query: query.query == 'fichas')
def query_text(inline_query):
	try:
		sambo = types.InlineQueryResultArticle('1', 'Samborondon', types.InputTextMessageContent(imprimir("fichas sambo")))
		quito = types.InlineQueryResultArticle('2', 'Quito', types.InputTextMessageContent(imprimir("fichas quito")))
		cuenca = types.InlineQueryResultArticle('3', 'Cuenca', types.InputTextMessageContent(imprimir("fichas cuenca")))
		ambato = types.InlineQueryResultArticle('4', 'Ambato', types.InputTextMessageContent(imprimir("fichas ambato")))
		porto = types.InlineQueryResultArticle('5', 'Portoviejo', types.InputTextMessageContent(imprimir("fichas porto")))
		ibarra = types.InlineQueryResultArticle('6', 'Ibarra', types.InputTextMessageContent(imprimir("fichas ibarra")))
		macha = types.InlineQueryResultArticle('7', 'Machala', types.InputTextMessageContent(imprimir("fichas macha")))
		esme = types.InlineQueryResultArticle('8', 'Esmeraldas', types.InputTextMessageContent(imprimir("fichas esme")))
		tulcan = types.InlineQueryResultArticle('9', 'Tulcan', types.InputTextMessageContent(imprimir("fichas tulcan")))
		nueva = types.InlineQueryResultArticle('10', 'Nueva Loja', types.InputTextMessageContent(imprimir("fichas nueva")))
		santo = types.InlineQueryResultArticle('11', 'Santo Domingo', types.InputTextMessageContent(imprimir("fichas santo")))
		baba = types.InlineQueryResultArticle('12', 'Babahoyo', types.InputTextMessageContent(imprimir("fichas baba")))
		gala = types.InlineQueryResultArticle('13', 'Galapagos', types.InputTextMessageContent(imprimir("fichas gala")))
		macas = types.InlineQueryResultArticle('14', 'Macas', types.InputTextMessageContent(imprimir("fichas macas")))
		rio = types.InlineQueryResultArticle('15', 'Riobamba', types.InputTextMessageContent(imprimir("fichas rio")))
		loja = types.InlineQueryResultArticle('16', 'Loja', types.InputTextMessageContent(imprimir("fichas loja")))
		bot.answer_inline_query(inline_query.id, [sambo, quito, cuenca, ambato, porto, ibarra, macha, esme, tulcan, nueva, santo, baba, gala, macas, rio, loja])
	except Exception as e:
		print(e)

bot.polling()
