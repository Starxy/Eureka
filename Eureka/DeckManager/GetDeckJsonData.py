import requests


def get_deck_json(set_id):
    """
    调用 Artifact 官方提供的接口来获取卡组信息
    https://github.com/ValveSoftware/ArtifactDeckCode+
    :param set_id:  卡组编号
    :return:
    """
    url = "https://playartifact.com/cardset/" + set_id
    set_info = requests.get(url).json()
    deck_url = set_info["cdn_root"] + set_info["url"]
    return requests.get(deck_url).json()
