from flask import Flask, render_template, request, jsonify
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from text_extractor import get_pdf_text, convert_json_to_text
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)

CORS(app)

# Set your OpenAI API key
openai.api_key = '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'

def summarize_with_langchain_and_openai(transcript, language_code='english', model_name='gpt-3.5-turbo'):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_text(transcript)
    text_to_summarize = " ".join(texts[:4])

    system_prompt = 'I want you to act as a Life Coach that can create good summaries!'
    prompt = f'''\Please analyze the following resume and provide suggestions for improvement, corrections, and a score out of 10 by comparing it with standard resumes in your dataset.
      You can assume that the standard resumes cover a wide range of skills and experiences.
      Resume: {text_to_summarize}.'''
    
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        temperature=1
    )
    
    return response['choices'][0]['message']['content']



@app.route('/summarize', methods=['POST'])
@cross_origin()
def summarize():
    pdf_docs = request.files.getlist('pdf_docs')
    try:
        temp = get_pdf_text(pdf_docs)
        raw_text = convert_json_to_text(temp)
        summary = summarize_with_langchain_and_openai(raw_text, language_code = 'english',  model_name='gpt-3.5-turbo')
        
        return jsonify({'summary': summary})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
