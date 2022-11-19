import os
import shutil

def current_path():
    os.chdir(r"D:\CCI Corpus- Project")# set your working directory

def cci_path():
    os.chdir(r"D:\CCI\CCI Orders - 940 total orders till 2021") # set your cci directory


cci_path() # set working directory where cci corpus is present

year_folder_name = os.listdir()

year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
year_cnt = 0 # for index
file_counter = 0
empty_month = list()
multiple_order = list()

for i in year_folder_name:
    path = os.path.join(r"D:\CCI\CCI Orders - 940 total orders till 2021", str(i))
    os.chdir(path)
    directories = os.listdir()
    snum = 0
    for j in directories:
        new_path = os.path.join(path, j)
        #print(new_path)
        os.chdir(new_path)
        #print(os.getcwd())
        files =  os.listdir()
        if len(files) == 0:
            empty_month.append("{}_{}".format(i, j))
        else:
            for k in files: # k is a string with either .pdf or some name need to import re for conditional 
                if k[-4:] == ".pdf":
                    snum +=1
                    UID ="{yr}_{snum}_{onum}".format(yr = year[year_cnt],snum = snum, onum = 1)
                    src = os.path.join(new_path, k)
                    dst = "D:\CCI_txt_orders\{uid}.pdf".format(uid = UID)
                    shutil.copy(src,dst)
                else:
                    snum +=1
                    multiple_orders = os.path.join(new_path, k)
                    os.chdir(multiple_orders)
                    order = os.listdir()
                    multiple_order.append(k)# to know the cases of multiple orders
                    onum = 1
                    for o in order:
                        UID ="{yr}_{snum}_{onum}".format(yr = year[year_cnt],snum = snum, onum = onum)
                        onum +=1
                        src = os.path.join(multiple_orders, o)
                        dst = "D:\CCI_txt_orders\{uid}.pdf".format(uid = UID)
                        shutil.copy(src, dst)
    year_cnt +=1                
                        
