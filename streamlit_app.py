import streamlit as st
from openai import OpenAI
import toml

# Get an open AI API client and cache it
@st.cache_resource
def get_openai_client(api_key):
    return OpenAI(api_key=api_key)

st.sidebar.title('Config')
api_key = st.sidebar.text_input('OpenAI API Key')

st.markdown('''
# 🚀 Welcome to GPT-Marketing Project! 🎉

This is your go-to spot for creating awesome marketing content using the Chat GPT technology. You can tailor-make the output to resonate with your specific audience and set the tone that matches your brand. Put your OpenAI API key in the sidebar to get started. (Or ask me for mine!)

## 📝 Here's how to get started with the Demo:
            ''')


st.markdown('''1. **What type of content do you need?** 📚 Let us know if you're looking to create cover letters, social media content, emails or something else. The world is your content oyster!''')
content_type = st.text_input("Cover Letter, Blog post, etc.", value='Cover letter')

st.markdown('''2. **Who's your audience?** 🎯 Include demographics, interests, and any other relevant info. The better we know your audience, the more engaging the content.''')
audience = st.text_input('Audience', value='Vail Resorts')

st.markdown('''3. **Got a writing sample?** 🖊️ Sharing a sample from the author helps us to match your unique style and tone.''')
writing_sample = st.text_area('Writing Sample', value="""I thought I\'d go back and create a little streamlit demo of the project to showcase the functionality. Upon review, I can\'t figure out a way to apply the functionality of the app I built. There is code in there that out performed the state of the art in spell checking but no way to actually use it."

So, one lesson is clear. Losing sight of the use case and the user experience of an app will doom it to failure.

I need to refocus my work with Allies on the user experience. 

And my response is clear as well. I have to fix this in order to learn from it. So I’ll start again from project definition.""")

st.markdown('''4. **Any extra thoughts?** 💡 This step is totally optional! If there's a specific topic you want to dive into, questions to answer or any guidelines, feel free to share.''')
prompt = st.text_area('Extra Prompts', value='Please write a friendly cover letter for this position highlighting my data analytics skills and my passion for skiing')

st.markdown('''Enjoy your journey crafting custom marketing content! 🎈''')

assembled_messages = [
                {
                    "role": "system",
                    "content": "You are an expert marketing copy writer and you are proficient in applying all the principles of marketing in your work. You write messages that connect with the audience and follow a sepcific tone of voice that you are given."
                },
                {
                    "role": "user",
                    "content": f"Please write a {content_type}. Make it targeted to the interests and desires of: {audience}. Mimic the writing style of: {writing_sample}. And do {prompt}."
                }
            ]

if st.button('Submit'):
    with st.spinner('Generating content...'):
        client = get_openai_client(api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            stream=True,
            messages=assembled_messages
        )
        
        st.write_stream(response)
        
        