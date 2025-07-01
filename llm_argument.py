from ai_common import *
import openai_common
import anthropic_common
import google_common

gpt_model = "gpt-4o-mini"
claude_model = "claude-3-haiku-20240307"

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

claude_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]

def call_gpt():
    messages = add_system_message(gpt_system, [])
    for gpt, claude in zip(gpt_messages, claude_messages):
        add_assistant_message(gpt, messages)
        add_user_message(claude, messages)
    response = openai_common.chat(gpt_model, messages)
    return response

def call_claude():
    messages = []
    for gpt, claude_message in zip(gpt_messages, claude_messages):
        add_user_message(gpt, messages)
        add_assistant_message(claude_message, messages)
    add_user_message(gpt_messages[-1], messages)
    response = anthropic_common.chat(claude_model, claude_system, messages)
    return response

print(f"GPT:\n{gpt_messages[0]}\n")
print(f"Claude:\n{claude_messages[0]}\n")

for i in range(5):
    gpt_next = call_gpt()
    print(f"GPT:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)

    claude_next = call_claude()
    print(f"Claude:\n{claude_next}\n")
    claude_messages.append(claude_next)