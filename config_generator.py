import json

ips = [
    '188.121.106.78',
  '37.32.6.159',
  '188.121.106.19',
  '37.32.31.236',
  '37.32.30.64',
  '37.32.31.249',
  '37.32.7.123',
  '37.32.6.17',
  '37.32.4.41']

inbounds = []
outbounds = []
routing = []
for i, ip in enumerate(ips):
    inbounds.append(
      {
        "tag": f"in-{i+1}",
        "type": "mixed",
        "listen": "::",
        "listen_port": 2080 + i,
          "users": [
          {
            "username": "proxyman",
            "password": "Proxyisawesome1"
          }
        ]
      }
    )
    outbounds.append(
          {
          "type": "socks",
          "tag": f"proxy-{i+1}",
          "server": ip,
          "server_port": 445,
          "username": "proxyman",
          "password": "Proxyisawesome1",
          "network": "tcp"
        }
    )
    routing.append(
      {
        "inbound": [
          f"in-{i+1}"
        ],
        "outbound": f"proxy-{i+1}"
      }
    )
with open("assets/ansible/broker.json","w") as file:
    configs = {
        "log":{
          "level": "error"
        },
        "inbounds": inbounds,
        "outbounds": outbounds,
        "route":       {
          "rules": routing
        }
    }
    json.dump(configs,file,indent=4,ensure_ascii=False)
# print(json.dumps(inbounds))
# print(json.dumps(outbounds))
# print(json.dumps(routing))
