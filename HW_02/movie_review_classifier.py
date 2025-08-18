from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
llm = ChatOpenAI(temperature=0)
template = """
    This is a movie review sentiment classifier.
    Review: "I loved the movie! The acting was great and the plot was engaging." This review is positive.
    Review: "What a waste of time. The movie was boring and the acting was terrible." This review is negative.
    Review: "بدتر از اين فيلم نديدم. بازيگرا افتضاح بودن و داستان هم هيچ جذابي نداشت." This review is negative.
    Review: "این فیلم واقعا عالی بود! بازیگران فوق‌العاده بودند و داستان بسیار جذاب بود." This review is positive.
    input review: {review}
"""
i = 1
reviews = [
    "This movie was fantastic! The cinematography was stunning and the performances were top-notch.",
    "I didn't enjoy this film at all. The plot was confusing and the characters were unlikable.",
    "این فیلم واقعا خسته‌کننده بود. داستان هیچ جذابیتی نداشت و بازیگران هم خوب نبودند.",
    "این فیلم یکی از بهترین فیلم‌هایی بود که تا به حال دیده‌ام. داستان فوق‌العاده و بازیگران عالی بودند.",
    "The special effects were amazing, but the story was lacking.",
]
prompt = PromptTemplate(input_variables=["review"], template=template)
formatted_prompt = prompt.format(review=reviews[i])
print('review:', reviews[i])
response = (llm.invoke(formatted_prompt).content.strip())
print('response:', response)