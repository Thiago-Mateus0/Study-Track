# Study Track - Meu rastreador de estudos
# Criado para praticar Python enquanto acompanho meu progresso na faculdade

import json
import os
from datetime import date

# Pede um número inteiro positivo e repete a pergunta se a pessoa digitar outra coisa
def pedir_numero(pergunta):
    while True:
        try:
            numero = int(input(pergunta))
            if numero > 0:
                return numero
        except ValueError:
            pass
        print("Digite um numero inteiro maior que zero.")


# Carrega os dados salvos, ou começa do zero se for a primeira vez
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        dados = json.load(f)
    sessoes = dados["sessoes"]
    meta_minutos = dados["meta_minutos"]
else:
    sessoes = []
    meta_minutos = 60

while True:
    print("\n--- STUDY TRACK ---")
    print("1. Registrar estudo")
    print("2. Ver progresso")
    print("3. Mudar meta diaria")
    print("4. Sair")

    opcao = input("\nEscolha uma opcao: ")

    # ----- REGISTRAR ESTUDO -----
    if opcao == "1":
        topico = input("O que voce estudou? ")
        minutos = pedir_numero("Por quantos minutos? ")

        sessao = {"topico": topico, "minutos": minutos, "data": str(date.today())}
        sessoes.append(sessao)

        # Salva no arquivo apos cada registro
        with open("data.json", "w") as f:
            json.dump({"sessoes": sessoes, "meta_minutos": meta_minutos}, f)

        print("Sessao salva!")

        # Soma so o que foi estudado hoje (sessoes antigas, sem data, nao entram)
        hoje = 0
        for s in sessoes:
            if s.get("data") == str(date.today()):
                hoje = hoje + s["minutos"]

        if hoje >= meta_minutos:
            print("Voce atingiu sua meta do dia!")
        else:
            faltam = meta_minutos - hoje
            print("Hoje voce estudou " + str(hoje) + " min. Faltam " + str(faltam) + " minutos para sua meta.")

    # ----- VER PROGRESSO -----
    elif opcao == "2":
        if len(sessoes) == 0:
            print("Nenhuma sessao registrada ainda.")
        else:
            print("\n--- Suas sessoes ---")
            total = 0
            for i in range(len(sessoes)):
                s = sessoes[i]
                print(str(i + 1) + ". " + s["topico"] + " - " + str(s["minutos"]) + " min")
                total = total + s["minutos"]

            print("\nTotal estudado: " + str(total) + " minutos")
            print("Sua meta diaria: " + str(meta_minutos) + " minutos")

    # ----- MUDAR META -----
    elif opcao == "3":
        meta_minutos = pedir_numero("Nova meta em minutos: ")

        # Salva a nova meta no arquivo
        with open("data.json", "w") as f:
            json.dump({"sessoes": sessoes, "meta_minutos": meta_minutos}, f)

        print("Meta atualizada para " + str(meta_minutos) + " minutos!")

    # ----- SAIR -----
    elif opcao == "4":
        print("Ate mais! Be water, my friend.")
        break

    else:
        print("Opcao invalida. Tente de novo.")