import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 (프로필 사진 및 연락처)
with st.sidebar:
    st.header("Contact")
    # 이미지가 있다면 주석을 해제하고 경로를 넣으세요
    # st.image("profile.jpg", width=200) 
    st.write("📧 이메일: email@example.com")
    st.write("🔗 깃허브: [github.com/username](https://github.com)")
    st.write("📝 블로그: [velog.io/@username](https://velog.io)")

# 3. 메인 화면 - 타이틀 및 핵심 요약
st.title("👋 안녕하세요, [이름] 입니다!")
st.subheader("💡 '성장을 즐기는 개발자' [이름]의 포트폴리오입니다.")

st.markdown("---")

# 4. 내 소개
st.header("✨ About Me")
st.write(
    """
    안녕하세요! 저는 새로운 기술을 배우고 문제를 해결하는 과정에서 즐거움을 느끼는 개발자입니다. 
    사용자 중심의 서비스를 만들기 위해 고민하며, 동료들과의 원활한 소통을 중요하게 생각합니다.
    """
)

st.markdown("---")

# 5. 기술 스택 (가로로 배열하기 위해 컬럼 사용)
st.header("🛠 Tech Stacks")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages & Frameworks")
    st.markdown("- **Python** (FastAPI, Flask)")
    st.markdown("- **JavaScript** (React, Next.js)")
    st.markdown("- **SQL** (PostgreSQL, MySQL)")

with col2:
    st.subheader("Tools & Devops")
    st.markdown("- **Git / GitHub**")
    st.markdown("- **Docker**")
    st.markdown("- **Streamlit** (Web Dashboard)")

st.markdown("---")

# 6. 프로젝트 경험 (토글 메뉴로 깔끔하게 정리)
st.header("🚀 Projects")

with st.expander("📌 프로젝트 1: 스트림릿 웹 대시보드 구축"):
    st.write("**기간:** 2026.01 - 2026.02")
    st.write("**설명:** 데이터 시각화를 위해 스트림릿을 활용한 내부 모니터링 도구 개발")
    st.markdown("- **주요 역할:** 프론트엔드 UI 설계 및 데이터 파이프라인 연결")
    st.markdown("- **성과:** 기존 대비 데이터 확인 소요 시간 40% 단축")

with st.expander("📌 프로젝트 2: AI 기반 챗봇 서비스"):
    st.write("**기간:** 2025.09 - 2025.12")
    st.write("**설명:** LLM API를 활용한 맞춤형 고객 응대 챗봇 서비스")
    st.markdown("- **주요 역할:** 백엔드 API 서버 구축 및 프롬프트 엔지니어링")
    st.markdown("- **성과:** 일일 활성 사용자 수(DAU) 1,000명 달성")