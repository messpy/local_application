#pip speedtest-cli
import speedtest 

st = speedtest.Speedtest()
st.get_best_server()

# 速度測定を実行
download_speed = st.download() / 1024 / 1024  # Mbpsに変換
upload_speed = st.upload() / 1024 / 1024  # Mbpsに変換
ping = st.results.ping

print("[測定結果]")
print(f"download_speed: {download_speed}Mbps")
print(f"upload_speed: {upload_speed}Mbps")
print(f"ping: {ping}ms")
