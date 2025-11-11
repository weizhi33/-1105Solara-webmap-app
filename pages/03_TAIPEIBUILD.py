# 檔名: 03_3D台北建築圖.py
import solara
import leafmap.maplibregl as leafmap

# 台北市中心坐標 (接近信義區/市政府)
TAIPEI_CENTER = [121.56, 25.03] 

def create_map():
    """
    根據頁面要求建立 Leafmap (MapLibre GL) 地圖。
    - 使用 CartoDB Positron 底圖 (style="positron")。
    - 實作台北 3D 建築圖層。
    """
    
    # 1. 使用 leafmap.Map 建立地圖 (它預設已是 MapLibre GL backend)
    # style="positron" 直接使用 CartoDB Positron 免費底圖
    m = leafmap.Map(
        center=TAIPEI_CENTER, # 將中心稍微調整到更靠近台北市中心
        zoom=15.5, # 適當的縮放級別
        pitch=60, # 傾斜角度，營造 3D 效果
        bearing=-17, # 地圖旋轉角度
        style="positron", # CartoDB Positron 底圖
        height="750px",
        sidebar_visible=False, # 預設關閉側邊欄，讓地圖更純粹
    )
    
    # 2. 實作台北 3D 建築圖層
    # leafmap.add_overture_3d_buildings 使用 Overture Maps 的全球建築資料
    # 使用 'simple' 模板，這是一個預設樣式，通常不需要 Mapbox Token
    m.add_overture_3d_buildings(
        template="simple",
        name="Overture 3D Buildings" # 給圖層一個名稱
    )
    
    # 加上一個圖層控制，方便查看圖層（選用）
    m.add_layer_control() 
    
    return m

@solara.component
def Page():
    """
    Solara 頁面組件，用於顯示 Leafmap 地圖。
    """
    m = create_map()
    
    # 將 Leafmap 對象轉換為 Solara 組件
    return m.to_solara()