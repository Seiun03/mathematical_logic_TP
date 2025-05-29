import streamlit as st
from util.database import run_query
from datetime import datetime

# ---------- 공통 세션 키 초기화 ----------
if "board" not in st.session_state:
    st.session_state.board = "글 목록"
if "write_mode" not in st.session_state:
    st.session_state.write_mode = False
if "view_post" not in st.session_state:
    st.session_state.view_post = None
# --------------------------------------

def sidebar_set():
    menu = st.sidebar.selectbox("메뉴", ["글 목록", "글 작성"])
    st.session_state.board = menu          # 한 줄로 단순화

def delete_post():
    run_query(
        "DELETE FROM posts WHERE id = %s",
        (st.session_state.view_post,),      # ← 반드시 (값 ,) 형식
        fetch=False
    )
    st.toast("글이 삭제되었습니다.", icon=":material/done:")
    st.rerun()

def commit_post(post_id, comment, name):
    run_query(
        "INSERT INTO comments (post_id, name, comment) VALUES (%s, %s, %s)",
        (post_id, name, comment),
        fetch=False
    )
    st.toast("댓글이 등록되었습니다.", icon=":material/done:")

def delete_comment(comment_id):
    run_query(
        "DELETE FROM comments WHERE id = %s",
        (comment_id,),
        fetch=False
    )
    st.toast("댓글이 삭제되었습니다.", icon=":material/done:")
    st.rerun()

def show_list():
    posts = run_query("SELECT * FROM posts ORDER BY id DESC")
    if posts is None:
        st.info("게시된 글이 없습니다.")
        return

    for _, p in posts.iterrows():
        with st.expander(f"{p['title']} - {p['created_at']}"):
            st.write(p["content"])

            # ───────── 자세히 보기 ─────────
            if st.button("자세히 보기", key=f"view_{p['id']}"):
                st.session_state.view_post = int(p["id"])
                st.rerun()      # detail 화면으로 즉시 이동

            # ───────── 글 상세 화면 ─────────
            if st.session_state.view_post == p["id"]:
                detail = run_query(
                    "SELECT * FROM posts WHERE id = %s",
                    (p["id"],)
                )
                d = detail.iloc[0]
                st.subheader(d["title"])
                st.write(d["content"])
                st.caption(f"작성일: {d['created_at']}")

                # 글 삭제
                if d["name"] == st.session_state.name:
                    st.button("글 삭제", on_click=delete_post, key=f"del_post_{p['id']}")

                st.markdown("---")
                st.markdown("#### 댓글")

                # ----- 댓글 입력 -----
                with st.form(key=f"comment_form_{p['id']}", clear_on_submit=True):
                    new_comment = st.text_input("댓글 작성", key=f"new_comment_{p['id']}")
                    submitted = st.form_submit_button("댓글 등록")
                    if submitted:
                        if new_comment.strip():
                            commit_post(p["id"], new_comment.strip(), st.session_state.name)
                            st.rerun()
                        else:
                            st.warning("내용을 입력해주세요.")

                # ----- 댓글 목록 -----
                comments = run_query(
                    "SELECT * FROM comments WHERE post_id = %s ORDER BY id ASC",
                    (p["id"],)
                )
                if comments is not None:
                    for _, c in comments.iterrows():
                        st.write(f":material/chat: {c['comment']} (작성자: {c['name']}, {c['created_at']})")
                        if c["name"] == st.session_state.name:
                            st.button(
                                "삭제",
                                key=f"del_comment_{c['id']}",
                                on_click=delete_comment,
                                args=(c["id"],),
                                type="secondary",
                                use_container_width=True,
                                help="내가 쓴 댓글 삭제"
                            )

def show_write():
    if st.session_state.write_mode:
        with st.form("글쓰기", clear_on_submit=True):
            title = st.text_input("제목")
            content = st.text_area("내용", height=400)
            submitted = st.form_submit_button("작성 완료")
            if submitted:
                if title and content:
                    run_query(
                        "INSERT INTO posts (title, content, name) VALUES (%s, %s, %s)",
                        (title, content, st.session_state.name),
                        fetch=False
                    )
                    st.toast("게시글이 등록되었습니다.", icon=":material/done:")
                    st.session_state.write_mode = False
                    st.rerun()
                else:
                    st.warning("모든 필드를 입력해주세요.")

def show_board():
    if not st.session_state.log_in:
        st.error("로그인 후 이용 가능한 서비스입니다.")
        return

    sidebar_set()

    if st.session_state.board == "글 목록":
        show_list()
    else:
        st.session_state.write_mode = True
        show_write()
