import numpy as np
import xlsxwriter

def measure(matrix):
    # matrix = [[171432, 39, 1186, 540, 2, 13660, 1260, 192, 521],
    #  [1048, 1526, 16, 15, 0, 794, 58, 16, 2],
    #  [9914, 78, 14771, 244, 0, 5054, 594, 55, 108],
    #  [1158, 5, 95, 6579, 0, 4985, 396, 108, 5],
    #  [1, 0, 0, 1, 103, 3, 2, 0, 0],
    #  [10354, 30, 876, 1157, 6, 87877, 1010, 267, 22],
    #  [2740, 15, 360, 566, 5, 3754, 27296, 47, 28],
    #  [1015, 3, 27, 82, 0, 1032, 38, 2787, 6],
    #  [382, 14, 24, 10, 0, 37, 19, 2, 3970]]

    matrix = np.array(matrix)

    precision_mic = [0]*9
    recall_mic = [0]*9
    accur_mic = [0]*9
    ave_accur  =0
    class_f1= [0]*9
    class_tp = [0]*9
    class_tn = [0]*9
    class_fp = [0]*9
    class_fn = [0]*9
    error_rate  = [0]*9
    mac_p_sum = [0]*9

    i = 0
    #i is true class
    while i <9:
        total = matrix.sum()
        class_tp[i] = matrix[i][i]
        for idx in range(0,9):
            if idx!=i:
                class_fp[i] += matrix[idx][i]
                #false negative
                class_fn[i] += matrix[i][idx]
        class_tn[i] = total - class_fn[i]- class_fp[i]-class_tp[i]
        accur_mic[i] = (class_tn[i]+class_tp[i])/total
        error_rate[i] = 1 - accur_mic[i]
        precision_mic[i] =  class_tp[i]/(class_fp[i]+class_tp[i])
        recall_mic[i] = class_tp[i]/(class_tp[i]+class_fn[i])
        class_f1[i] = 2*(precision_mic[i]*recall_mic[i])/(recall_mic[i]+precision_mic[i])
        i+=1
    class_tp = np.array(class_tp)
    class_tn = np.array(class_tp)
    class_fp = np.array(class_fp)
    class_fn = np.array(class_fn)
    error_rate = np.array(error_rate)
    mac_p_sum = np.array(mac_p_sum)

    accur_mic = np.array(accur_mic)
    precision_mic = np.array(precision_mic)
    recall_mic = np.array(recall_mic)



    ave_accur= accur_mic.sum()/9

    mac_ave_precision = precision_mic.sum()/9
    mac_ave_recall = recall_mic.sum()/9
    mac_ave_f1 = mac_ave_recall*mac_ave_precision*2/(mac_ave_recall+mac_ave_precision)
    mac_error = error_rate.sum()/9

    mic_ave_precision = class_tp.sum()/(class_fp.sum()+class_tp.sum())
    mic_ave_recall = class_tp.sum()/(class_tp.sum()+class_fn.sum())
    mic_ave_f1 = (mic_ave_precision*mic_ave_recall*2)/(mic_ave_precision+mic_ave_recall)



    labels = ['SVM', 'CryptoCurrency', 'coronavirus', 'cyberpunk', 'jokes', 'recipes', 'Showerthoughts',
              'suicideanddepression', 'texas', 'wallstreetbets', 'TOTAL (Macro)', 'TOTAL (Micro) ']
    results = []

    workbook = xlsxwriter.Workbook('TFIDF_first.xlsx')
    worksheet = workbook.add_worksheet('SVM result')

    labels = ['SVM', 'CryptoCurrency', 'coronavirus', 'cyberpunk', 'jokes', 'recipes', 'Showerthoughts',
              'suicideanddepression', 'texas', 'wallstreetbets', 'TOTAL (Macro)', 'TOTAL (Micro) ']


    rows = ['SVM','Accuracy','Error rate', 'Precision','Recall','F1-score']

    labels = tuple(labels)
    rows = tuple(rows)
    accur =  tuple(np.round(accur_mic,3))
    err =  tuple(np.round(error_rate, 3))
    pre =  tuple(np.round(precision_mic, 3))
    rec =  tuple(np.round(recall_mic, 3))
    f1 =  tuple(np.round(class_f1, 3))

    worksheet.write_row('A1',rows)
    worksheet.write_column('A1',labels)
    worksheet.write_column('B2', accur) # accuracy
    worksheet.write('B11', ave_accur)

    worksheet.write_column('C2', err )  # error
    worksheet.write('C11', mac_error)

    worksheet.write_column('D2',pre  )  # precision
    worksheet.write('D11', mac_ave_precision)
    worksheet.write('D12', mic_ave_precision)

    worksheet.write_column('E2',rec )  # recall
    worksheet.write('E11', mac_ave_recall)
    worksheet.write('E12', mic_ave_recall)

    worksheet.write_column('F2',f1 )  # f1
    worksheet.write('F11',mac_ave_f1)
    worksheet.write('F12', mic_ave_f1)

    workbook.close()

    print(np.round(class_f1,3), end=" f1_catagory")

    print("%.2f" %mac_ave_f1,end=" macro average\n")
    print("%.2f" %mic_ave_f1, end=" micro average\n")

    print(np.round(recall_mic,3),end=" recall_catagory\n")
    print("%.2f" %mic_ave_recall,end=" mirco average recall\n")
    print("%.2f" %mac_ave_recall, end=" macro average recall\n")

    # print(np.round(precision_mic,3),end="precision catagory\n")

    print("%.2f" %mac_ave_precision,end=" mac ave precision\n")
    print("%.2f" %mic_ave_precision, end = " mic ave precision\n")


    print("%.2f" %ave_accur, end=" average accuarcy\n")
    print(np.round(accur_mic,3),end=" ave catagory\n")

    print("%.2f" %mac_error,end=" macro error\n")
    print(np.round(error_rate,3),end = " error class\n")
