import os 
import openai

# The code is run on python3.7 platform with library "openai"
# Please create and use your personal key: https://platform.openai.com/account/api-keys (free for 3 Months with $18)
# Several models are listed : https://platform.openai.com/docs/models/gpt-3
# The meaning of parameters are shown in https://dev.to/codemee/yong-python-chuan-jie-openai-mo-ni-chatgpt-liao-tian-ji-qi-ren-2fh6
openai.api_key = "Your API Key"

def send_respond_openai(prompt):
    response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = prompt,
                max_tokens = 1024,
                temperature = 0.8,
                top_p = 0.75,
                n=1
                )
    completed_text = response["choices"][0]["text"]
    return completed_text



if __name__ == "__main__":
    prev_prompt = ''
    prev_ans = ''
    while 1:   
        message = input("You: ")
        if message == "exit":
            break
        else:
            prompt=prev_prompt + "\n"+ prev_ans + "\n" + message
            completed_text = send_respond_openai(prompt)
            print('Open AI: ',completed_text)
            prev_prompt = message
            prev_ans = completed_text
