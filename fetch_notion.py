"""
Script untuk mengambil tulisan dari Notion dan menyimpannya sebagai posts.json
Cara pakai: python3 fetch_notion.py
"""

import json
import urllib.request
import os
import sys

# ====== ISI BAGIAN INI ======
NOTION_TOKEN = "TEMPEL_TOKEN_NOTION_DI_SINI"
DATABASE_ID = "TEMPEL_DATABASE_ID_DI_SINI"
# =============================

NOTION_VERSION = "2022-06-28"
API_URL = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"


def get_text(prop):
    """Ambil teks polos dari property Notion (title atau rich_text)."""
    if not prop:
        return ""
    items = prop.get("title") or prop.get("rich_text") or []
    return "".join([t.get("plain_text", "") for t in items])


def get_select(prop):
    if not prop or not prop.get("select"):
        return ""
    return prop["select"].get("name", "")


def get_date(prop):
    if not prop or not prop.get("date"):
        return ""
    return prop["date"].get("start", "")


def get_checkbox(prop):
    if not prop:
        return False
    return prop.get("checkbox", False)


def fetch_posts():
    if "TEMPEL" in NOTION_TOKEN or "TEMPEL" in DATABASE_ID:
        print("ERROR: kamu belum mengisi NOTION_TOKEN dan DATABASE_ID di file ini.")
        print("Buka fetch_notion.py, ganti bagian 'TEMPEL_...' dengan token dan ID asli kamu.")
        sys.exit(1)

    req = urllib.request.Request(
        API_URL,
        method="POST",
        headers={
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "sorts": [{"property": "Tanggal", "direction": "descending"}]
        }).encode("utf-8"),
    )

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"Gagal mengambil data dari Notion (HTTP {e.code}):")
        print(body)
        print("\nCek lagi: apakah token benar? Apakah database sudah di-connect ke integration-nya?")
        sys.exit(1)

    posts = []
    for page in data.get("results", []):
        props = page.get("properties", {})
        published = get_checkbox(props.get("Published"))
        if not published:
            continue  # lewati tulisan yang belum di-publish

        posts.append({
            "title": get_text(props.get("Title")),
            "date": get_date(props.get("Tanggal")),
            "category": get_select(props.get("Kategori")),
            "excerpt": get_text(props.get("Excerpt")),
        })

    return posts


if __name__ == "__main__":
    posts = fetch_posts()
    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"Berhasil! {len(posts)} tulisan tersimpan ke posts.json")
    print("Sekarang upload file posts.json ke GitHub untuk update website kamu.")
