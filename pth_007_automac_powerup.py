import pyautogui
import time

#pyautogui.click => clicar em algum lugar
#pyautogui.press => apertar uma tecla
#pyautoqui.write => escrever um texto

#Passo 1: entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1 #faz um segundo de pausa entre cada comando
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.click(x=1133, y=586)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3) #aguarda 3 segundos para executar a proxima ação

#Passo 2: fazer o login (e-mail + senha) usar o script pos_mouse.py
# pos do campos 'e-mail' é x=3345, y=343
# pos do campo "senha" é x=3330, y=463
pyautogui.click(x=3345, y=343)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.click(x=3330, y=463)
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

#Passo 3: importar base de dados
import pandas as pd
tabela=pd.read_csv(r'G:\Meu Drive\2_REPOSITORIOS\PYTHON\PTH_008_AUTOMACAO_PROCESSOS\drive-download-20250603T080918Z-1-001\produtos.csv')
print(tabela)

#Passo 4: cadastrar produto
for linha in tabela.index:
    pyautogui.click(x=3233, y=183) #posicao do primeiro campo x=3233, y=183
    
    #codigo="MOLO000251"
    codigo=str(tabela.loc[linha,'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    #marca='Logitech'
    marca=str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    #tipo='Mouse'
    tipo=str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    #categoria='1'
    categoria=str(tabela.loc[linha,'categoria']) #categoria deve ser formatada como texto
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    #preco_unitario='25.95'
    preco_unitario=str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    
    #custo='6.50'
    custo=str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    #obs=""
    obs=str(tabela.loc[linha,'obs'])
    if obs !='nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    
    pyautogui.press('enter')
    
    pyautogui.scroll(-9000) #ir para o final da pagina de registros
    pyautogui.scroll(10000) #ir para o topo da pagina de registros

#Passo 5: repetir para outro produto

