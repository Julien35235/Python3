def openfilleChatGPTMethod():
    import openai

    # Configuration de l'API OpenAI
    openai.api_key = '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'  # Remplacez par votre clé d'API OpenAI

    def chat_with_gpt(prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',  # Sélectionnez le moteur ChatGPT approprié
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
            n=1,
            stop=None,
            echo=True
        )
        return response.choices[0].text.strip()

    # Exemple d'utilisation
    user_input = input("Vous: ")

    while user_input.lower() != 'exit':
        # Ajoutez un prompt à votre choix pour démarrer la conversation
        conversation_history = "Bonjour, je suis ChatGPT, comment puis-je vous aider?"

        # Ajoutez l'entrée utilisateur à l'historique de conversation
        conversation_history += '\nUtilisateur: ' + user_input

        # Obtenir la réponse de ChatGPT
        response = chat_with_gpt(conversation_history)

        # Afficher la réponse de ChatGPT
        print("ChatGPT:", response)

        # Demander une nouvelle entrée à l'utilisateur
        user_input = input("Vous: ")