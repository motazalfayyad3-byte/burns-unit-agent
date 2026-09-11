import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة والعنوان
st.set_page_config(
    page_title="الوكيل الرقمي - وحدة الحروق | مستشفى الأميرة بسمة",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 الوكيل الرقمي - وحدة الحروق")
st.subheader("مستشفى الأميرة بسمة التعليمي")
st.caption("أهلاً بك! يمكنك استخدام الشات أدناه للاستفسار عن بروتوكولات العلاج، المواعيد، وخدمات وحدة الحروق.")

# كود التضمين المباشر للوحة المحادثة
gabster_iframe_code = """
<div style="width: 100%; height: 600px;">
    <script data-gabster-widget src="https://widget.gabster.ai/loader?cbid=6aa465d23ce8e5fcb461c305" data-embed-type="iframe"></script>
</div>
"""

# عرض شاشة المحادثة داخل الصفحة
components.html(gabster_iframe_code, height=620, scrolling=True)
