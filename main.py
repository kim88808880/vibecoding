import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎓 MBTI로 알아보는<br>나에게 딱 맞는 직업 추천 💼</h1>", unsafe_allow_html=True)
st.markdown("---")

# MBTI 선택
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요!", mbti_types)

# MBTI별 직업 + 설명 + 이미지
mbti_careers = {
    "INTJ": [
        ("전략 컨설턴트", "📊 계획 세우는 데 진심!", "https://images.unsplash.com/photo-1562564055-71e051d33c19"),
        ("AI 연구원", "🧠 미래를 설계하는 두뇌파", "https://images.unsplash.com/photo-1581090700227-1e8f1f9b6c8b")
    ],
    "INTP": [
        ("데이터 과학자", "📈 분석에 몰입하는 천재", "https://images.unsplash.com/photo-1555949963-aa79dcee981d"),
        ("이론 물리학자", "🔬 세상의 원리를 탐구", "https://images.unsplash.com/photo-1581092588421-4c4d3a9df07e")
    ],
    "ENTJ": [
        ("CEO", "🏢 리더십의 화신", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"),
        ("프로젝트 매니저", "📅 체계적이고 강력한 추진력", "https://images.unsplash.com/photo-1551836022-d5d88e9218df")
    ],
    "ENTP": [
        ("창업가", "🚀 아이디어 뱅크", "https://images.unsplash.com/photo-1605902711622-cfb43c4437d7"),
        ("마케팅 디렉터", "📣 창의력 폭발 전략가", "https://images.unsplash.com/photo-1557425493-9acb3c1a5f4b")
    ],
    "INFJ": [
        ("심리상담사", "💖 타인을 이해하는 공감의 대가", "https://images.unsplash.com/photo-1607746882042-944635dfe10e"),
        ("사회운동가", "🌍 세상을 따뜻하게 바꾸는 힘", "https://images.unsplash.com/photo-1541701494587-cb58502866ab")
    ],
    "INFP": [
        ("작가", "✍️ 감성을 글로 표현하는 사람", "https://images.unsplash.com/photo-1519337265831-281ec6cc8514"),
        ("일러스트레이터", "🎨 내면의 세계를 그리는 예술가", "https://images.unsplash.com/photo-1607083204539-63f00c07b0aa")
    ],
    "ENFJ": [
        ("교사", "📚 모두를 이끄는 따뜻한 리더", "https://images.unsplash.com/photo-1577896851231-70ef18881754"),
        ("인사담당자", "🧑‍💼 조직을 연결하는 소통가", "https://images.unsplash.com/photo-1551836022-d5d88e9218df")
    ],
    "ENFP": [
        ("기획자", "🧠 재기발랄한 아이디어 뱅크", "https://images.unsplash.com/photo-1590608897129-79da98d159d4"),
        ("광고 크리에이터", "🎬 트렌드를 주도하는 감각파", "https://images.unsplash.com/photo-1580894894514-41036acc21d1")
    ],
    "ISTJ": [
        ("회계사", "📊 정확함과 신뢰의 상징", "https://images.unsplash.com/photo-1581092334431-498d78c418c4"),
        ("법률 사무원", "⚖️ 꼼꼼하고 체계적인 전문가", "https://images.unsplash.com/photo-1533142266415-ac591a4c3ed1")
    ],
    "ISFJ": [
        ("간호사", "❤️ 헌신과 돌봄의 아이콘", "https://images.unsplash.com/photo-1588776814546-ec7e1e4c1e51"),
        ("보육교사", "🧸 아이들의 따뜻한 친구", "https://images.unsplash.com/photo-1615393361662-10a5cb7e7cd0")
    ],
    "ESTJ": [
        ("경찰관", "🚓 질서를 지키는 정의로운 리더", "https://images.unsplash.com/photo-1607082349250-f7c7a9b5df2f"),
        ("군인", "🎖️ 체계와 규율을 중시하는 수호자", "https://images.unsplash.com/photo-1603530446297-0d8c9cfb6bb6")
    ],
    "ESFJ": [
        ("이벤트 플래너", "🎉 모두가 즐거운 자리를 만드는 사람", "https://images.unsplash.com/photo-1515169067865-5387ec356754"),
        ("영양사", "🥗 건강을 책임지는 따뜻한 전문가", "https://images.unsplash.com/photo-1604908811996-3b75d8cfbdf2")
    ],
    "ISTP": [
        ("기계 엔지니어", "🔧 손재주와 분석력의 조합", "https://images.unsplash.com/photo-1581091012184-5c248c3c9b20"),
        ("응급 구조사", "🚑 빠른 판단력의 실전형", "https://images.unsplash.com/photo-1588776814323-38821184c22f")
    ],
    "ISFP": [
        ("플로리스트", "🌸 감성과 자연을 잇는 직업", "https://images.unsplash.com/photo-1603871415915-47f78584e9a1"),
        ("패션 디자이너", "👗 스타일로 감정을 표현하는 아티스트", "https://images.unsplash.com/photo-1512436991641-6745cdb1723f")
    ],
    "ESTP": [
        ("스포츠 선수", "⚽ 에너지 넘치는 도전자", "https://images.unsplash.com/photo-1534528741775-53994a69daeb"),
        ("소방관", "🔥 행동력과 용기의 상징", "https://images.unsplash.com/photo-1588776814207-1ee1d8e7b703")
    ],
    "ESFP": [
        ("배우", "🎭 무대 위의 빛나는 스타", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd47"),
        ("여행 유튜버", "🌍 삶을 즐기고 공유하는 모험가", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e")
    ]
}

# 추천 결과 출력
st.markdown(f"<h2 style='text-align: center;'>🧭 {mbti}에게 추천하는 직업</h2>", unsafe_allow_html=True)

for job, desc, img_url in mbti_careers[mbti]:
    st.image(img_url, use_column_width=True, caption=job)
    st.markdown(f"### {desc}")
    st.markdown("---")
