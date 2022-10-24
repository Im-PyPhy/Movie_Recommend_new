import streamlit as st
import pickle
from helper import recommend_list

movies_df = pickle.load(open('df_final.pkl','rb'))
movies_df.head()

st.image('PngItem_1876144.png')
st.title('Movies Recommender')

st.write('')
st.write('')
st.write('')

movie =  st.selectbox('Select movie',movies_df['title'])



if st.button('Recommend'):
    Movies,Trailers,Posters = recommend_list(movie)
    col1, col2, col3, = st.columns(3)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    with col1:
        st.write(Movies[0][0])
        st.image(Posters[0])
        st.subheader('Genre')
        st.write(Movies[0][1])
        link = Trailers[0]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)

    with col2:
        st.write(Movies[1][0])
        st.image(Posters[1])
        st.subheader('Genre')
        st.write(Movies[1][1])
        link = Trailers[1]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)

    with col3:
        st.write(Movies[2][0])
        st.image(Posters[2])
        st.subheader('Genre')
        st.write(Movies[2][1])
        link = Trailers[2]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)

    col4, col5, col6, = st.columns(3)


    with col4:
        st.write(Movies[3][0])
        st.image(Posters[3])
        st.subheader('Genre')
        st.write(Movies[3][1])
        link = Trailers[3]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)

    with col5:
        st.write(Movies[4][0])
        st.image(Posters[4])
        st.subheader('Genre')
        st.write(Movies[4][1])
        link = Trailers[4]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)

    with col6:
        st.write(Movies[5][0])
        st.image(Posters[5])
        st.subheader('Genre')
        st.write(Movies[5][1])
        link = Trailers[5]
        link = f"[Trailer]{link}"
        st.markdown(link, unsafe_allow_html=True)
