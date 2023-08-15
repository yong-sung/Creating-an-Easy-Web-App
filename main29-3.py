import streamlit as st
import datetime
import pyupbit

# API 키 설정
access_key = "YOUR_ACCESS_KEY"
secret_key = "YOUR_SECRET_KEY"
upbit = pyupbit.Upbit(access_key, secret_key)  # UPbit API에 접근할 수 있는 객체 생성

ticker = "BTC-KRW"  # 원하는 암호화폐 티커 입력

d = st.date_input("날짜를 선택하세요", datetime.date.today())

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d + datetime.timedelta(days=1))
count = 24
price_data = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count) # 지정한 거래 쌍, 간격, 종료 날짜 및 개수로 가격 데이터를 가져옴.

st.line_chart(price_data['close'])

# 실행 방법: main29-3.py 우클릭 후, 통합터미널에서 열기 -> streamlit run main29-3.py
