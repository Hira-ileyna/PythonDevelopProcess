students = {
    101: {"Name":  "Yiğit ",
          "Surname" : "Bilgi",
          "Birthday": 2010,
          "Notes": (40,80,90)
          },
    102: {"Name":  "Ada ",
              "Surname" : "Bilgi",
              "Birthday": 2012,
              "Notes": (80,80,80)
              },
    103: {"Name":  "Çınar ",
            "Surname" : "Turan",
            "Birthday": 2017,
            "Notes": (70,70,70)
            }
}

studentNo = int(input('Student No: '))
student = students[studentNo]
average = (student["Notes"][0] + student["Notes"][1] + student["Notes"][2]) / 3
print(f"{studentNo} numaralı {student["Name"]} {student["Surname"]} ismindeki öğrencinin yaşı {2026 - student["Birthday"]} ve not ortalaması {average} ")