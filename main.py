from webserver import keep_alive
import requests

channelID = 945702804129992714
headers = {
    "authorization":
    "OTEzODAyNjMyMzkxNDM0Mjkw.YkcU7g.T3fggN70xgGoCzl854DPiFCbDfo"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
