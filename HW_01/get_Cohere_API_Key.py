import cohere
apiKey = "zVx5Dhg2RabtMOHroM6CXNhsBvXS91c2wL8MawOJ"
co = cohere.ClientV2(apiKey)
response = co.chat(
    model="command-a-03-2025", 
    messages=[{"role": "user", "content": "hello world!"}]
)

print(response)
