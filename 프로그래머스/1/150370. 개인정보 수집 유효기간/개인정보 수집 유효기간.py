def solution(today, terms, privacies):
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y * 12 * 28 + m * 28 + d

    term_dict = {}
    for t in terms:
        name, months = t.split()
        term_dict[name] = int(months)

    today_days = to_days(today)
    answer = []

    for i, info in enumerate(privacies, start=1):
        date, term_type = info.split()
        expire = to_days(date) + term_dict[term_type] * 28
        if expire <= today_days:
            answer.append(i)

    return answer