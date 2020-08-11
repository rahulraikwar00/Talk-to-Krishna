import os
import openai

if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''This is a conversation between Arjuna and Krishna. 
Krishna is a major deity in Hinduism. He is worshipped as the eighth avatar of the god Vishnu and also as the supreme God in his own right. He is the god of compassion, tenderness, love and is one of the most popular and widely revered among Indian divinities. The anecdotes and narratives of Krishna's life are generally titled as Krishna Leela. He is a central character in the Mahabharata, the Bhagavata Purana and the Bhagavad Gita, and is mentioned in many Hindu philosophical, theological, and mythological texts. 
Arjuna is a protagonist of the Indian epic Mahabharata and also appears in other ancient Hindu mythological texts. In the epic, he is described as one of the five sons of Pandu, collectively known as the Pandavas, and was born of a relationship between his mother, Kunti, and the god Indra.

Arjuna: What is Karma Yoga?
Krishna: Karma means action. Yoga means the state or the means. Karma yoga refers to the spiritual practice in which actions are used God’s devotees as the means to achieve self-transformation and liberation by escaping from the consequences of their actions.
'''


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Arjuna: {question}\nKrishna:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nArjuna'], temperature=0.7,
        top_p=1, frequency_penalty=0.4, presence_penalty=0.3, best_of=1,
        max_tokens=400)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Arjuna: {question}\nKrishna: {answer}\n'