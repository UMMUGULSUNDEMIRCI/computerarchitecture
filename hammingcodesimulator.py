import tkinter as tk
from tkinter import messagebox

def calculate_hamming_code(data):
    m = 1
    while len(data) + m + 1 > 2**m:
        m += 1

    hamming_code = []
    j = 0
    k = 0
    for i in range(1, len(data) + m + 1):
        if i == 2**k:
            hamming_code.append(0)
            k += 1
        else:
            hamming_code.append(data[j])
            j += 1

    for i in range(m):
        parity_position = 2**i - 1
        parity = 0
        for j in range(parity_position, len(hamming_code), 2**(i + 1)):
            for k in range(2**i):
                if j + k < len(hamming_code):
                    parity ^= hamming_code[j + k]
        hamming_code[parity_position] = parity

    return hamming_code

def verify_hamming_code(received_hamming_code):
    error_position = 0
    for i in range(len(received_hamming_code)):
        if received_hamming_code[i] == 1:
            error_position ^= i + 1
    return error_position

def calculate_hamming():
    data_str = data_entry.get()
    data = [int(bit) for bit in data_str.split()]
    hamming_code = calculate_hamming_code(data)
    hamming_code_str = ' '.join(map(str, hamming_code))
    hamming_code_label.config(text=f"Hamming Kodu: {hamming_code_str}")

def verify_hamming():
    faulty_hamming_str = faulty_hamming_entry.get()
    faulty_hamming_code = [int(bit) for bit in faulty_hamming_str.split()]
    error_position = verify_hamming_code(faulty_hamming_code)
    
    if error_position != 0:
        faulty_hamming_code[error_position - 1] = 1 if faulty_hamming_code[error_position - 1] == 0 else 0
        messagebox.showinfo("Sonuç", f"Hata konumu: {error_position}. Hata düzeltildi.")
    else:
        messagebox.showinfo("Sonuç", "Hata yok.")
    
    corrected_hamming_code_str = ' '.join(map(str, faulty_hamming_code))
    corrected_hamming_code_label.config(text=f"Düzeltilmiş Hamming Kodu: {corrected_hamming_code_str}")

# Tkinter arayüzü oluştur
root = tk.Tk()
root.title("Hamming Kodu Simülasyonu")

# Veri girişi
tk.Label(root,bg='lightblue',text="Veri (0'lar ve 1'ler, bitler arasında boşluk bırak!):").grid(row=0, column=0)
data_entry = tk.Entry(root, width=50)
data_entry.grid(row=0, column=1)

# Hamming kodunu hesapla butonu
calculate_button = tk.Button(root,bg='lightpink', text="Hamming Kodunu Hesapla", command=calculate_hamming)
calculate_button.grid(row=1, column=0, columnspan=2)

# Hamming kodu etiketi
hamming_code_label = tk.Label(root, text="Hamming Kodu:")
hamming_code_label.grid(row=2, column=0, columnspan=2)

# Hatalı Hamming kodu girişi
tk.Label(root,bg='lightblue', text="Hatalı Hamming Kodu (0'lar ve 1'ler, bitler arasında boşluk bırak!):").grid(row=3, column=0)
faulty_hamming_entry = tk.Entry(root, width=50)
faulty_hamming_entry.grid(row=3, column=1)

# Hamming kodunu doğrula butonu
verify_button = tk.Button(root,bg='lightgreen', text="Hamming Kodunu Kontrol Et", command=verify_hamming)
verify_button.grid(row=4, column=0, columnspan=2)

# Düzeltilmiş Hamming kodu etiketi
corrected_hamming_code_label = tk.Label(root, text="Düzeltilmiş Hamming Kodu:")
corrected_hamming_code_label.grid(row=5, column=0, columnspan=2)

# Tkinter ana döngüsünü başlat
root.mainloop()
