import openai
from decouple import config

KEY_OPENAI = config('KEY_OPENAI')
openai.api_key = KEY_OPENAI
print(f'openai.api_key : {openai.api_key}')


def openAIQuery(query):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=query,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'

    return answer


if __name__ == '__main__':
    if not openai.api_key:
        print(f'api_key is not set')
        exit(0)
        
    query = 'Me diga uma receita de bolo.'
    try:
        response = openAIQuery(query)
        print(f'Response : {response}')
    except Exception as e:
        print(f'Exception : {str(e)}')