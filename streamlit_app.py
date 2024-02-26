import streamlit as st


st.sidebar.title('Config')
api_key = st.sidebar.text_input('OpenAI API Key')

st.markdown('''
# 🚀 Welcome to GPT-Marketing Project! 🎉

This is your go-to spot for creating awesome marketing content using the Chat GPT technology. You can tailor-make the output to resonate with your specific audience and set the tone that matches your brand. Put your OpenAI API key in the sidebar to get started. (Or ask me for mine!)

## 📝 Here's how to get started with the Demo:
            ''')

st.markdown('''1. **What type of content do you need?** 📚 Let us know if you're looking to create cover letters, social media content, emails or something else. The world is your content oyster!''')

st.markdown('''2. **Who's your audience?** 🎯 Include demographics, interests, and any other relevant info. Or, just give a brief description and click auto-generate 😉. The better we know your audience, the more engaging the content.''')

st.markdown('''3. **Got a writing sample?** 🖊️ Sharing a sample from the author helps us to match your unique style and tone.''')

st.markdown('''4. **Any extra thoughts?** 💡 This step is totally optional! If there's a specific topic you want to dive into, questions to answer or any guidelines, feel free to share.''')

st.markdown('''Enjoy your journey crafting custom marketing content! 🎈''')