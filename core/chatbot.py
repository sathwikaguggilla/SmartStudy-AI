def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! I am SmartStudy AI 🤖"

    elif "summary" in user_input:
        return "Click the Summary button to generate a summary."

    elif "quiz" in user_input:
        return "Click the Quiz button to test your knowledge."

    elif "structure" in user_input:
        return """
        📁 SmartStudy AI Project Structure:

        SmartStudy_AI/
        ├── main.py
        ├── core/
        ├── components/
        ├── utils/
        ├── assets/
        └── requirements.txt
        """

    else:
        return "I'm here to help you study!"