## open ai/chatgpt3  with Python
from openai import OpenAI
import time
import streamlit  as st

openai = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

domains = ['google.com']

for dom in domains:
    result = openai.chat.completions.create(model="gpt-3.5-turbo",messages=[
    {"role": "user", "content": dom}
  ])

    time.sleep(2)
    print('#### sleeping for a while #####')
    st.write(result.choices[0].message.content)
    #print(result.choices[0].message.content)






