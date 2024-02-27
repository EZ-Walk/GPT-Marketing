import streamlit as st
from openai import OpenAI
import toml

# Get an open AI API client and cache it
@st.cache_resource
def get_openai_client(api_key):
    return OpenAI(api_key=api_key)

st.sidebar.title('Config')

example_select = st.sidebar.selectbox(label='Example Scenario', options=toml.load('examples.toml'), index=0)
example = toml.load('examples.toml')[example_select]
# print(toml.load('examples.toml'))
print(example)


st.markdown('''
# 🚀 Welcome to GPT-Marketing Project! 🎉

This is your go-to spot for creating awesome marketing content using the Chat GPT technology. You can tailor-make the output to resonate with your specific audience and set the tone that matches your brand. Put your OpenAI API key in the sidebar to get started. (Or ask me for mine!)

## 📝 Here's how to get started with the Demo:
            ''')


st.markdown('''1. **What type of content do you need?** 📚 Let us know if you're looking to create cover letters, social media content, emails or something else. The world is your content oyster!''')
content_type = st.text_input("Cover Letter, Linked in post with emojis, etc.", value=example['content_type'])

st.markdown('''2. **Who's your audience?** 🎯 Include demographics, interests, and any other relevant info. The better we know your audience, the more engaging the content.''')
audience = st.text_input('Audience', value=example['audience'])

st.markdown('''3. **Got a writing sample?** 🖊️ Sharing a sample from the author helps us to match your unique style and tone.''')
writing_sample = st.text_area('Writing Sample', value=example['writing_sample'])

st.markdown('''What's the goal? 🎯 Before we dive in, let's get clear about your goal. Are we aiming to educate, sell, inspire, or something else? Every great piece of content has a purpose – let's define yours!''')
objective = st.text_input('Objective', value=example['objective'])

st.markdown('''4. **Any extra thoughts?** 💡 This step is totally optional! If there's a specific topic you want to dive into, questions to answer or any guidelines, feel free to share.''')
prompt = st.text_area('Extra Prompts', value=example['prompt'])

st.markdown('''Enjoy your journey crafting custom marketing content! 🎈''')

assembled_messages = [
                {
                    "role": "system",
                    "content": "You are an expert at writing marketing copy and you love writing messages that people connect with."
                },
                {
                    "role": "user",
                    "content": f"You understand the thoughts and feelings of the following audience: {audience} and you will use this understanding as a basis for reasoning."
                },
                {
                    "role": "user",
                    "content": f"Output a {content_type}."
                },
                                {
                    "role": "user",
                    "content": f"The goal of this message is to {objective}."
                },
                {
                    "role": "user",
                    "content": f"Mimic the writing style of: {writing_sample}. And do: {prompt}"
                }
            ]

if st.button('Submit'):
    with st.spinner('Generating content...'):
        client = get_openai_client(st.secrets['api_key'])
        response = client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=assembled_messages
        )
        
        st.write_stream(response)
        
        