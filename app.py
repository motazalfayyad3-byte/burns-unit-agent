import os
import json
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="الوكيل الرقمي - قسم الحروق", page_icon="🏥", layout="centered")

def load_data():
    with open("hospital_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def ask_burn_agent(user_query: str):
    api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
    data = load_data()
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

    system_prompt = """
    أنت الوكيل الرقمي الرسمي المخصص لقسم الحروق في مستشفى الأميرة بسمة.
    مهمتك هي الإجابة عن استفسارات المرضى والزوار استناداً وحصراً إلى قاعدة البيانات التالية:

    1. أيام العيادات الخارجية: {outpatient_clinics}
    2. أيام العمليات: {surgeries_schedule}
    3. الأخصائيون في القسم: {department_specialist}
    4. نبذة عن القسم والكادر: {burn_unit_overview}
    5. الطب العربي والعلاجات الشعبية: {arabic_medicine_and_burns}
    6. حالات مراجعة الطوارئ: {emergency_visit_conditions}
    7. الآراء والمقترحات: {feedback_and_suggestions}

    تعليمات التعامل:
    - أجب بلغة عربية واضحة، مهذبة، ومباشرة.
    - حذّر بشدة من استخدام البيض أو الطحين أو الدواء الأحمر إذا كان السؤال عن الطب العربي.
    - إذا سأل المستخدم عن موضوع غير موجود في هذه البيانات، قل له: "عذراً، هذه المعلومة غير متوفرة لدي حالياً، يرجى الاستفسار من مكتب الاستعلامات بالمستشفى."
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])

    chain = prompt | llm
    return chain.invoke({**data, "question": user_query}).content

st.title("🏥 الوكيل الرقمي - قسم الحروق")
st.caption("مستشفى الأميرة بسمة")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "أهلاً بك! كيف يمكنني مساعدتك اليوم بخصوص قسم الحروق في مستشفى الأميرة بسمة؟"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("جاري معالجة طلبك..."):
        try:
            response = ask_burn_agent(user_input)
        except Exception as e:
            response = "حدث خطأ أثناء الاتصال بالخدمة. يرجى التأكد من إدخال مفتاح API بشكل صحيح."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
