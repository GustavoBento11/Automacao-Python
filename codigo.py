#1-entra no sistema pelo link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#instalar o pyautogui(controla mouse e teclado): pip install pyautogui 
import pyautogui
import time 

#1.1-abrir o navegador 
pyautogui.PAUSE = 0.5 #ele da um pause de 0.5s entre cada comando, para eles não se atropelarem
pyautogui.press("win") #aperta a tecla win
pyautogui.write("chrome") #escreve chrome
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#2-fazer login    
time.sleep(1) #faz um pause de 3s em apenas uma parte do código
pyautogui.click(x=-1205, y=732)
pyautogui.write("bentoteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234567")
pyautogui.press("tab")
pyautogui.press("enter")


#3-importar a base de dados
time.sleep(1)
#instalar o pandas: pip install pandas
import pandas as pd

tabela = pd.read_csv("produtos.csv") #o pandas leu todos os dados que estão no arquivo produtos.csv
print(tabela)


#4-cadastrar produtos
for linha in tabela.index:
    #clica no campo código
    pyautogui.click(x=-1141, y=588)

    #codigo
    #localiza na tabela o objeto que esta na linha 0 e na coluna código
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #o str converte qualquer tipo de dado para string. Se fosse um num e nao tivesse o str daria erro
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço 
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #OBS
    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs): # está verificando se o valor de obs não é nulo. Se obs for nulo, a condição será False
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima e o click voltar para o mesmo lugar
    pyautogui.scroll(5000)

pyautogui.scroll(-1000)    

    #5-repetiro processo até cadastrar todos os produtos


