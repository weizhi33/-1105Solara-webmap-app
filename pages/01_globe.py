# 檔案: pages/01_globe.py

import solara
import leafmap.leafmap as leafmap
from ipyleaflet import basemaps
import json
from pathlib import Path

TAIPEI_CENTER = (25.0330, 121.5654) 
# 注意：在 pages/ 目錄中，相對路徑應該是找到根目錄下的檔案
# 如果在 HF Space 中讀取失敗，您可能需要使用絕對路徑或調整讀取方式。
# 這裡我們暫時假設相對路徑 Path("../routes.geojson") 或 Path("routes.geojson") 可以奏效，
# 但由於 routes.geojson 在根目錄，通常 Path("../routes.geojson") 更保險。
# 為了簡化，我們嘗試使用根目錄 Path("routes.geojson")，這是 HF 推薦的相對路徑方式。
MRT_FILE_PATH = Path("routes.geojson") 

def load_geojson_data(file_path: Path):
    if not file_path.exists():
        print(f"⚠️ 錯誤：GeoJSON 檔案未找到於 {file_path}。請檢查檔案路徑。")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"❌ 載入 GeoJSON 檔案失敗: {e}")
        return None

class MapApp(solara.component):
    
    def __call__(self):
        """Solara 元件的渲染方法。Hooks 必須在這裡調用。"""
        
        # 1. 在渲染方法內部調用 use_memo 載入 GeoJSON 數據
        geojson_data = solara.use_memo(lambda: load_geojson_data(MRT_FILE_PATH), [])
        
        # 2. 在渲染方法內部調用 use_memo 建立地圖實例
        m = solara.use_memo(lambda: leafmap.Map(
            center=TAIPEI_CENTER, 
            zoom=12,
            basemap=basemaps.CartoDB.DarkMatter,
        ), [])
        
        # 3. 使用 use_effect 在地圖和數據準備好之後加入圖層
        @solara.use_effect(dependencies=[m, geojson_data])
        def add_mrt_layer():
            if m and geojson_data:
                try:
                    m.add_geojson(
                        geojson_data, 
                        layer_name="台北捷運" # 圖層名稱
                    )
                    m.add_layers_control()
                except Exception as e:
                    print(f"❌ 加入 GeoJSON 圖層失敗: {e}")

        
        # 渲染 Solara 介面
        return solara.Column(
            [
                solara.Markdown("## 🗺️ 台北捷運路網 Solara 地圖應用"),
                solara.Figure(m, height="600px")
            ]
        )