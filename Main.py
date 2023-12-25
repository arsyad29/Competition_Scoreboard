import streamlit as st
import time

# Catatan widget bagus:
# https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/
# Incremeant plus minus
# https://blog.streamlit.io/session-state-for-streamlit/

# Set background

st.title("English First")
left_column, middle_column, right_column = st.columns(3)
with left_column:
    tim1 = st.text_input('Input Team 1 name')
with middle_column:
    tim2 = st.text_input('Input Team 2 name')
with right_column:
    tim3 = st.text_input('Input Team 3 name')

left_column, middle_column, right_column = st.columns(3)
with middle_column:
    st.title('Timer')
    if st.button("Reset Timer"):
        st.empty()
    if st.button('Star Timer'):
        ph = st.empty()
        N = 15
        for secs in range(N,0,-1):
            mm, ss = secs//60, secs%60
            ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
            time.sleep(1)

st.title("Competition")
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title(f'{tim1}')
    if 'score_tim1' not in st.session_state:
    	st.session_state.score_tim1 = 0
    # Plus button
    pluss_but1 = st.button('Correct!')
    if pluss_but1:
        st.session_state.score_tim1 += 100
    # Minus button
    min_but1 = st.button('Wrong!')
    if min_but1:
        st.session_state.score_tim1 -= 50
    # Print button
    st.title(st.session_state.score_tim1)

with middle_column:
    st.title(f'{tim2}')
    if 'score_tim2' not in st.session_state:
    	st.session_state.score_tim2 = 0
    # Plus button
    pluss_but2 = st.button('Correct! ')
    if pluss_but2:
        st.session_state.score_tim2 += 100
    # Minus button
    min_but2 = st.button('Wrong! ')
    if min_but2:
        st.session_state.score_tim2 -= 50
    # Print button
    st.title(st.session_state.score_tim2)

with right_column:
    st.title(f'{tim3}')
    if 'score_tim3' not in st.session_state:
    	st.session_state.score_tim3 = 0
    # Plus button
    pluss_but3 = st.button('Correct!  ')
    if pluss_but3:
        st.session_state.score_tim3 += 100
    # Minus button
    min_but3 = st.button('Wrong!  ')
    if min_but3:
        st.session_state.score_tim3 -= 50
    # Print button
    st.title(st.session_state.score_tim3)


left_column, middle_column, right_column = st.columns(3)
with middle_column:
    if st.button('Reset All Score'):
        st.session_state.score_tim1 = 0
        st.session_state.score_tim2 = 0
        st.session_state.score_tim3 = 0