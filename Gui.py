import tkinter as tk
from tkinter import INSERT
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
root=tk.Tk()
root.geometry("800x500")
root.configure(bg="#accdf5")
root.title("PYTHON MINI PROJECT")
LARGEFONT = ("Courier", 35)
label = tk.Label(text="STOCK MARKET PREDICTOR",font=LARGEFONT, bg='#accdf5')
label.place(x=100, y=10)
sma_var=tk.DoubleVar()
wma_var = tk.DoubleVar()
momentum_var =tk. DoubleVar()
Stochastic_K_var = tk.DoubleVar()
Stochastic_D_var = tk.DoubleVar()
Relative_strength_index_var = tk.DoubleVar()
Signal_var = tk.DoubleVar()
Larry_William_R_var = tk.DoubleVar()
ADO_var = tk.DoubleVar()
CCI_var = tk.DoubleVar()
def prediction(T1):
    li=[None]*10
    li[0] = float(sma_var.get())
    li[1] = float(wma_var.get())
    li[2] = float(momentum_var.get())
    li[3] = float(Stochastic_K_var.get())
    li[4] = float(Stochastic_D_var.get())
    li[5] = float(Relative_strength_index_var.get())
    li[6] = float(Signal_var.get())
    li[7] = float(Larry_William_R_var.get())
    li[8] = float(ADO_var.get())
    li[9]=float(CCI_var.get())
    predict=np.array([li])
    
    loaded_model = pickle.load(open("D:/python/PYTHON ASSIGNMENTS/PYTHON MINI PROJECT/finalized_model", 'rb'))
    predicted_logisticRegression = loaded_model.predict(predict)
    T1.delete("1.0", "end")
    
    T1.insert(INSERT, predicted_logisticRegression[0])

Simple_moving_average = tk.Label(root, bg="#accdf5", text='Simple moving average', font=('calibre', 10, 'bold'))
Simple_moving_average.place(x=215, y=97)
Weighted_moving_average = tk.Label(root, bg="#accdf5", text='Weighted_moving_average', font=(
    'calibre', 10, 'bold')).place(x=215, y=117)
momentum = tk.Label(root, bg="#accdf5", text='momentum',
                    font=('calibre', 10, 'bold')).place(x=215, y=137)
Stochastic_D = tk.Label(root, bg="#accdf5", text='Stochastic_D', font=(
    'calibre', 10, 'bold')).place(x=215, y=157)
Stochastic_K = tk.Label(root, bg="#accdf5", text='Stochastic_K', font=(
    'calibre', 10, 'bold')).place(x=215, y=177)
RSI = tk.Label(root, bg="#accdf5", text='RSI', font=(
    'calibre', 10, 'bold') ).place(x=215, y=197)
Signal = tk.Label(root, bg="#accdf5", text='Signal',
                  font=('calibre', 10, 'bold')).place(x=215, y=217)
Larry_William_R = tk.Label(root, bg="#accdf5", text='Larry_William_R', font=(
    'calibre', 10, 'bold')).place(x=215, y=237)
ADO = tk.Label(root, bg="#accdf5", text='ADO', font=(
    'calibre', 10, 'bold')).place(x=215, y=257)
CCI = tk.Label(root, bg="#accdf5", text='CCI_var',
               font=('calibre', 10, 'bold')).place(x=215, y=277)


entryNum1 = tk.Entry(root, textvariable=sma_var).place(x=400, y=100)
entryNum2 = tk.Entry(root, textvariable=wma_var).place(x=400, y=120)
entryNum3 = tk.Entry(root, textvariable=momentum_var).place(x=400, y=140)
entryNum4 = tk.Entry(root, textvariable=Stochastic_K_var).place(x=400, y=160)
entryNum5 = tk.Entry(root, textvariable=Stochastic_D_var).place(x=400, y=180)
entryNum6 = tk.Entry(root, textvariable=Relative_strength_index_var).place(x=400, y=200)
entryNum7 = tk.Entry(root, textvariable=Signal_var).place(x=400, y=220)
entryNum8 = tk.Entry(root, textvariable=Larry_William_R_var).place(x=400, y=240)
entryNum9 = tk.Entry(root, textvariable=ADO_var).place(x=400, y=260)
entryNum10= tk.Entry(root, textvariable=CCI_var).place(x=400, y=280)


T1 = tk.Text(height=1, width=7, bg='white', relief="raised")
T1.place(x=425,y=320,height=28)
sub_btn = tk.Button(root, text="Predict", relief="raised", height=1, width=7,
                    command=lambda: prediction(T1), bg="#4e74fc").place(x=250, y=320)
root.mainloop()
