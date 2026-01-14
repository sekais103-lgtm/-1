import streamlit as st

# ページ設定
st.set_page_config(page_title="スプラ3 ブランド検索", layout="centered")

# タイトルと説明
st.title("🦑 スプラ3 ギアパワー検索")
st.write("欲しいギアパワーを選ぶと、それが付きやすいブランドを表示します。")

# --- データ定義 ---
# キー：ギアパワー名、値：付きやすいブランドのリスト
# ※スプラトゥーン3の最新データに基づいています
gear_data = {
    "インク効率アップ（メイン）": ["アロメ", "ジモン"],
    "インク効率アップ（サブ）": ["ホッコリー"],
    "インク回復力アップ": ["シグレニ"],
    "ヒト移動速度アップ": ["ロッケンベルグ"],
    "イカダッシュ速度アップ": ["クラーゲス"],
    "スペシャル増加量アップ": ["ヤコ"],
    "スペシャル減少量ダウン": ["エゾッコ"],
    "スペシャル性能アップ": ["フォーリマ"],
    "復活時間短縮": ["ホタックス"],
    "スーパージャンプ時間短縮": ["アイロニック"],
    "サブ性能アップ": ["エンペリー"],
    "相手インク影響軽減": ["バ"],
    "サブ影響軽減": ["シチリン"],
    "アクション強化": ["アナアキ", "バラズシ"],
    # ※特定のブランドがない、または付きやすい傾向がないギアは除外、または別途処理
}

# 選択肢のリスト作成
gear_list = list(gear_data.keys())

# --- UI部分 ---

# セレクトボックス（ドロップダウン）でギアを選択
selected_gear = st.selectbox(
    "探しているギアパワーを選択してください：",
    gear_list
)

# 検索ボタン（なくても動きますが、あるとアプリっぽい挙動になります）
if st.button("ブランドを検索"):
    st.markdown("---")
    
    # 結果の取得
    brands = gear_data.get(selected_gear)
    
    if brands:
        st.subheader(f"「{selected_gear}」が付きやすいブランド")
        
        # 複数のブランドがある場合も見やすく表示
        cols = st.columns(len(brands))
        for i, brand in enumerate(brands):
            with cols[i]:
                st.success(f"🏷️ {brand}")
                
        st.info("💡 ヒント: ロビーでドリンクチケットを使うと、ブランドに関係なく付きやすくなりますよ！")
    else:
        st.error("データが見つかりませんでした。")

# フッター
st.markdown("---")
st.caption("Splatoon 3 Gear Brand Search Tool")