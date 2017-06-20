# Django_Lunch

在命令列把環境變數設起來：
```bash
export DJANGO_SETTINGS_MODULE=lunch.settings.local
```
不過環境變數每次重開終端機都會重設，很不方便。
所以可以在虛擬環境的 `activate` 指令裡加上這一行。打開 `venv/lunch/bin/activate`（Windows 是 `venv\lunch\Scripts\activate.bat`），在最後面新增一行，加入上面的指令。這樣你之後啟用虛擬環境時，就會自動更新環境變數了。
