# nltk.download()
first_value = open("lemma.txt", 'rU')
lemma_text = first_value.read()
first_value = open("abzatced_text.txt")
paragraphed_text = first_value.read()

# разбиение текста
paragraphed_text = paragraphed_text.lower().split("\n")
separated_text = []
for paragraph in paragraphed_text:
    separated_text.append(paragraph.split(" "))

# разбиение на слова лемматизированного текста
paragraphs = lemma_text.lower().split("\n")
separated_text = []
for paragraph in paragraphs:
    separated_text.append(paragraph.split(" "))

# формирование частотных вхождений слов
frequency_map = {}
maps = []
for i in range(0, len(separated_text)):
    for word in separated_text[i]:
        frequency_map[word] = paragraphed_text[i].count(word)
    maps.append(frequency_map)
    frequency_map = {}

# подсчет косинусных мер
cosine_list = [0]
for i in range(0, len(maps) - 1):
    cosine_mul = 0
    for entry_key in maps[i]:
        try:
            val1 = maps[i][entry_key]
            val2 = maps[i + 1][entry_key]  # value in second array
            cosine_mul += val1 * val2
        except:
            continue
    len1 = 0
    len2 = 0
    for entry_value in maps[i].values():
        len1 += entry_value * entry_value
    for entry_value in maps[i + 1].values():
        len2 += entry_value * entry_value
    cosine_list.append(cosine_mul / (pow(len1, 0.5) * pow(len2, 0.5)))

r = 0.1

# формирование нулей и единиц
bool_arr = []
for value in cosine_list:
    if value > r:
        bool_arr.append(0)
    else:
        bool_arr.append(1)

bool_arr_expert = []
for i in range(0, len(bool_arr)):
    bool_arr_expert.append(0)

# я сказала ХАРДКОДИМ! 10 21 25 54 57
# я сказала ХАРДКОДИМ! 10 21 25 54 57 58 90 95 104 105 106 109 112 126 130
positions = [1, 10, 21, 25, 54, 57, 58, 90, 95, 104, 105, 106, 109, 112, 126, 130]
for index in positions:
    bool_arr_expert[index - 1] = 1

# All outcomes
true_positive = 0
true_negative = 0
false_negative = 0
false_positive = 0
for i in range(0, len(bool_arr)):
    first_value = bool_arr[i]
    second_value = bool_arr_expert[i]
    if (first_value == 1) & (second_value == 1):
        true_positive += 1
    if (first_value == 0) & (second_value == 0):
        true_negative += 1
    if (first_value == 1) & (second_value == 0):
        false_positive += 1
    if (first_value == 0) & (second_value == 1):
        false_negative += 1

# Precision, Recall and F-measure
precision = float(true_positive / float(true_positive + false_positive))
print("Precision: " + str(precision))

recall = float(true_positive / float(true_positive + false_negative))
print("Recall: " + str(recall))

f_measure = float(2 * precision * recall / (precision + recall))
print("F-measure: " + str(f_measure))

# print(bool_arr.count(1) - 1)
