def formulate_prompt(query, docs):
    assert len(docs) != 0, "There's no any context documents."
    num_docs = len(docs)
    
    prompt = f"""
        あなたは優秀な質問応答システムです。
        これから「質問」と「文脈（コンテキスト）」を与えますので、
        文脈に基づいて適切な答えを返してください。
        関連する文脈と関連しない文脈があります。関連する文脈から答えを見つけて、その他は無視してください。
        もし文脈内に答えが見つからない場合は、「答えがわかりません」と返答してください。
        
        質問：{query}
    """

    for id in range(num_docs):
        prompt += f"""\n こちらは関連する文脈 {id} です：{docs[id].replace("passage: ", "")}"""
        
    return prompt