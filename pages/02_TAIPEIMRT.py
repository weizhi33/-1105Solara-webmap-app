# 檔案: pages/02_TAIPEIMRT.py

import solara
import leafmap.maplibregl as leafmap 
# 【注意】我們仍使用 MapLibreGL 後端，因為它在你環境中運行成功

# 修正後的 GeoJSON 原始連結 (Raw URL)
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

@solara.component
def Page():
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    @solara.use_memo 
    def create_mrt_map():
        taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
        
        m = leafmap.Map(
            center=(taipei_lat, taipei_lon), 
            zoom=10, 
            height="750px",
        )
        
        m.add_basemap("CartoDB.DarkMatter")
        
        # 【關鍵修正：移除 in_geojson=】
        m.add_geojson(
            MRT_ROUTES_URL,  # <--- 直接傳入 URL 變數
            layer_name="臺北捷運",
            style={'color': '#00BFFF', 'weight': 3, 'opacity': 0.9}, 
        )
        return m
        
    mrt_map = create_mrt_map()
    
    return mrt_map.to_solara()