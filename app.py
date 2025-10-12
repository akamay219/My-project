from flask import Flask, request, render_template, jsonify
import os
import openai

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Please set your OPENAI_API_KEY as an environment variable.")

# Store conversation history per session (in memory)
SESSIONS = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id = data.get("session_id", "default")
    user_message = data.get("message", "")

    # Initialize history for this session
    history = SESSIONS.setdefault(session_id, [])
    history.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in history],
            max_tokens=400,
            temperature=0.7
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = f"Error contacting OpenAI API: {e}"

    # Add AI response to history
    history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply, "session_id": session_id})

if __name__ == "__main__":
    app.run(debug=True)
