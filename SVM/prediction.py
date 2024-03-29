from libsvm.svmutil import (
    svm_train,
    svm_predict,
    svm_problem,
    svm_parameter
)

from dataset import load_data_set as lds

def data_format(data_arr):
    data_list = []
    for data in data_arr:
        data_dict = {}
        for idx, item in enumerate(data):
            data_dict[idx + 1] = item
        data_list.append(data_dict)
    return data_list

def predict(tr_data_arr, tr_label_arr, pred_data_arr, pred_label_arr):
    data_arr = data_format(tr_data_arr)
    prob = svm_problem(tr_label_arr, data_arr)
    param = svm_parameter('-c 2048.0 -g 0.001953125')
    svm_model = svm_train(prob, param)
    
    pred_data_arr = data_format(pred_data_arr)
    pred_data_len = len(pred_label_arr)
    wrong = 0
    for idx, data in enumerate(pred_data_arr):
        p_label, p_acc, p_val = svm_predict(
            [pred_label_arr[idx]], [data], svm_model)
        if int(p_label[0]) != int(pred_label_arr[idx]):
            wrong += 1
    
    accuracy = (pred_data_len - wrong) * 100.0 / pred_data_len
    return pred_data_len, wrong, accuracy

def get_data_file():
    data_arr, label_arr = lds.load('')
    
    with open('', 'w+') as fp:
        for d_idx, data in enumerate(data_arr):
            feature_list = []
            for f_idx, feature in enumerate(data):
                feature_list.append('%s:%s' % (f_idx + 1, feature))
            feature_str = ' '.join(feature_list)
            fp.write('%s %s\n' % (label_arr[d_idx], feature_str))