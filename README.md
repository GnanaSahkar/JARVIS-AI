Function to Integrate Open AI using OpenAI libraries and API Key







def ai(prompt):
    OPENAI_API_KEY = "Enter your API here"
    client = OpenAI(api_key=OPENAI_API_KEY)

    text = f"Sahkar's AI Response for the prompt: {prompt} \n *****************************************\n\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response['choices'][0]['message']['content']

    if not os.path.exists("Responses"):
        os.mkdir("Responses")

    with open(f"Responses/prompt-{random.randint(1, 23423674376675)}.txt", "w") as f:
        f.write(text)


