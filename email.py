import os
import smtplib
import email.mime.text
import MIMEText

#Aqui é a biblioteca que vai ser usada para enviar o email, a biblioteca smtplib é a biblioteca que vai fazer a conexão com o servidor do gmail e enviar o email, e a biblioteca email.mime.text é a biblioteca que vai montar a mensagem do email.

#configurações

Remetente = 'meuemail@gmail.com' #O seu email que vai enviar a mensagem
senha = 'minhasenha' # A sua senha do email que vai enviar a mensagem
Destinatario = 'Destinatario@gmail.com' #O email do destinatario que vai receber a mensagem

#Montando a mensagem

mensagem = MIMEText('Ola, criei um script em python que envia email automaticamente! e tambem explicando passo a passo como fazer isso!') #Isso é o corpo a mensagem do email 

mensagem['subject'] = 'Email automatico com python' #Isso é o assunto do email 

mensagem['from'] = Remetente #Isso é o remetente do email ( este é o email que vai enviar a mensagem)
mensagem['to'] = Destinatario #Isso é o destinatario do email (este é o email que vai receber a mensagem)

#conectando a mensagem

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: #iniciando a conexão com o servidor do gmail, e a porta 465 é a porta de envio de email do gmail
# O with é usado para garantir que a conexão seja fechada corretamente após o envio do email, mesmo que ocorra algum erro durante o processo.
    server.login(Remetente, senha) #Vai logar no email do remetente para enviar a mensagem
    server.send_message(mensagem) #Vai pegar a sua mensagem e enviar para o destinatario

print('Email enviado com sucesso!')