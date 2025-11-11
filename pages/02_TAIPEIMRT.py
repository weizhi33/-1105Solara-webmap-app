# 檔案: pages/02_TAIPEIMRT.py

import solara
import leafmap.maplibregl as leafmap 

# 【關鍵修正】使用正確的原始連結 (Raw URL) 和檔案名稱 (routes.geojson)
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

@solara.component
def Page():
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    # 使用 use_memo 來創建地圖，以確保地圖物件在 Solara 中正確管理
    @solara.use_memo 
    def create_mrt_map():
        taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
        
        m = leafmap.Map(
            center=(taipei_lat, taipei_lon), 
            zoom=10, # 初始縮放使用 10 比較廣泛
            height="750px",
        )
        
        # 設定作業要求的暗色底圖
        m.add_basemap("CartoDB.DarkMatter")
        
        # 【關鍵修正】使用頂部定義的正確變數 MRT_ROUTES_URL
        m.add_geojson(
            in_geojson=MRT_ROUTES_URL, # 這裡使用變數
            layer_name="臺北捷運",
            style={'color': '#00BFFF', 'weight': 3, 'opacity': 0.9}, 
        )
        return m
        
    mrt_map = create_mrt_map()
    
    # 顯示地圖：使用 Leafmap 專為 Solara 提供的顯示函式
    return mrt_map.to_solara()