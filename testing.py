import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-test-123456789")

def generate_summary(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def process_large_batch(items):
    results = []

    for item in items:
        summary = generate_summary(item)
        results.append(summary)

    return results

if __name__ == "__main__":
    print(generate_summary("DebtMap is an AI-powered migration advisor."))
