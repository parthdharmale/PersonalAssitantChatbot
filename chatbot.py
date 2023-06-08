import tkinter as tk
import openai
import time


openai.api_key = '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'

bot_name = 'Oggy'


start_prompt = f'Hello, my name is {bot_name}. I can help you with tasks such as setting reminders, creating to-do lists, and more. How can I assist you today?'

openai.api_key = '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'
openai_model = 'text-davinci-003'


def generate_response(prompt):
    response = openai.Completion.create(
        engine=openai_model,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()


def get_response():
    user_input = input_box.get()
    global bot_name
    prompt = f'{bot_name}: {user_input}\n{bot_name}: '
    response = generate_response(prompt)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n{bot_name}: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    input_box.delete(0, tk.END)

#User Interface
root = tk.Tk()
root.title(bot_name)
root.configure(bg="#ADD8E6")

chat_history = tk.Text(root, height=20, width=50, bg="#F0F8FF", font=("Times New Roman", 12))
chat_history.config(state=tk.DISABLED)
scrollbar = tk.Scrollbar(root)
scrollbar.config(command=chat_history.yview)
chat_history.config(yscrollcommand=scrollbar.set)
input_box = tk.Entry(root, width=50, font=("Times New Roman", 12))
input_box.configure(bg="#F0FFFF", highlightbackground="#F0FFFF")
send_button = tk.Button(root, text="Send", command=get_response, bg="#ADD8E6", font=("Times New Roman", 12))

chat_history.pack(side=tk.TOP, pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
input_box.pack(side=tk.LEFT, padx=5, pady=10)
send_button.pack(side=tk.RIGHT, padx=5, pady=10)


chat_history.config(state=tk.NORMAL)
chat_history.insert(tk.END, f"{bot_name}: {start_prompt}\n\n")
chat_history.config(state=tk.DISABLED)


root.mainloop()

while True:
    get_response()
    time.sleep(0)
