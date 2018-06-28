# SOTA-backend


# [Sota-IOT](https://sota-iot.com)

主要要修改的sql部分在app.yaml檔案內
目前連接的project是sota-199909，cloudsql也是

### 需要安裝的套件都在requirements.txt

    目錄請自訂到該目錄的lib資料夾(自行新增)
    appengine_config.py會把lib中所有套件自動包含到專案內



另外要測試必須要上傳到GAE才進行測試
目前無法本地端測試，因連接cloudsql時是使用google的範例

部署時可以用指令或者GUI

## [這裡是GAE的GUI連結](https://cloud.google.com/appengine/docs/standard/python/download)

## [dashboard所使用的模板](https://startbootstrap.com/template-overviews/sb-admin-2/)

### ToDoList: 持續新增

    登入登出功能大致完成(還沒有session)
    登入後儀表板的配置
