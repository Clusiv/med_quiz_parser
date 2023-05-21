from pprint import pprint
from dbfile import db


# output format:
# [Номер вопроса]. [Текст вопроса].

# A. [Вариант ответа A]
# B. [Вариант ответа B]
# C. [Вариант ответа C]
# D. [Вариант ответа D]

# ОТВЕТ: [укажи только букву правильного ответа большой буквы, правильный ответ указан "1"]

# a = """ДРЕНАЖНОЕ ПОЛОЖЕНИЕ ПРИДАЕТСЯ ПАЦИЕНТУ ДЛЯ
# 0 уменьшения одышки
# 0 расширения бронхов
# 0 снижения лихорадки
# 1 улучшения отхождения мокроты
# %СИМПТОМАМИ НАЧАЛЬНОГО ПЕРИОДА РАХИТА ЯВЛЯЮТСЯ
# 1 беспокойство, потливость, пугливость, вздрагивание во сне
# 0 покраснение кожных покровов
# 0 беспокойство, потливость, повышение температуры
# 0 беспокойство, повышение температуры
# """


splited = db.split('@')

def template(index, topic, answers, right_answer):
    s = f"""{index}. {topic}.

A. {answers[0].capitalize() if answers[0][0].isalpha() == True else answers[0]}.
B. {answers[1].capitalize() if answers[1][0].isalpha() == True else answers[1]}.
C. {answers[2].capitalize() if answers[2][0].isalpha() == True else answers[2]}.
D. {answers[3].capitalize() if answers[3][0].isalpha() == True else answers[3]}.

ОТВЕТ: {right_answer}
"""
    return s

output_file = open('output.txt', 'w')

for i, t in enumerate(splited):
    right_answer = ''
    topic = t.split('\n')
    q = topic[0]
    dirty_answers = []
    if topic[-1] == '':
        dirty_answers = topic[1:-1]
    else:
        dirty_answers = topic[1:]
    # print(q, len(dirty_answers) != 4)
    if len(dirty_answers) != 4:
        pprint(topic)
    # print(t)
    clear_answers = []
    for w, j in zip(['A', 'B', 'C', 'D'], dirty_answers):
        if j[0] == '1':
            right_answer = w
        clear_answers.append(j[2:])
        # print(right_answer)
    s = template(i + 1, q, clear_answers, right_answer)
    output_file.write(s)
    # print(s)
