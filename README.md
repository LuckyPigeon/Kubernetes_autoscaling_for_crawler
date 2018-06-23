# Kubernetes
Using kubernetes to autoscale crawler doing crawling

### Slide URL
[利用Kubernetes進行自動化大規模網站爬蟲](https://docs.google.com/presentation/d/12jGGQHKwuOInzwsyK6PQrqG53X0SVJCUU7FBWuuHZCQ/edit#slide=id.g3c7567ae6a_0_10)

### Kubernetes手把手

### 爬蟲手把手
* Requirement: 
    * mysql-connector==2.1.6
    * selenium==3.4.3
    * beautifulsoup4==4.6.0
    * Flask==0.12.2
* 選定自己喜歡的selenium driver(Chrome, Firefox, PhantomJS ...)，本範例採用Chrome driver
* 開始爬蟲
* 分析Youtube URL，發現搜尋query的共同部分=>https://www.youtube.com/results?search_query=\<keyword\>
* 在Youtube搜尋頁面鍵入keyword，開始觀察需要爬的資料(url and description)的pattern
* 發現我們的搜尋結果對應到的source是twoColumnSearchResultsRenderer
* ![](https://i.imgur.com/fDUZBj7.png)
* 進一步觀察發現description就在title下的accessibility下的accessibilityData下的label裡面，為了與其他label區分，所以使用"title":{"accessiblity這樣的pattern來過濾
* ![](https://i.imgur.com/BTHEohX.png)
* 而url的部分就很簡單地以Youtube特有的pattern /watch=?來過濾
* ![](https://i.imgur.com/r530iIK.png)

### 踩雷
* --pod-cidr flannel network -> flannel network should match the pod network CIDR
* [kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) -> 讓隱私資料以加密的方式呈現
* [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) -> 讓Kubernetes的pods可以共享資料
* mysql CrashLoopBackOff -> 沒打帳號密碼
* [HPA Current CPU Utilization:%](https://github.com/kubernetes-incubator/kube-aws/issues/549)
* emoji -> mysql預設是latin1，只要一碰到中文字或是emoji就炸了
* [build dockerfile的時候解析不出domain name](https://goo.gl/D3qWQ7) -> DNS 8.8.8.8 出了點狀況
* [Docker build with Flask](http://containertutorials.com/docker-compose/flask-simple-app.html)
* headless chrome -> 無視窗開啟Chrome，在selenium driver 設定上也要設定disable-gpu
* chrome driver的參數可以設置 chrome_options與execute_path前面那個就是設定headless chrome的地方
* urlopen、PhantomJS等文字瀏覽器page_source與Chrome、Firefox等圖形瀏覽器源碼不同
