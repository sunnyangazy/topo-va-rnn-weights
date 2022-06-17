import numpy as np

class SourceDataDemo:

    @property
    def seg_0_lstm_1_w_i(self):
        my_data = np.genfromtxt("./static/data/seg0-lstm_1-weights/epoch_0_lstm_1_w_i.csv", delimiter=',')
        print(my_data.shape)
        my_data2 = my_data.tolist()

        d0 = my_data2[0]
        d1 = my_data2[1]
        d2 = my_data2[2]
        d3 = my_data2[3]
        d4 = my_data2[4]

        return d0,d1,d2,d3,d4
    
    @property
    def seg_1_lstm_1_w_i(self):
        my_data = np.genfromtxt("./static/data/seg0-lstm_1-weights/epoch_80_lstm_1_w_i.csv", delimiter=',')
        print(my_data.shape)
        my_data2 = my_data.tolist()

        d0 = my_data2[0]
        d1 = my_data2[1]
        d2 = my_data2[2]
        d3 = my_data2[3]
        d4 = my_data2[4]

        return d0,d1,d2,d3,d4

    @property
    def seg_2_lstm_1_w_i(self):
        my_data = np.genfromtxt("./static/data/seg0-lstm_1-weights/epoch_20_lstm_1_w_f.csv", delimiter=',')
        print(my_data.shape)
        my_data2 = my_data.tolist()

        d0 = my_data2[0]
        d1 = my_data2[1]
        d2 = my_data2[2]
        d3 = my_data2[3]
        d4 = my_data2[4]

        return d0,d1,d2,d3,d4

    @property
    def seg_3_lstm_1_w_i(self):
        my_data = np.genfromtxt("./static/data/seg0-lstm_1-weights/epoch_40_lstm_1_w_f.csv", delimiter=',')
        print(my_data.shape)
        my_data2 = my_data.tolist()

        d0 = my_data2[0]
        d1 = my_data2[1]
        d2 = my_data2[2]
        d3 = my_data2[3]
        d4 = my_data2[4]

        return d0,d1,d2,d3,d4
    

    @property
    def seg_4_lstm_1_w_i(self):
        my_data = np.genfromtxt("./static/data/seg0-lstm_1-weights/epoch_60_lstm_1_w_c.csv", delimiter=',')
        print(my_data.shape)
        my_data2 = my_data.tolist()

        d0 = my_data2[0]
        d1 = my_data2[1]
        d2 = my_data2[2]
        d3 = my_data2[3]
        d4 = my_data2[4]

        return d0,d1,d2,d3,d4

class SourceData(SourceDataDemo):
    ...
