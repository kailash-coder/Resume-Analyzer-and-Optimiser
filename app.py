import os
import openai
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from text_extractor import get_pdf_text, convert_json_to_text
# from dotenv import load_dotenv, find_dotenv

# Specify the path to your .env file
#env_path = '/home/USER/.env/openai_api' # Change the Path
# Load the OpenAI API key from the .env file
#load_dotenv(env_path)
# openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = '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'



def summarize_with_langchain_and_openai(transcript, language_code = 'english', model_name='gpt-3.5-turbo'):
    # Split the document if it's too long
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_text(transcript)
    text_to_summarize = " ".join(texts[:4]) # Adjust this as needed

    # Prepare the prompt for summarization
    system_prompt = 'I want you to act as a Life Coach that can create good summaries!'
    prompt = f'''\Please analyze the following resume and provide suggestions for improvement, corrections, and a score out of 10 by comparing it with standard resumes in your dataset.
      You can assume that the standard resumes cover a wide range of skills and experiences.
      Resume: {text_to_summarize}.'''

    # Start summarizing using OpenAI
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        temperature=1
    )
    
    return response['choices'][0]['message']['content']

def main():
    st.title('Resume Analyzer')
    # link = st.text_input('Enter the link of the YouTube video you want to summarize:')


    # user_question = st.text_input("Ask about the uploaded documents:")
    st.subheader("Your Resume")
    pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'",type=['pdf'], accept_multiple_files=True)
    if st.button('Start'):
        if pdf_docs:
            try:
                
                progress = st.progress(0)
                status_text = st.empty()

                status_text.text('Loading the transcript...')
                progress.progress(25)

                # Getting both the transcript and language_code
                # transcript, language_code = get_transcript(link)
                temp = get_pdf_text(pdf_docs)

                raw_text = convert_json_to_text(temp)

               
                status_text.text(f'Creating summary...')
                progress.progress(75)

                model_name = 'gpt-3.5-turbo'
                summary = summarize_with_langchain_and_openai(raw_text, language_code = 'english',  model_name='gpt-3.5-turbo')

                status_text.text('Summary:')
                st.markdown(summary)
                progress.progress(100)
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please upload a valid File.')

if __name__ == "__main__":
    main()