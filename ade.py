import requests

url = "https://discord.com/api/v9/channels/1173572558751272972/messages"  # Fix typo in the URL

payload = {
    "content": "Subscribe"
}

headers = {
    "Authorization": "MTE2MTk4OTY2NDIzNjkwNDQ1OA.GutHGg.2JhUuv6q0GDCDENMrA6RiWdIsCP4zor5yq_d3U"
}

res = requests.post(url, data=payload, headers=headers)  # Use 'data' instead of 'payload' for form data
