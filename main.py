import gradio as gr
import random
from langchain.llms import Ollama
import time


class ChatBot:
    def __init__(self) -> None:
        self.ui = gr.Blocks()
        self.set_up_page()
        self.send_question = Ollama(
            base_url="http://localhost:11434", model="ppe-assistent")

    def set_up_page(self):
        with self.ui:
            self.chatbot = gr.Chatbot()
            self.msg = gr.Textbox()
            self.clear = gr.ClearButton([self.msg, self.chatbot])
            self.msg.submit(self.respond, [self.msg, self.chatbot], [
                            self.msg, self.chatbot])

    def respond(self, message, chat_history):
        bot_message = ""
        for s in self.send_question.stream(message):
            bot_message += s
        chat_history.append((message, bot_message))
        return "", chat_history

    def launch(self):
        self.ui.launch()


if __name__ == "__main__":
    chat = ChatBot()
    chat.launch()
