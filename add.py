from flask import Flask, render_template, request, redirect, url_for
import openai

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

def get_openai_answer(question):
    try:
        # Call OpenAI API with the correct endpoint for chat models
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": question}]
        )
        # Extract the response text
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except openai.error.AuthenticationError:
        return "Authentication failed. Invalid API key."
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            answer = get_openai_answer(question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
