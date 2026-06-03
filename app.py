import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 이름과 아이콘)
st.set_page_config(page_title="폐암 환자 군집 분석 시스템", page_icon="🫁", layout="centered")

# 2. 메인 타이틀 및 설명
st.title("🫁 폐암 환자 군집 분석 시스템")
st.markdown("AI가 환자의 특성을 분석하여  \n어떤 군집(유형)에 속하는지 예측합니다.")

# 구분선
st.markdown("---")

# 3. 환자 정보 입력 섹션
st.subheader("📋 환자 정보 입력")

# 나이, 흡연량, 음주량 입력창을 가로로 배치하기 위한 컬럼 설정
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "나이", 
        min_value=0.00, 
        max_value=120.00, 
        value=50.00, 
        step=1.00, 
        format="%.2f"
    )

with col2:
    smoking = st.number_input(
        "흡연량", 
        min_value=0.00, 
        max_value=100.00, 
        value=10.00, 
        step=1.00, 
        format="%.2f"
    )

with col3:
    drinking = st.number_input(
        "음주량", 
        min_value=0.00, 
        max_value=100.00, 
        value=5.00, 
        step=1.00, 
        format="%.2f"
    )

# 구분선
st.markdown("---")

# 4. 군집 분석하기 버튼 (가로로 꽉 찬 버튼 느낌을 주기 위해 use_container_width 사용)
if st.button("🔍 군집 분석하기", use_container_width=True):
    # 버튼을 클릭했을 때 실행될 로직 (예시 문구)
    st.success("군집 분석을 시작합니다... (이곳에 예측 모델 코드를 연동하세요!)")
    st.write(f"입력된 데이터 -> 나이: {age}, 흡연량: {smoking}, 음주량: {drinking}")