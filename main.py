import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 💫 타이틀
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎓 MBTI로 알아보는<br>나에게 딱 맞는 직업 추천 💼</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🧠 MBTI 선택
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요!", mbti_types)

# 🎯 추천 직업 데이터
mbti_careers = {
    "INTJ": [("전략 컨설턴트", "📊 계획 세우는 데 진심!"), ("AI 연구원", "🧠 미래를 설계하는 두뇌파")],
    "INTP": [("데이터 과학자", "📈 분석에 몰입하는 천재"), ("이론 물리학자", "🔬 세상의 원리를 탐구")],
    "ENTJ": [("CEO", "🏢 리더십의 화신"), ("프로젝트 매니저", "📅 체계적이고 강력한 추진력")],
    "ENTP": [("창업가", "🚀 아이디어 뱅크"), ("마케팅 디렉터", "📣 크리에이티브한 전략가")],
    "INFJ": [("심리상담가", "🧘 사람의 마음을 읽는 능력자"), ("작가", "📚 조용히 세상에 영향을 주는")],
    "INFP": [("시나리오 작가", "🎬 상상력을 현실로"), ("사회복지사", "💖 따뜻한 공감으로 세상과 연결")],
    "ENFJ": [("교사", "👩‍🏫 세상을 이끄는 교육자"), ("홍보 전문가", "🎤 따뜻하고 설득력 있는 커뮤니케이터")],
    "ENFP": [("예술가", "🎨 자유로운 영혼의 표현가"), ("기획자", "🧩 신박한 아이디어 뱅크")],
    "ISTJ": [("회계사", "📒 꼼꼼하고 책임감 있는 전문가"), ("공무원", "🏛️ 체계적이고 신뢰할 수 있는 일꾼")],
    "ISFJ": [("간호사", "💉 따뜻하고 헌신적인 마음"), ("보육교사", "🧸 사랑으로 아이를 품는 직업")],
    "ESTJ": [("군인", "🎖️ 강한 책임감과 리더십"), ("경영 관리자", "📂 조직을 이끄는 핵심인물")],
    "ESFJ": [("이벤트 플래너", "🎉 모두를 위한 행복한 계획자"), ("영업 담당자", "💼 친화력 만렙 커뮤니케이터")],
    "ISTP": [("엔지니어", "⚙️ 손재주와 문제해결력 갑"), ("파일럿", "✈️ 차분하고 정확한 조종사")],
    "ISFP": [("디자이너", "🖌️ 감성과 미적 감각의 조화"), ("플로리스트", "🌸 섬세함과 예술의 만남")],
    "ESTP": [("소방관", "🚒 용감하고 빠른 판단력"), ("스포츠 코치", "🏋️ 에너지 넘치는 리더")],
    "ESFP": [("연예인", "🎤 모두의 이목을 집중시키는 존재감"), ("여행 가이드", "🌍 자유롭고 활기찬 삶")]
}

# 🎨 출력
if mbti:
    st.markdown(f"### 🔎 {mbti} 유형에게 어울리는 직업은?")
    st.markdown("---")
    col1, col2 = st.columns(2)
    careers = mbti_careers.get(mbti, [])
    
    for i, (job, desc) in enumerate(careers):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div style='background-color: #F4F1FF; padding: 20px; border-radius: 15px; margin-bottom: 10px; box-shadow: 2px 2px 10px #DDD;'>
                <h4 style='color:#6C63FF'>{job}</h4>
                <p style='font-size:18px;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
