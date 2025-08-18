from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import json

# define the language model with a specific temperature and model name
llm = ChatOpenAI(temperature=0.2, model_name="gpt-4o-mini")

# define the prompt template for resume analysis
resume_analysis_prompt = ChatPromptTemplate.from_messages([
    ("system", "شما یک تحلیل‌گر حرفه‌ای رزومه هستید. لطفاً اطلاعات زیر را از رزومه استخراج کنید و به صورت JSON ساختار یافته ارائه دهید:"),
    ("user", """
رزومه:
{resume_text}

اطلاعات مورد نیاز:
1- نام و نام خانوادگی، ایمیل، شماره تلفن تماس
2- اطلاعات تحصیلی: مقطع، رشته، دانشگاه، تاریخ فارغ‌التحصیلی
3- سوابق کاری: عنوان شغل، محل کار، مدت اشتغال، وظایف شغلی
4- مهارت‌های فردی: مهارت‌های فنی، مهارت‌های نرم
5- گواهینامه‌ها و دوره‌های آموزشی
لطفاً خروجی را به صورت JSON ساختار یافته ارائه دهید.
""")
])

# read the resume file
resume_file_path = "resume_sample2.txt"
with open(resume_file_path, "r", encoding="utf-8") as file:
    resume_text = file.read()

# make the prompt to invoke the language model
messages = resume_analysis_prompt.invoke({"resume_text": resume_text})
response = llm.invoke(messages)

# save the response to a JSON file
output_filename = resume_file_path[:-4] + "_analysis.json"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(response.content)

print(f"the analysis has been saved to {output_filename}")
