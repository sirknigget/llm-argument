from ai_common import *
import openai_common
import anthropic_common
import google_common

gpt_model = "gpt-4o-mini"
claude_model = "claude-3-haiku-20240307"
gemini_model = google_common.MODEL_GEMINI_2_FLASH

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way. You talk with 2 other bots."

claude_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting. You talk with 2 other bots."

gemini_system = "You are a chatbot that's a big smartass. You always make nerdy jokes. You always inject your hyper-intelligence into every normal conversation.  You talk with 2 other bots."

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]
gemini_messages = ["Hello world!"]

def call_gpt():
    messages = add_system_message(gpt_system, [])
    for gpt, claude, gemini in zip(gpt_messages, claude_messages, gemini_messages):
        add_assistant_message(gpt, messages)
        add_user_message("Claude says:\n" + claude, messages)
        add_user_message("Gemini says\n" + gemini, messages)
    response = openai_common.chat(gpt_model, messages)
    return response


def call_claude():
    messages = []
    for gpt, claude_message, gemini in zip(gpt_messages, claude_messages, gemini_messages):
        add_user_message("GPT says:\n" + gpt, messages)
        add_assistant_message(claude_message, messages)
        add_user_message("Gemini says\n" + gemini, messages)
    add_user_message(gpt_messages[-1], messages)
    response = anthropic_common.chat(claude_model, claude_system, messages)
    return response


def call_gemini():
    messages = []
    for gpt, claude_message, gemini in zip(gpt_messages, claude_messages, gemini_messages):
        add_user_message("GPT says:\n" + gpt, messages)
        add_user_message("Claude says:\n" + claude_message, messages)
        add_assistant_message(gemini, messages)
    add_user_message(gpt_messages[-1], messages)
    add_user_message(claude_messages[-1], messages)
    response = google_common.chat(gemini_model, gemini_system, messages)
    return response


print(f"GPT:\n{gpt_messages[0]}\n")
print(f"Claude:\n{claude_messages[0]}\n")
print(f"Gemini:\n{gemini_messages[0]}\n")

for i in range(5):
    gpt_next = call_gpt()
    print(f"GPT:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)

    claude_next = call_claude()
    print(f"Claude:\n{claude_next}\n")
    claude_messages.append(claude_next)

    gemini_next = call_gemini()
    print(f"Gemini:\n{gemini_next}\n")
    gemini_messages.append(gemini_next)
