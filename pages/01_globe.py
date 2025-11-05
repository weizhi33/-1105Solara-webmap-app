import solara
import leafmap.leafmap as leafmap
from ipyleaflet import basemaps
import json
from pathlib import Path

# 📌 台北的中心座標 (緯度, 經度)
TAIPEI_CENTER = (25.0330, 121.5654) 
# 假設 GeoJSON 檔案與 app.py 在同一目錄下
MRT_FILE_PATH = Path("routes.geojson")

def load_geojson_data(file_path: Path):
    """從本地檔案載入 GeoJSON 資料，供 ipyleaflet 使用。"""
    if not file_path.exists():
        # 在部署環境中，如果檔案不存在會印出此訊息
        print(f"⚠️ 錯誤：GeoJSON 檔案未找到於 {file_path}。")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"GeoJSON 檔案已成功載入：{file_path}")
        return data
    except Exception as e:
        print(f"❌ 載入 GeoJSON 檔案失敗: {e}")
        return None

class MapApp(solara.component):
    
    # 1. 僅載入一次 GeoJSON 數據，並將其轉為 Python 字典/列表
    geojson_data = solara.use_memo(lambda: load_geojson_data(MRT_FILE_PATH), [])
    
    # 2. 建立以台北為中心的暗色底圖
    m = solara.use_memo(lambda: leafmap.Map(
        center=TAIPEI_CENTER, 
        zoom=12,
        # 使用 CartoDB.DarkMatter 實現暗色底圖
        basemap=basemaps.CartoDB.DarkMatter,
    ), [])
    
    # 3. 在地圖和數據準備好之後加入圖層
    @solara.use_effect(dependencies=[m, geojson_data])
    def add_mrt_layer():
        if self.m and self.geojson_data:
            try:
                # 使用 m.add_geojson 方法加入 GeoJSON 資料 (字典格式)
                # 實現：使用 m.add_geojson(url, layer_name="台北捷運") 加入圖層。
                self.m.add_geojson(
                    self.geojson_data, 
                    layer_name="台北捷運" # 圖層名稱
                )
                print("台北捷運路網 GeoJSON 圖層已成功加入。")
                # 可選：加入圖層控制，方便使用者開關圖層
                self.m.add_layers_control()
            except Exception as e:
                print(f"❌ 加入 GeoJSON 圖層失敗: {e}")


    def __call__(self):
        """Solara 元件的渲染方法"""
        
        # 渲染 Solara 介面
        return solara.Column(
            [
                solara.Markdown("## 🗺️ 台北捷運路網 Solara 地圖應用"),
                solara.Markdown(
                    "此地圖使用 **leafmap** (ipyleaflet 後端) 和 **CartoDB.DarkMatter** 暗色底圖。"
                ),
                # 渲染地圖
                # 設定高度確保地圖能正常顯示
                solara.Figure(self.m, height="600px")
            ]
        )