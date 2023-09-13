import openai

openai.api_key = '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'


def gerar_mensagem_personalizada(filme, nota):
    prompt = f"Um usuário assistiu ao filme '{filme}' e deu uma nota de {nota} estrelas. Por favor, escreva uma mensagem personalizada para este usuário."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,  
        n=1,  
    )
    
    return response.choices[0].text.strip()


nome_filme = input("Qual é o nome do filme que você assistiu? ")
nota = int(input("Qual nota (de 1 a 5) você daria para este filme? "))


if 1 <= nota <= 5:
    mensagem = gerar_mensagem_personalizada(nome_filme, nota)
    print(f"Você assistiu '{nome_filme}' e deu a nota {nota}. Mensagem gerada:\n{mensagem}")
else:
    print("A nota fornecida não está dentro do intervalo válido (1 a 5).")

