# 檔案: pages/02_TAIPEIMRT.py

import solara
import leafmap.maplibregl as leafmap 

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
        
        # 【關鍵修正：將 layer_name 和 style 替換為 name 和 style_dict】
        m.add_geojson(
            MRT_ROUTES_URL,  # <--- URL 依然是第一個位置參數
            name="臺北捷運", # <--- 使用 'name' 替換 'layer_name'
            # 在 MapLibreGL 中，樣式參數是 style_dict，且它應為 GeoJSON 樣式規範。
            # 但由於錯誤顯示 style 也被拒絕，我們將樣式放在單獨的 add_layer 呼叫中，
            # 或者先完全移除 style 參數，讓它用預設樣式運行。
            # 我們先使用最精簡的版本來測試 GeoJSON 載入：
        )
        
        # 如果你成功運行，你可以用 m.add_layer_json() 這種 MapLibre 方式來添加樣式
        # 但為了通過 Pydantic 驗證，我們先用最簡潔的方式載入圖層
        
        return m
        
    mrt_map = create_mrt_map()
    
    return mrt_map.to_solara()