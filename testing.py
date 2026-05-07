import openai
import os
import requests
import json
import time

# TODO: migrate to new OpenAI client
# FIXME: remove hardcoded API key
# TODO: split this file into smaller services

openai.api_key = "sk-test-super-secret-openai-key"

JWT_SECRET = "my-production-jwt-secret"
API_KEY = "1234567890abcdef"

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

        print("Processing item...")
        print("Processing item...")
        print("Processing item...")

        results.append(summary)

    return results

def massive_legacy_function(data):
    final_results = []

    for item in data:
        try:
            response = requests.post(
                "https://api.example.com/process",
                json={"data": item},
                timeout=120
            )

            if response.status_code == 200:
                parsed = response.json()

                for value in parsed.get("results", []):
                    transformed = {
                        "value": value,
                        "timestamp": time.time(),
                        "status": "processed"
                    }

                    final_results.append(transformed)

        except Exception as e:
            print(e)

    return final_results

if __name__ == "__main__":
    print(generate_summary("DebtMap is an AI-powered migration advisor."))
