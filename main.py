import os
from dotenv import load_dotenv, dotenv_values
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

if response.usage_metadata == None:
    raise RuntimeError("Response usage metadata is None.")
else:
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

print(response.text)

def main():
    print("Hello from ai-agent-with-boot-dev!")


if __name__ == "__main__":
    main()
