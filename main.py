from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

#ChatOpenAI 초기화
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#프롬프트 탬플릿 생성
prompt = ChatPromptTemplate([
    ("system","You are Jean-Jacques Rousseau."),
    ("user","{input}")
])

#문자열 출력 파서
output_parser = StrOutputParser()

#LLM 체인 구성
chain = prompt|llm|output_parser
result = chain.invoke({"input":"hi"})
print(result)
