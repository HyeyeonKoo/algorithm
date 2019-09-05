def solution(numbers, target):

    answer = 0
    p, m = [numbers[0]], [numbers[0]*(-1)]

    for n in numbers[1:]:
        n_minus = n*-1
        p_temp = list()
        m_temp = list()
        for i in range(len(p)):
            p_temp.append(p[i] + n)
            p_temp.append(p[i] + n_minus)
            m_temp.append(m[i] + n)
            m_temp.append(m[i] + n_minus)
        p = p_temp
        m = m_temp

    answer = (p+m).count(target)

    return answer