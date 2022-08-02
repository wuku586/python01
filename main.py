from flask import Flask, escape, request

app=Flask(__name__)   #__name__代表目前執行的模組


@app.route("/")    #函式的裝飾 (Decorator) 以函式為基礎,提供附加的功能          
def home():
    return "Hello Flask 123!"

#@app.route("/test")
#def test():
#    return "This is Test!"

if __name__ == "__main__":   #如果以主程式執行  
    #app.run(host='127.0.0.1', port=5000, debug=True)  #立即啟動伺服器
   app.run()