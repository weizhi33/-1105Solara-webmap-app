# 檔案: pages/02_TAIPEIMRT.py (最終修正版)

import solara
# 這裡使用 MapLibreGL 後端，這是因為在你環境中它才能成功運行並繞過各種錯誤。
# 如果老師特別要求 ipyleaflet，請在成功運行後再向老師說明兼容性問題。
import leafmap.maplibregl as leafmap 

# GeoJSON 原始連結 (Raw URL)，已修正 master 分支和 routes.geojson 檔名
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

def create_map():
    # 這是實際創建地圖的邏輯
    taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
    
    m = leafmap.Map(
        center=(taipei_lat, taipei_lon), 
        zoom=10, 
        height="750px",
    )
    
    # 設置作業要求的暗色底圖
    m.add_basemap("CartoDB.DarkMatter")
    
    # 修正 add_geojson 參數：
    # 1. 移除 in_geojson= (解決 TypeError: missing 'data')
    # 2. 移除 style={...} (解決 Pydantic validation error)
    m.add_geojson(
        MRT_ROUTES_URL,
        name="臺北捷運", # 這裡使用 name
    )
    return m


@solara.component
def Page():
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    # 【修正 'Map' object is not callable 錯誤】
    # 直接呼叫 create_map 函式，並將結果賦予 mrt_map 變數
    mrt_map = create_map() 
    
    # 顯示地圖：使用 MapLibreGL 的正確顯示方法
    return mrt_map.to_solara()