from notion_client import Client
import configparser
import json

## reference = "https://qiita.com/Yusuke_Pipipi/items/b44cb8442932019c52c9#%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9id" (2024/4/17)


def get_notion_api_key():#config.iniからapi_keyを取得する
    config = configparser.ConfigParser()
    config.read('./config.ini')
    api_key = config['DEFAULT']['API_KEY']
    client=Client(auth=api_key)
    return client

##各関数の先頭に    client = get_notion_api_key()をつける


def read_notion_database(database_id):# データベースの全ての情報を取得する
    client = get_notion_api_key()
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )

    print(response)
    return response


def get_page_title(page_id):#title取得
    client = get_notion_api_key()
    response = client.pages.retrieve(
        **{
            "page_id": page_id,
            "properties": [
                "Title"
            ]
        }
    )

    return response["properties"]["Title"]["title"][0]["plain_text"]


def get_page_content(page_id):#ページの内容取得
    client = get_notion_api_key()
    data = client.blocks.children.list(
        **{
            "block_id": page_id,
            "page_size": 50
        }
    )
    data_str = json.dumps(data)
    response=extract_content(data_str)
    return response


#created by chatGPT
def get_database_pages_and_public(database_id):
    """データベースIDからすべてのページIDとプロパティ「public」を取得する"""
    client = get_notion_api_key()
    query = client.databases.query(database_id=database_id)
    results = []
    for page in query['results']:
        page_id = page['id']
        public = page['properties'].get('public', {}).get('checkbox', False)
        results.append({'page_id': page_id, 'public': public})
    return results


#created by chatGPT
def get_page_properties_title_category_creation_date(page_id):
    """ページIDからプロパティ「Title」、「Category」、「Creation date」を取得する"""
    client = get_notion_api_key()
    page = client.pages.retrieve(page_id=page_id)
    title = page['properties'].get('Title', {}).get('title', [])[0].get('plain_text', '')
    category = [option['name'] for option in page['properties'].get('Category', {}).get('multi_select', [])]
    creation_date = page['properties'].get('Creation date', {}).get('date', {}).get('start', '')
    return {'title': title, 'category': category, 'creation_date': creation_date}


#created by chatGPT
def get_page_property_last_updated(page_id):
    """ページIDからプロパティ「Last updated」を取得する"""
    client = get_notion_api_key()
    page = client.pages.retrieve(page_id=page_id)
    last_updated = page['properties'].get('Last updated', {}).get('last_edited_time', '')
    return {'last_updated': last_updated}









#created by chatGPT
def extract_content(data):#ページの内容から必要な情報のみ抽出する
    """
    Notionのページデータからテキストベースおよび非テキストベースのブロックの内容を抽出し、
    各コンテンツを['block_type', 'content']の形式の配列にして返す。

    Args:
        data (str): Notion APIから取得したJSON形式の文字列。

    Returns:
        list: ['block_type', 'content']形式の配列のリスト。
    """
    # JSON文字列をPythonの辞書に変換
    data_dict = json.loads(data)

    # コンテンツを格納するためのリスト
    contents = []

    # results配列をループして、ブロックの内容を抽出
    for block in data_dict["results"]:
        block_type = block["type"]
        if block_type in ["paragraph", "heading_1", "heading_2", "heading_3", "bulleted_list_item"]:
            # テキストブロックからテキストを取得
            for text_element in block[block_type]["rich_text"]:
                text_content = text_element["plain_text"]
                contents.append([block_type, text_content])
                # リンクがあればURLも抽出し、別の要素として追加
                if text_element["text"].get("link"):
                    link_url = text_element["text"]["link"]["url"]
                    contents.append([f"{block_type} Link", link_url])
        elif block_type == "image":
            # 画像ブロックからURLを取得
            image_url = block["image"]["file"]["url"]
            contents.append([block_type, image_url])
        elif block_type == "bookmark":
            # ブックマークブロックからURLを取得
            if "bookmark" in block:
                bookmark_url = block["bookmark"]["url"]
                contents.append([block_type, bookmark_url])

    return contents
