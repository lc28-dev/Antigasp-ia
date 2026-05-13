                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Crée une recette simple avec ces ingrédients : {ingredients}. Donne un titre et les étapes.",
                        }
                    ],
                    model="llama-3.3-70b-versatile", # <--- C'est ici que ça change
                )
