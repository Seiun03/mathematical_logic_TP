import streamlit as st
from util.database import *
from datetime import datetime

def sidebar_set():
    menu = st.sidebar.selectbox("메뉴", ["글 목록", "글 작성"])
    if menu == "글 목록":
        st.session_state['board'] = "글 목록"
    elif menu == "글 작성":
        st.session_state['board'] = "글 작성"

def write_check():
    if st.session_state.write_mode != True:
        st.session_state.write_mode = True
    show_write()

#게시글 삭제
def delete_post():
    run_query("DELETE FROM posts WHERE id = %s", (st.session_state['view_post']), fetch=False)
    st.toast(f"{st.session_state.name}님이 작성하신 글의 삭제가 완료되었습니다.", icon = ":material/done:")

#댓글 등록
def commit_post(post_id, comment, name):
    run_query("INSERT INTO comments (post_id, name, comment) VALUES (%s, %s, %s)", (post_id, name, comment), fetch=False)
    st.toast(f"댓글이 등록되었습니다.", icon = ":material/done:")

#댓글 삭제
def delete_comment(post_id):
    run_query("DELETE FROM comments WHERE id = %s", (post_id,), fetch = False)
    st.toast(f"{st.session_state.name}님이 작성하신 댓글 삭제가 완료되었습니다.", icon = ":material/done:")

#게시글 목록록
def show_list():
    lists = run_query("SELECT * FROM posts ORDER BY id DESC")
    if lists is None: 
        st.info("게시된 글이 존재하지 않습니다.")
        return
    st.subheader("게시글 목록")
    for _, post in lists.iterrows():
        
        with st.expander(f"{post['title']} - {post['created_at']}"):
            st.session_state['view_post'] = post['id']
                
            if st.session_state['view_post'] == post['id']:
                post = run_query("SELECT * FROM posts WHERE id = %s", (st.session_state['view_post']))
            #-------글 내용-------
                st.subheader(post['title'].iloc[0])
                st.write(post['content'].iloc[0])
                st.caption(f"작성일: {post['created_at'].iloc[0]} / 작성자: {post['name'].iloc[0]}")
                if post['name'].iloc[0] == st.session_state.name:
                    st.button("글 삭제", icon = ":material/close:", on_click=delete_post, key=f"del_post_{post['id']}")

            #-----------댓글------------
                st.markdown('---')
                st.markdown('##### 댓글')
                comment = run_query("SELECT * FROM comments WHERE post_id = %s ORDER BY id ASC", (st.session_state['view_post'],))
                if comment is not None:
                    for _, com in comment.iterrows():
                        left, right = st.columns((10, 1.0))
                        with left:
                            st.write(f":material/chat: {com['comment']} (작성자 : {com['name']}, {com['created_at']})")
                        if com['name'] == st.session_state.name:
                            with right:
                                st.button("삭제", key=f"del_comment_{com['id']}", icon=":material/close:", on_click=delete_comment, args = (com['id'],))
                with st.form(key = f"comment_form_{post['id']}", clear_on_submit=True):
                    new_comment = st.text_input("댓글 작성",key = f"new_comment_{post['id']}")
                    submitted = st.form_submit_button("댓글 등록", icon = ":material/edit:")
                    if submitted:
                        if new_comment.strip():
                            commit_post(st.session_state['view_post'], new_comment.strip(), st.session_state.name)
                            
                        else:
                            st.toast("내용을 입력해주세요.", icon = ":material/block:")
                
                

def show_write():
    if st.session_state.write_mode:
        st.subheader("게시글 작성")
        st.markdown('')
        with st.form("글쓰기"):
            title = st.text_input('제목', placeholder = "제목")
            content = st.text_area("내용", height = 500)
            submit = st.form_submit_button("작성 완료")
            if submit:
                if title and content:
                    run_query('INSERT INTO posts (title, content, name) VALUES (%s, %s, %s)', (title, content, st.session_state.name), fetch = False)
                    st.toast("게시글 등록이 완료되었습니다.", icon = ":material/done:")
                else:
                    st.toast("모든 필드를 입력해주세요.", icon = ":material/block:")
    

def show_board():
    if st.session_state.log_in:
        sidebar_set()
        if st.session_state['board'] == "글 목록":
            show_list()
        else:
            show_write()
    else:
        st.error("로그인 후 이용가능한 서비스입니다.")