def find_spans2(query_tokens, passage_tokens):
    """
    Find spans of query in passage_tokens
    Arguments:
        query_tokens {[type]} -- [description]
        passage_tokens {[type]} -- [description]
    """
    s = 0
    passage_idxs = []
    for token in passage_tokens:
        start = s
        end = s + len(token) - 1
        passage_idxs.append([start, end])
        s = end + 1
    passage_str = ''.join(passage_tokens).lower()
    query_str = ''.join(query_tokens).lower()
    query_start = passage_str.find(query_str)
    if query_start == -1:
        return None
    query_end = query_start + len(query_str) - 1
    ans_start, ans_end = -1, -1
    for pid, p_spans in enumerate(passage_idxs):
        if p_spans[0] <= query_start and p_spans[1] >= query_start:
            ans_start = pid
        if p_spans[0] <= query_end and p_spans[1] >= query_end:
            ans_end = pid
    if ans_start != -1 and ans_end != -1:
        return [[ans_start, ans_end]]
    else:
        return None