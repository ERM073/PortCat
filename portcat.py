import socket
import time

print("""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ptc|  |  |  |  |  |  |  |  |  |  |  portcat
               GitHub.com/ERM073
""")

while True:
    # スキャンするホスト名またはIPアドレス
    print("-------------------------------------------")
    host = input("対象のIP address: ")

    # 開始ポート番号
    start_port = int(input("何番ポートからスキャンしますか? 0: "))

    # 終了ポート番号
    end_port = int(input("何番ポートまでスキャンしますか? 100: "))



    # ポートスキャン
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} が開いています")
            sock.close()
