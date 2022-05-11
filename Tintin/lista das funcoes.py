# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:03:14 2020

@author: hugom
"""
"""

Lista de funcoes 

Binance data

velas - a = simbolo / tira as velas de um periodo de tempo para tras
ordens - a = simbolo / tira as ultimas ordens / max-500

Matplot

chartplot - a = simbolo , (p1, p2, p3) = desenho no grafico / desenha grafico da funcao velas tiradas com indicadores(variavel p )

Moving Average

movingaverage - a = simbolo / tira as moving averages da funcao velas

Divergencia

divrsi/divmacd - price - preco que o script analisa , ind - indicador ,nome - simbolo, time - horas das velas tiradas , velas_atras - quantidade de velas para tras que o script analisa

Indicadores

indicadores - o - open, c - close, h - high, l - low / tira os indicadores da funcao velas

Padroes

padroes - o - open, c - close, h - high, l - low / tira os padroes da funcao velas
padroestime - lista - lista a analisar,opentime_lista ,closetime_lista/ pega numa lista e onde acontece algo(result) tira o closetime e opentime desse momento. 
padroestimeresult - (padrao, opentime, closetime) = padroestime ,a = simbolo ,b - quantidade de minutos para tras,volumesantigos2 - funcao volumesantigos2 / junta a funcao volumes antigos e padroestime e faz print dos tempos do acontecimento

Previousvolumes

volumesantigos - opentime, closetime , a = symbolo/ vai buscar as ordens do opentime ate closetime e organiza por total, buy e sell
volumesantigos2 - opentime, closetime, a, minutos - minutos para ir buscar para tras do (opentime/closetime)/ o mesmo que volumes antigos mas vai buscar todos os minutos para tras

Juncao

start / comeca a funcao chamada 

















