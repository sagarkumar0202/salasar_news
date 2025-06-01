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


import pandas as pd
import numpy as np
import random
from datetime import date
from datetime import datetime
from datetime import time

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  
# Same as st.write(df)

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))


df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)


df = pd.DataFrame(
    {
        "Date": [date(2024, 1, 1), date(2024, 2, 1), date(2024, 3, 1)],
        "Total": [13429, 23564, 23452],
    }
)
df.set_index("Date", inplace=True)

config = {
    "_index": st.column_config.DateColumn("Month", format="MMM YYYY"),
    "Total": st.column_config.NumberColumn("Total ($)"),
}

st.dataframe(df, column_config=config)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
)

event.selection


df1 = pd.DataFrame(
    np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
)

my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
)

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.


my_chart = st.vega_lite_chart(
    {
        "mark": "line",
        "encoding": {"x": "a", "y": "b"},
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)

data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
            required=True,
        )
    },
    hide_index=True,
)


data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Views By Your Salasar channel",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)

data_df = pd.DataFrame(
    {
        "birthday": [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Reporter Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)

data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.TimeColumn(
            "Last 4 Views time on your channel",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
        ),
    },
    hide_index=True,
)


data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
           [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ListColumn(
            "View in (last 6 months)",
            help="View in the last 6 months",
            width="medium",
        ),
    },
    hide_index=True,
)