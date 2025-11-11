# 02_2D台北捷運圖.py
import streamlit as st
import leafmap.leafmap as leafmap

# 頁面標題
st.title("02_TAIPEIMRT") 

# 臺北捷運路線 GeoJSON 檔案的原始 URL
# 這是你從老師的 GitHub 倉庫中找到的路線檔案
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/main/Taipei_MRT_Routes.geojson"

# 1. 建立地圖實例
# 2. 設定以臺北為中心 (大約經緯度)
# 3. 使用暗色底圖 (CartoDB.DarkMatter)
taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10

m = leafmap.Map(
    center=(taipei_lat, taipei_lon), 
    zoom=zoom, 
    tiles='CartoDB.DarkMatter' # 作業要求：暗色底圖
)

# 4. 載入臺北捷運路網 (Vector)
m.add_geojson(
    in_geojson=MRT_ROUTES_URL, 
    layer_name="臺北捷運",
    # 建議加上樣式設定，讓線條在暗色底圖上更明顯
    style={'color': '#00BFFF', 'weight': 3, 'opacity': 0.9}, 
)

# 顯示地圖
m.to_streamlit(height=600)