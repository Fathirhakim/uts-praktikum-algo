kalimat =input("masukan kalimat;")
vokal ="aiuoeAIUEO"
jumlah_vokal =sum(1 for huruf in kalimat if huruf in vokal)
print("jumlah huruf vokal",jumlah_vokal)