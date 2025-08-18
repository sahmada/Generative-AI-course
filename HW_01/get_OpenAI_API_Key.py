from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);