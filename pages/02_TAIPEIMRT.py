# 檔案: pages/02_TAIPEIMRT.py

import solara
# 使用 MapLibreGL 後端，因為它在你環境中運行成功
import leafmap.maplibregl as leafmap 

# 修正後的 GeoJSON 原始連結 (Raw URL)
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

@solara.component
def Page():
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    # 這裡可以保留 @solara.use_memo 來優化性能 (雖然在你最新的截圖中似乎有 use_memo 的錯誤，
    # 但這個錯誤可能是因為 add_geojson 的 TypeError 引起的，我們先保留 use_memo)
    @solara.use_memo 
    def create_mrt_map():
        taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
        
        m = leafmap.Map(
            center=(taipei_lat, taipei_lon), 
            zoom=10, 
            height="750px",
        )
        
        # 設置作業要求的暗色底圖
        m.add_basemap("CartoDB.DarkMatter")
        
        # 【關鍵修正：移除 in_geojson=】
        # 直接將 URL 變數作為第一個位置參數傳入
        m.add_geojson(
            MRT_ROUTES_URL,  # <--- 這裡不再寫 in_geojson=
            layer_name="臺北捷運",
            style={'color': '#00BFFF', 'weight': 3, 'opacity': 0.9}, 
        )
        return m
        
    mrt_map = create_mrt_map()
    
    # 顯示地圖
    return mrt_map.to_solara()