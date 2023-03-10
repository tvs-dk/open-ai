#This code makes it possible to chat with Chat-GPT using python
#There is probably some adjustments that can be made to the parameters such as max tokens etc.


import openai

openai.api_key = "your_api"

def generate_response(prompt, model="text-davinci-002"):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message


prompt = "Explain the theory about LF NMR transverse relaxation time"

response = generate_response(prompt)
print(response)

