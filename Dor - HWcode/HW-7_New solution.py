# ---Create a Python script that take a list of dictionaries and create an excel file that
# includind the id,Date and sS_Id columns by the dictionaries keys(use the .item() to extract the valalus
# from the dictionaries)

# -----------------------------------#
# Solutions
# -----------------------------------#

import pandas as pd

Data = [{'id': '934', 'Date': '2022-04-13 ', 'S_Id': '5219', 'Lead_num': '62'},
        {'id': '935', 'Date': '2022-04-04 ', 'S_Id': '25256', 'Lead_num': '93'},
        {'id': '936', 'Date': '2022-04-13 ', 'S_Id': '25338', 'Lead_num': '11'},
        {'id': '937', 'Date': '2022-04-12 ', 'S_Id': '25565', 'Lead_num': '47'},
        {'id': '938', 'Date': '2022-04-09 ', 'S_Id': '25775', 'Lead_num': '108'},
        {'id': '940', 'Date': '2022-04-11 ', 'S_Id': '25844', 'Lead_num': '59'},
        {'id': '941', 'Date': '2022-04-14 ', 'S_Id': '2608', 'Lead_num': '04'},
        {'id': '942', 'Date': '2022-04-13 ', 'S_Id': '26162', 'Lead_num': '87'},
        {'id': '943', 'Date': '2022-04-13 ', 'S_Id': '26278', 'Lead_num': '74'},
        {'id': '944', 'Date': '2022-04-11 ', 'S_Id': '26696', 'Lead_num': '35'},
        {'id': '945', 'Date': '2022-04-10 ', 'S_Id': '27366', 'Lead_num': '25'},
        {'id': '946', 'Date': '2022-04-13', 'S_Id': '27467', 'Lead_num': '42'},
        {'id': '947', 'Date': '2022-04-10', 'S_Id': '27745', 'Lead_num': '77'},
        {'id': '948', 'Date': '2022-04-13 ', 'S_Id': '27942', 'Lead_num': '93'},
        {'id': '949', 'Date': '2022-04-13 ', 'S_Id': '28381', 'Lead_num': '142'},
        {'id': '950', 'Date': '2022-04-13 ', 'S_Id': '28469', 'Lead_num': '21'},
        {'id': '951', 'Date': '2022-04-13 ', 'S_Id': '28665', 'Lead_num': '81'},
        {'id': '952', 'Date': '2022-04-13 ', 'S_Id': '29471', 'Lead_num': '53'},
        {'id': '953', 'Date': '2022-04-08 ', 'S_Id': '541897', 'Lead_num': '33'},
        {'id': '954', 'Date': '2022-04-13 ', 'S_Id': '543341', 'Lead_num': '16'},
        {'id': '955', 'Date': '2022-04-108 ', 'S_Id': '544583', 'Lead_num': '96'},
        {'id': '956', 'Date': '2022-04-13 ', 'S_Id': '546443', 'Lead_num': '26'},
        {'id': '957', 'Date': '2022-04-13 ', 'S_Id': '549183', 'Lead_num': '37'},
        {'id': '958', 'Date': '2022-04-13 ', 'S_Id': '20752', 'Lead_num': '51'},
        {'id': '959', 'Date': '2022-04-13 ', 'S_Id': '20808', 'Lead_num': '67'},
        {'id': '960', 'Date': '2022-04-13 ', 'S_Id': '23698', 'Lead_num': '11'},
        {'id': '961', 'Date': '2022-04-05', 'S_Id': '565020', 'Lead_num': '32'},
        {'id': '962', 'Date': '2022-04-07 ', 'S_Id': '566970', 'Lead_num': '03'},
        {'id': '963', 'Date': '2022-04-12 ', 'S_Id': '164899', 'Lead_num': '74'}]

Data[1].items()

Id = []
Date = []
S_Id = []

for dict in Data:
    for key, value in dict.items():
        if key == 'id':
            Id.append(value)
        elif key == 'Date':
            Date.append(value)
        elif key == 'S_Id':
            S_Id.append(value)


df = pd.DataFrame([Id[0:len(Id)], Date[0:len(Date)], S_Id[0:len(S_Id)]],
                  index=['Id', 'Date', 'S_Id'],
                  columns=range(1, len(S_Id) + 1))

df.to_excel('HW.xlsx',index=False)

df2 = df.T

df2.to_excel('HW.xlsx',index=False)

print("End")

#---Easy way

df = pd.DataFrame(Data)

df.to_excel('HW1.xlsx',index=False)

print("End")











