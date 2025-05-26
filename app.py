import streamlit as st
#from streamlit_player import st_player

#st.title('Salasar News')

# Sample video dictionary (replace with your video data)
DEFAULT_WIDTH = 80
videos = {
    "Video 1": "https://youtu.be/ts4GIKcB1B8?si=ELRg6Wls-p3wDuD6",
    "Video 2": "https://youtu.be/Bm5BL_AzhB0?si=XeoPq9BfoiRgzH_4",
    "Video 3": "https://youtu.be/SH6CM8J62rw?si=R6FIKlhY0pYalEo5",
    "Video 4": "https://youtu.be/5laj9ytQPQ8?si=81urG-Aw41b0kQYQ",
    "Video 5": "https://youtu.be/iEpqNw15GNk?si=ThnM3z1vQsH7LwsZ",
    "Video 6": "https://youtu.be/2lONW_4wL8c?si=vPrABqjSGv02p7pf"
}

st.set_page_config(layout="wide")
#st.title('Salasar News')
st.markdown("<h1 style='text-align: center; color: red;'>Salasar News</h1>", unsafe_allow_html=True)
# Get selected video title from sidebar
#st.sidebar.markdown("<h2 style='text-align: center; color: Red;'>Welcome To <h2 style='text-align: center; color: Blue;'> Salasar News</h1>", unsafe_allow_html=True)
st.sidebar.markdown(":red[Welcome to]    **:blue[Salasar News]**  ")
#st.sidebar.header("Welcome To Salasar News")
selected_video = st.sidebar.selectbox(":red[Select Video]", list(videos.keys()))

#width size
width = st.sidebar.slider(
    label=":blue[Width]", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
)
width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)
_, container, _ = st.columns([side, width, side])


# Get video path based on selection
video_path = videos[selected_video]

# Display video on main page
#st_player(video_path)
container.video(data=video_path)