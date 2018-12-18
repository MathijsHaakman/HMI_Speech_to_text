import os

count = 0
t_sure = 0
t_milis = 0

with open(os.path.join("Results", "results.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    while line:
        count += 1
        data = line.split(";")
        sure = float(data[2])
        milis = int(data[4])

        t_sure += sure
        t_milis += milis
        line = list.readline()

print("average certainty", t_sure / count)
print("average response time", t_milis / count)

t_wrr = t_wer = t_micro_precision = t_macro_precision = t_micro_recall = t_macro_recall = t_micro_f_score = t_macro_f_score = 0
count2 = 0
with open(os.path.join("Results", "wrr_wer.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    print("number;wrr,wer;micro precision;macro precision;micro recall;macro recall;micro f-score;macro f-score")
    while line:
        count2 += 1
        data = line.split(";")
        wrr = float(data[1])
        wer = float(data[2])
        micro_precision = float(data[3])
        macro_precision = float(data[4])
        micro_recall = float(data[5])
        macro_recall = float(data[6])
        micro_f_score = float(data[7])
        macro_f_score = float(data[8])

        t_wrr += wrr
        t_wer += wer
        t_micro_precision += micro_precision
        t_macro_precision += macro_precision
        t_micro_recall += micro_recall
        t_macro_recall += macro_recall
        t_micro_f_score += micro_f_score
        t_macro_f_score += macro_f_score

        line = list.readline()

print("average wrr", t_wrr / count)
print("average wer", t_wer / count)
print("average micro_precision", t_micro_precision / count)
print("average macro_precision", t_macro_precision / count)
print("average micro_recall", t_micro_recall / count)
print("average macro_recall", t_macro_recall / count)
print("average micro_f_score", t_micro_f_score / count)
print("average macro_f_score", t_macro_f_score / count)