import requests


def get_id(gmail):
    api = f"https://fe80kk63kd.execute-api.ap-southeast-1.amazonaws.com/get_id/{gmail}"
    request = requests.get(url=api)
    data = request.json()["member"]

    if data == "None":
        return "Club ID not found. The provided email address is not registered in the database. Please try again.\nContact aki_9716 if problem persists."

    return data



if __name__ == "__main__":
    print(get_id("markachilesflores2004@gmail.com"))
