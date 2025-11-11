# 檔案: pages/02_TAIPEIMRT.py (Solara 專用結構)
import solara
import leafmap.leafmap as leafmap 

# 臺北捷運路線 GeoJSON 檔案的原始 URL
MRT_ROUTES_URL = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/main/Taipei_MRT_Routes.geojson"

# 將所有邏輯封裝在 Solara 組件內
@solara.component
def Page():
    # 設置頁面標題
    solara.Title("02_2D 臺北捷運圖 (Solara)")
    
    # 使用 Solara 的 use_memo 確保地圖只創建一次，優化性能
    # use_memo 接受一個函式作為參數
    @solara.use_memo
    def create_mrt_map():
        # 1. 設定以臺北為中心、暗色底圖
        taipei_lat, taipei_lon, zoom = 25.03, 121.56, 10
        
        # 建立地圖實例 (這是 ipyleaflet 物件)
        m = leafmap.Map(
            center=(taipei_lat, taipei_lon), 
            zoom=zoom, 
            tiles='CartoDB.DarkMatter', # 作業要求：暗色底圖
        )
        
        # 2. 載入臺北捷運路網 (Vector)
        m.add_geojson(
            in_geojson=MRT_ROUTES_URL, 
            layer_name="臺北捷運",
            style={'color': '#00BFFF', 'weight': 3, 'opacity': 0.9}, 
        )
        return m
        
    mrt_map = create_mrt_map()
    
    # 顯示地圖：使用 Solara 的 ipywidgets 顯示器來顯示 Leafmap/ipyleaflet 物件
    # 這裡使用 solara.FigureSolara 來確保地圖能正確渲染並佔據空間
    solara.FigureSolara(mrt_map, height="600px")
    
# 如果你不需要複雜的佈局，只需在 Page() 之外調用它一次（在 Solara 中通常不是必需的）
# Page()