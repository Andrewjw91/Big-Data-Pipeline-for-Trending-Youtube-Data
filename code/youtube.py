
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,date
import seaborn as sns
from sqlalchemy import create_engine
engine = create_engine("sqlite:///youtube.db")

#----

st.title('YouTube Trending Video Data By Country')

#SideBar
st.sidebar.header('Filters')
#Country Select
country = st.sidebar.selectbox('Pick a country to show some info about',('BR', 'CA', 'DE', 'FR', 'GB', 'IND', 'JP', 'KR', 'MX', 'RUS', 'US'))
#Category Select
category = st.sidebar.selectbox('Pick a Video Category', ('ALL', 'Autos & Vehicles', 'Comedy', 'Education', 'Entertainment', 'Film and Animation', 'Gaming', 'Howto & Style', 'Music', 'News & Politics', 'Nonprofits & Activism', 'People & Blogs', 'Pets & Animals', 'Science & Technology', 'Sports', 'Travel & Events'))
#
st.sidebar.markdown('''---''')
#Date Select
st.sidebar.header('Pick a date range')
date_data = pd.read_sql('SELECT * FROM {}'.format(country), engine)
df = date_data
df['trending_date'] = pd.to_datetime(df['trending_date'])


start_date = st.sidebar.date_input(label='Start date', min_value= df['trending_date'].min(), max_value= df['trending_date'].max(), value= df['trending_date'].min())
end_date = st.sidebar.date_input(label='End date', min_value= df['trending_date'].min(), max_value= df['trending_date'].max(), value= df['trending_date'].max())
if start_date > end_date:
    st.error('Error: End date must fall after start date.')


#Category: ID Key Mapping
cat_dict = {'Autos & Vehicles': 2, 'Comedy': 23, 'Education': 27,
'Entertainment': 24, 'Film and Animation': 1, 'Gaming': 20,
'Howto & Style': 26, 'Music': 10, 'News & Politics': 25,
'Nonprofits & Activism': 29, 'People & Blogs': 22,
'Pets & Animals': 15, 'Science & Technology': 28,
'Sports': 17, 'Travel & Events': 19}

# Top Trending Categories
button = st.button('Top Trending Video Categories')

if button:
    st.write(
    '''
    ## Top Trending Video Categories in {}    
    '''.format(country))

    data = pd.read_sql('''SELECT {0}.categoryId, COUNT({0}.categoryId) as video_count, category_name FROM {0}
        LEFT JOIN categories c ON {0}.categoryId = c.categoryId
        GROUP BY category_name
        ORDER BY video_count DESC'''.format(country), engine)
    fig, ax = plt.subplots()
    sns.barplot(data=data, x='video_count', y='category_name', ax=ax)
    ax.set(xlabel='Trending Frequency', ylabel='')
    st.pyplot(fig)

# Most Frequent Trending Channels
button2 = st.button('Top Channels By Category')

if button2:
    if category == 'ALL':
        st.write('## Top Trending Channels (ALL Categories)')
        frequent_channels = pd.read_sql('''SELECT channelTitle, COUNT(channelTitle), trending_date FROM {0}
            GROUP BY channelTitle
            ORDER BY COUNT(channelTitle)
            DESC LIMIT 15'''.format(country), engine)

        fig, ax = plt.subplots()
        sns.barplot(data=frequent_channels, x='COUNT(channelTitle)', y='channelTitle', ax=ax)
        ax.set(xlabel='Trending Frequency', ylabel='')
        st.pyplot(fig)
    else:
        st.write('## Top {} Channels'.format(category))
        frequent_channels = pd.read_sql('''SELECT channelTitle, COUNT(channelTitle) FROM {0}
            WHERE categoryId = {1}
            GROUP BY channelTitle
            ORDER BY COUNT(channelTitle)
            DESC LIMIT 10'''.format(country, cat_dict[category]), engine)

        fig, ax = plt.subplots()
        sns.barplot(data=frequent_channels, x='COUNT(channelTitle)', y='channelTitle', ax=ax)
        ax.set(xlabel='Trending Frequency', ylabel='')
        st.pyplot(fig)
#





    