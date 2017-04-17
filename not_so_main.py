import nltk
import numpy


def preprocessText(text):
    # To lower case
    text = text.lower();

    # Tokenize text
    tokenizedText = nltk.wordpunct_tokenize(text);
    tokenizedText = [w for w in tokenizedText if
                     not w in (',', '(', ')', '"', "'", ').', '),', '/', ';', ':')]

    return tokenizedText


def createPseudosentences(text):
    start = 0
    pseudosentences = []
    word = text[start]
    while start < len(text):
        sentence = []
        # print word
        word = text[start]
        while (word[len(word) - 1] != "."):
            # print word
            sentence.append(word)
            if (start < len(text) - 1):
                start += 1
            if (start == len(text) - 1):
                break
            word = text[start]
        start += 1
        pseudosentences.append(sentence)
    return pseudosentences


def cosMeasure(text, printOutput=False):
    start = 1
    scores = []
    cosMeasureRes = []

    while start < len(pseudosentences) - 1:

        block1 = list(pseudosentences[start]);
        block2 = list(pseudosentences[start + 1]);
        start += 1

        if printOutput: print
        block1
        if printOutput: print
        block2

        # Block similarity metric
        terms1 = list(block1);
        terms1 = list(set(terms1));

        terms2 = list(block2);
        terms2 = list(set(terms2));
        # print terms

        freq1 = []
        freq2 = []
        sum1 = []

        similarity = 0;
        w1 = 0;
        w2 = 0;
        count = 0;

        for word in terms1:
            for w in block1:
                if w == word:
                    count += 1
            freq1.append(count)
            count = 0

        for word in terms2:
            for w in block2:
                if w == word:
                    count += 1
            freq2.append(count)
            count = 0

        ii = 0

        while ii < len(terms1):
            jj = 0
            s = 0

            while jj < len(terms2):
                if terms2[jj] == terms1[ii]:
                    s = freq1[ii] * freq2[jj]
                jj += 1
            sum1.append(s)
            ii += 1

        SUM = 0
        for s in sum1:
            SUM += s

        F1 = 0
        for f11 in freq1:
            F1 += f11 * f11

        F2 = 0
        for f22 in freq2:
            F2 += f22 * f22

        F2 = numpy.sqrt(F2)
        F1 = numpy.sqrt(F1)

        cosMeasureRes.append(SUM / (F1 * F2))

    return cosMeasureRes


def toBorders(cosM, et):
    result = []
    for r in cosM:
        if (r >= et):
            result.append(0)
        if (r < et):
            result.append(1)
    return result


f = open("src.txt", "r")
src = f.read();
f.close()
res2 = []
for w in src:
    if (w != '\n'):
        res2.append(w)
print
res2

f = open("document.txt", "r")
text = f.read();
f.close()
tocenized = preprocessText(text);
pseudosentences = createPseudosentences(tocenized)
# print pseudosentences

result = cosMeasure(pseudosentences)
print
result

res1 = toBorders(result, 0.35)
print
res1

tp = 0
tn = 0
fn = 0
fp = 0
ii = 0
while ii < 132:
    f = res1[ii]
    s = int(res2[ii])
    # print (f, " ", s)
    if ((f == 1) & (s == 1)):
        tp += 1
    if ((f == 0) & (s == 0)):
        tn += 1
    if ((f == 1) & (s == 0)):
        fp += 1
    if ((f == 0) & (s == 1)):
        fn += 1
    ii += 1

precision = float(tp / float(tp + fp))
print("Precision: " + str(precision))
recall = float(tp / float(tp + fn))
print("Recall: " + str(recall))
f = float(2 * precision * recall / (precision + recall))

print("F-measure: " + str(f))
