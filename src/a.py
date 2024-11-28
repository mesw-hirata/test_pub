import re
import unicodedata

def normalize_text(text):
    # 全角文字を半角文字に変換し、大文字を小文字に変換
    return unicodedata.normalize('NFKC', text).lower()

def add_tags_around_match(original_text, search):
    # 正規化されたテキストを作成
    normalized_text = normalize_text(original_text)
    normalized_search = normalize_text(search)
    
    # 正規表現パターンを作成
    pattern = re.compile(re.escape(normalized_search), re.IGNORECASE)
    
    # 一致する部分の前後にタグを追加
    def replacement(match):
        start, end = match.span()
        return f"<a>{original_text[start:end]}</a>"
    
    return pattern.sub(replacement, normalized_text)

def main():
    text = "This is a bBb and ＢＢＢ test."
    search = "bbb"
    
    # 元のテキストにタグを追加
    result = add_tags_around_match(text, search)
    
    print(result)

if __name__ == "__main__":
    main()
    print('test')
