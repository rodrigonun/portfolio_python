#pth_010_site_chatbot.py

#titulo
#in put do chat
#a cada mensagem enviada:
    #mostrar a mensagem
    #enviar essa mensagem para a IA responder
    #aparece na tela a resposta da IA
#streamlit
    #outros: flask, django, outros
    #faz frontend e backend

#dicionario
    #dicionario = {chave1:valor1,chave2:valor2)
        #chave=atributo, valor=registro
    #selecionar 1 elemento do dicionario -> dicionario[chave1] -> output:valor1


    
import streamlit as st
from openai import OpenAI

modelo=OpenAI(api_key=chave)

#escrevendo titulo e ação demandada
st.write("### RNUNES Chatbot")

#memoria do streamlit
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens']=[]
    
#para adicionar uma mensagem
#st.session_state['lista_mensagem'].append(mensagem)

#exibir historico de mensagens
for mensagem in st.session_state['lista_mensagens']:
    print(mensagem)
    role=mensagem['role']
    content=mensagem['content']
    st.chat_message(role).write(content)

#exibir msg demandada na caixa de texto
mensagem_usuario=st.chat_input('Escreva sua msg')

if mensagem_usuario:
    #user -> usuario
    #assistant -> ia
    st.chat_message('user').write(mensagem_usuario)
    #para adicionar uma mensagem
    #st.session_state['lista_mensagem'].append(mensagem)
    mensagem={'role':'user','content':mensagem_usuario}
    st.session_state['lista_mensagens'].append(mensagem)
    
    #RESPOSTA DA INTELIGENCIA ARTIFICIAL
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state['lista_mensagens'],
        model='gpt-4o'            
    )
    print(resposta_modelo)
    
    resposta_ia=resposta_modelo.choices[0].message.content   
    #resposta_ia= 'Você quis dizer: ' + mensagem_usuario    
    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia={'role':'assistant','content':resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)
    

    
