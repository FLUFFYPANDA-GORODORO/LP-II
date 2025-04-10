print("Starting the chatbot GUI...")

import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # Replace with your key
model = genai.GenerativeModel('gemini-pro')
print("Script started!")  # Add this at the top of your script


def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def send():
    user_input = entry.get()
    chat_window.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)
    bot_reply = ask_gemini(user_input)
    chat_window.insert(tk.END, f"Bot: {bot_reply}\n")

# GUI Setup
window = tk.Tk()
window.title("Gemini Chatbot")
window.geometry("500x550")

chat_window = scrolledtext.ScrolledText(window, width=60, height=25, wrap=tk.WORD)
chat_window.pack(pady=10)
chat_window.insert(tk.END, "Bot: Hello! How can I assist you today?\n")

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(window, text="Send", command=send)
send_button.pack(side=tk.LEFT, pady=10)

window.mainloop()
