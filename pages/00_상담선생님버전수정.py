import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 💫 타이틀 영역
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎓 MBTI로 알아보는<br>나에게 딱 맞는 직업 추천 💼</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🧠 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🎯 추천 직업 데이터
mbti_careers = {
    "INTJ": [("전략 컨설턴트", "📊 계획 세우는 데 진심!"), ("AI 연구원", "🧠 미래를 설계하는 두뇌파")],
    "INFP": [("작가", "✍️ 감성을 글로 풀어내는"), ("상담사", "💬 마음을 읽는 따뜻한 조언자")],
    "ESFP": [("MC/방송인", "🎤 무대가 어울리는 분위기 메이커!"), ("이벤트 플래너", "🎈 사람들과 함께하는 즐거움")],
    "ISTJ": [("공무원", "📁 책임감 최고!"), ("회계사", "📊 꼼꼼하고 정확한 일 처리")],
    "ENFP": [("광고기획자", "💡 창의력이 폭발!"), ("스타트업 창업자", "🚀 모험을 즐기는 리더")],
    # 필요한 MBTI에 따라 계속 추가 가능
}

# 🎯 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요! 💖", mbti_types)

# 🌟 결과 출력
if selected_mbti:
    st.markdown(f"<h2 style='color:#FF6F61;'>✨ {selected_mbti} 유형에게 추천하는 직업은?</h2>", unsafe_allow_html=True)

    careers = mbti_careers.get(selected_mbti, [])
    if careers:
        for title, desc in careers:
            st.markdown(f"""
            <div style="background-color:#f9f4ff; padding:15px; margin:10px 0; border-radius:15px; box-shadow: 2px 2px 10px rgba(108, 99, 255, 0.2);">
                <h3 style="color:#6C63FF;">{title}</h3>
                <p style="font-size:16px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("아직 해당 MBTI의 추천 직업 데이터가 준비 중이에요! 🔧")

# 🌈 하단 문구
st.markdown("---")
st.markdown("<p style='text-align: center; font-size:14px; color: gray;'>🚀 이 웹앱은 진로 탐색을 위한 재미있는 참고용 도구입니다!<br>자신만의 길을 자유롭게 탐색하세요 💕</p>", unsafe_allow_html=True)
