import streamlit as st
import openai

# 🔒 안전하게 숨긴 API 키 불러오기
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 앱 타이틀
st.set_page_config(page_title="밸류시프트 GPT 상품명 생성기", page_icon="🛍️")
st.title("🎀 밸류시프트 GPT 상품명 생성기 🎀")
st.markdown("원하는 키워드를 입력하면, 상품명을 AI가 뿅~ 만들어드려요!")

# 사용자 입력
keyword = st.text_input("📦 상품 키워드 입력", placeholder="예: 핑크 고양이 스마트폰 케이스")

# 버튼 누르면 실행
if st.button("상품명 생성하기"):
    if keyword.strip() == "":
        st.warning("키워드를 입력해 주세요!")
    else:
        with st.spinner("상품명 생성 중... 뿅!✨"):
            try:
                prompt = f"'{keyword}' 키워드를 활용해서 쇼핑몰에서 쓸 수 있는 귀엽고 매력적인 상품명을 5개 추천해줘. 1, 2, 3 형식으로."

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "너는 감성 쇼핑몰의 상품명 작명가야."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8
                )

                output = response.choices[0].message.content.strip()
                st.success("🎉 상품명 생성 완료!")
                st.text_area("💡 추천 상품명", value=output, height=200)

            except Exception as e:
                st.error(f"에러 발생: {e}")
