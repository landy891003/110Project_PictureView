# 110Project_PictureView

使用:
 - PyQt5  
 - PIL
 - opencv


檔案架構:
- main.ui → main.py → (Func) MainWindow.py
- running.ui → running.py → (Func) RunningWindow.py
- illustrate.ui → illustrate.py →(Func) IllustrateWindow.py 
- controller.py : 控制跳轉頁面
- start.py : 開啟程式

已利用pyinstaller打包成.exe 在 dist 中，命名為start.py

2022.03.28
－建立基礎架構:
(1) 進入→流程→圖片編輯(開啟檔案、座標點觸發事件、放大縮小)→儲存圖片檔案
