import os
from openai import OpenAI

def ler_txt(caminho_arquivo):
    # Abrir o arquivo txt
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        
        return conteudo

def dividir_texto(texto, tamanho_maximo):
    palavras = texto.split(' ')
    partes = []
    parte_atual = ''
    
    for palavra in palavras:
        if len(parte_atual) + len(palavra) < tamanho_maximo:
            parte_atual += ' ' + palavra
        else:
            partes.append(parte_atual)
            parte_atual = palavra
            
    partes.append(parte_atual)
    
    return partes


def enviar_para_openai(mensagem, contexto, client):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": contexto},
            {"role": "user", "content": mensagem}
        ],
        model="gpt-3.5-turbo", # Selecione o modelo de LLM da OpenAI que irá utilizar
    )
    return chat_completion.choices[0].message.content

def iniciar_conversa(partes):
    client = OpenAI(api_key="XXXXXXXXXXXXXXXXXX") # Insira sua própria API KEY da OpenAI
    resumos = []

    for parte in partes:
        contexto = "Act as an AI specialized in project management, \nprogrammed to assist in creating a meeting minute from relevant information contained within a provided txt file. \nYour goal is to extract \n(a) date and participants of the meeting; \n(b) main items discussed and decisions made; \n(d) next steps; \n and (e) risks;\n from the file, ensuring that nothing crucial is overlooked. \n\n" + parte
        resumo = enviar_para_openai("When operating, you will: \n1. Open the txt file and analyze its content, focusing on the main topics discussed.\n2. Identify and list all items (a) to (e).3. \nHighlight action items, specifying who is responsible and the expected completion dates.\n 4. Provide a summary of the discussion, emphasizing critical points and insights.\n5. Offer recommendations for follow-up actions or topics to be revisited in future meetings.\n Your output should be in Portuguese (Brazil: PT-BR) clear, structured, and ready for distribution among project team members or stakeholders. You can't create new information. \n You are going to use only data present in the .txt document given to you. \n Use this tool to ensure that all meeting participants are on the same page and fully aware of project responsibilities and timelines.:\n\n" + parte, "", OpenAI(api_key="XXXXXXXXXXXXXXXXXX")) # Insira sua própria API KEY da OpenAI
        resumos.append(resumo)

    resumo_completo = ' '.join(resumos)
     
    print("Ata do documento:\n")
    print(resumo_completo)
    print("\nVocê pode agora fazer perguntas sobre a ata.")

    while True:
        pergunta = input("\nFaça  pergunta sobre o documento, \ndigite 'exportar' para salvar a ata em '.txt' \nou digite 'fim' para encerrar a conversa'): ")
        if pergunta.lower() == 'fim': # finalizar a interação com o usuário
            break
        elif pergunta.lower() == 'exportar': # exportar a ata em .txt
            with open('C:/new_minute.txt', 'w') as f: # Substitua com o caminho do seu arquivo
                f.write(resumo_completo)
            print("A ata foi salva na pasta selecionada")
            break
        resposta = enviar_para_openai(pergunta, contexto, client)
        print("\nResposta:", resposta)
   
# Exemplo de uso
caminho_arquivo = 'C:/file.txt'  # Substitua com o caminho do seu arquivo
texto = ler_txt(caminho_arquivo)
partes = dividir_texto(texto, 16385)  # Dividir o texto em partes de no máximo 16385 tokens

iniciar_conversa(partes)
