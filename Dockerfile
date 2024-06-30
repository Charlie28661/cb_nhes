# 使用官方的 Python 基礎映像
FROM python:3.8

# 設置工作目錄
WORKDIR /app

# 複製應用程序代碼到容器中
COPY . /app

# 安裝應用程序依賴
RUN pip install -r requirements.txt
RUN pip install --upgrade Flask Werkzeug
RUN rm -r /root/.cache/pip

# 開放容器內的端口
EXPOSE 80

# 定義環境變數
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 啟動應用程序
CMD ["flask", "run", "--host=0.0.0.0"]