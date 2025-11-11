# 檔案: pages/02_TAIPEIMRT.py (最終修正版，移除 use_memo 以避免 TypeError)

import solara
import leafmap.maplibregl as leafmap 

# GeoJSON 原始連結 (Raw URL)
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

def create_map():
    # 這裡是實際創建地圖的邏輯
    taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
    
    m = leafmap.Map(
        center=(taipei_lat, taipei_lon), 
        zoom=10, 
        height="750px",
    )
    
    m.add_basemap("CartoDB.DarkMatter")
    
    # 解決 Pydantic 錯誤：只傳入 URL 和 name
    m.add_geojson(
        MRT_ROUTES_URL,
        name="臺北捷運",
    )
    return m


@solara.component
def Page():
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    # 這裡直接呼叫 create_map 函式，並將結果賦予 mrt_map 變數
    mrt_map = create_map() 
    
    # 顯示地圖
    return mrt_map.to_solara()