import pyautogui
from


with open('produtos.txt','r') as file:
    for linha in file:
         produto = linha.split(',')[0]
         quantidade = linha.split(',')[1]
         preco = linha.split(',')[2]
        
         pyautogui.click(740,65,duration=2)
         pyautogui.write(produto)
         
         pyautogui.click(739,91,duration=2)
         pyautogui.write(quantidade)

         pyautogui.click(740,124,duration=2)
         pyautogui.write(preco)

