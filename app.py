import streamlit as st
import streamlit.components.v1 as components

# إعدادات واجهة تطبيق وحدة الحروق
st.set_page_config(
    page_title="الوكيل الرقمي - وحدة الحروق | مستشفى الأميرة بسمة",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 الوكيل الرقمي - وحدة الحروق")
st.subheader("مستشفى الأميرة بسمة التعليمي")

# لصق المقتطف المنسوخ هنا بين علامات التنصيص
gabster_code = """
<script data-gabster-widget src="https://widget.gabster.ai/loader?cbid=6aa465d23ce8e5fcb461c305" data-embed-type="widget"></script>
"""

# عرض المقتطف داخل Streamlit
components.html(gabster_code, height=620, scrolling=True)
