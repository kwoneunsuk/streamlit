import streamlit as st


st.set_page_config(
    page_title='포켓몬 도감',
    page_icon='./images/monsterball.png')


st.title('hello streamlit')
st.subheader('포켓몬 도감')
st.text('포켓몬 도감을 추가해서 도감을 채워보세요')
st.markdown('**마크다운** 기능을 적용해보세요.')

pokemons = [
    {
        'name' :'누오',
        'image_url' :'https://i.namu.wiki/i/xRW3MoL3xUKlBgrV1-jnC7xuwvHHgoF0Xvxort7gD7YydvigWSO4gSuL1B-k-Y-cioI5kZ2GL4SEp0bJs2NCxS371jr9ylwxV8bw3oIL8HSXa2Aec7oUfFwBfE1wR9vZEZ78wTH4sYEthlR7QC3N5g.webp'
    },
    {
        'name' :'피카추',
        'image_url' :'https://i.namu.wiki/i/ksLBuLqR52CAPQU0bSPRUWTJasduzwcSXyxVD-pxjoHiNdabf9_J-oCEDT7V2jV6ETloF3V4CvBs3vhciUgawRGq-lq_W9dLVq2GxcKyOKT4Io8zYfgScYjDZF-1yXpgoLuxxSjJ0iSYkyxA2RSuhQ.webp'
    },
    {
        'name': '피카추',
        'image_url': 'https://i.namu.wiki/i/ksLBuLqR52CAPQU0bSPRUWTJasduzwcSXyxVD-pxjoHiNdabf9_J-oCEDT7V2jV6ETloF3V4CvBs3vhciUgawRGq-lq_W9dLVq2GxcKyOKT4Io8zYfgScYjDZF-1yXpgoLuxxSjJ0iSYkyxA2RSuhQ.webp'
    },
]

cols = st.columns(3)

for i in range(3) :
    with cols[i] :
        pokemon=pokemons[i]
        with st.expander(label=pokemon['name'], expanded=True) :
            st.subheader(pokemon['name'])
            st.image(pokemon['image_url'])
