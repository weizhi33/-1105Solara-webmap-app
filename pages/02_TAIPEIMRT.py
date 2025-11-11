# 檔案: pages/02_TAIPEIMRT.py (使用 MapLibreGL 後端)

import solara
import leafmap.maplibregl as leafmap  # <-- 關鍵修正 1: 使用 maplibregl 後端

# 臺北捷運路線 GeoJSON 檔案的原始 URL (使用你找到的正確連結)
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

# 將地圖創建邏輯放在一個簡單的函數中
def create_map():
    # 設置你需要的中心點、縮放級別和樣式
    # 這裡使用同學的設定值，以確保程式碼能運行
    m = leafmap.Map(
        center=(121.55555, 25.08722), 
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron", # 預設樣式
        height="750px",
        sidebar_visible=False,
    )
    
    # 設置作業要求的暗色底圖 (CartoDB.DarkMatter)
    m.add_basemap("CartoDB.DarkMatter")
    
    # 載入 GeoJSON 資料 (直接將 URL 作為第一個參數)
    # 註：這裡使用 m.add_geojson(url, name=...)，而不是 m.add_geojson(in_geojson=...)
    m.add_geojson(MRT_ROUTES_URL, name="臺北捷運")
    
    return m

# Solara 組件
@solara.component
def Page():
    # 創建地圖物件
    m = create_map()
    
    # 顯示地圖：使用 Leafmap 專為 Solara 提供的顯示函式
    return m.to_solara()  # <-- 關鍵修正 2: 使用 m.to_solara() 顯示地圖