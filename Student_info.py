class telebe_melumatlari:
    student_code_list=[]
    student_name_list=[]
    student_surname_list=[]
    student_email_list=[]
    student_phone_list=[]
    
    def __init__(self):
        
        self.Proqram_Haqqinda()
        self.melumati_al()
        
  
            
    def Proqram_Haqqinda(self):
        print("""Telebe melumatlarinin daxil edilmesi ve idare olunmasi proqramina xos gelmisiniz! Programi başladarken sizden telebe melumatlarını daxil etmek teleb olunur.
Birinci növbede daxil edeceyiniz telebelerin ümumi sayını qeyd edirsiz ve sizin qeyd etdiyiniz say qeder sizden telebelerin, "Kodu", "Adı", "Soyadı", "Email-i" ve "Telefon nömresi teleb
olunacaq. Telebeleri adian göre axtarmaq üçün "AdinaUygunAxtar()"  telebe koduna göre melumatları deyişm?k isteyirsinizse "Koda_Gore_Melumat_Deyisdir()", telebe melumatlarini silmek
isteyirsinizse "Melumati_Sil()", bütün telebe melumatlarını göstermek isteyirsinizse "Butun_Telebeleri_Goster()", standarta uyğun olmadığı üçün sisteme daxil edilmeyen telebenin
email ve ya telefonunu hemin telebeye elave etmek isteyirsinizse "Email_Telefon_Elave_Et()", telebelerin melumatlarini listler sekilinde goruntulemek ucun
"goster()" funsksiyasını çağırın """)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("""DIQQET! kodlarda Class olaraq 'telebe_melumatari' adi verilmisdir ve bu Class 'telebe' adli deyisene verilmisdir. Bu sebebder yuxarida gosterilen funksiyalari cagirarken
asagidaki numuneye uygun cagirin:
telebe.AdinaUygunAxtar()""")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    def melumati_al(self):

        ### How much student #############
        self.telebe_sayi=int(input("Telebe sayini qeyd edin:"))
        ### How much student #############

        self.m=1

        while self.m<=self.telebe_sayi:
            ######### input code ####################
            self.code=int(input("Telebe kodunu daxil edin:"))


            if 2<len(str(self.code))<4:
                self.student_code_list.append(self.code)
                print("********************************************")
                print("Telebe kodu sisteme ugurlar elave edildi")
                print("********************************************")

            else:
                self.id_code=100
                if self.id_code in self.student_code_list:
                    self.id_code+=1
                    self.student_code_list.append(self.id_code)
                        
                if self.id_code not in self.student_code_list:
                    self.student_code_list.append(self.id_code)

                print("********************************************")
                print("Daxil etdiyiniz telebe kodu 3 reqemli olmadigi ucun sistem terefinden avtomatik verilen id kod: {}".format(self.id_code))
                print("********************************************")
                ######### input code ####################
                        

                    
                    
                    

                
                        

                        
                        

            ##################### input name ###############################
            while True:
                
                self.name=input("Telebe adini qeyd edin:")

                if self.name == "":
                    print("Telebenin adini daxil edin!")
                    continue
                if isinstance(self.name,str):
                    self.student_name_list.append(self.name)
                    break
                else:
                    print("Telebenin adini daxil edin!")
                    continue
            
            print("*********************************************")
            print("Telebe adi sisteme ugurlar elave edildi")
            print("*********************************************")
            ##################### input name ###############################
            
            ##################### input surname ###############################
            self.surname=input("Telebe soyadini qeyd edin:")

            self.student_surname_list.append(self.surname)
            print("*********************************************")
            print("Telebe soyadi sisteme ugurla elave edildi")
            print("*********************************************")
            ##################### input surname ###############################
            
            ##################### input email ###############################
            while True:
                self.email=input("Telebe emailini qeyd edin:")

                self.email_list=list(self.email)
            

                if "@" in self.email_list:
                    self.student_email_list.append(self.email)
                    print("*********************************************")
                    print("Telebe email-i sisteme ugurla elave edildi")
                    print("*********************************************")
                    break
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Daxil etdiyiniz melumat email olmadigi  ucun sisteme elave olunmadi!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    continue

            ##################### input email ###############################

            ##################### input phone ###############################
            while True:
                self.phone=input("Telebenin telefon nomresi (+994-ile):")

                self.phone_list=list(self.phone)

                if self.phone_list[0]=="+" and self.phone_list[1]=="9" and self.phone_list[2]=="9" and self.phone_list[3]=="4":
                    self.student_phone_list.append(self.phone)
                    print("*********************************************")
                    print("Telebenin telefon nomresi ugurlar sistem elave edildi")
                    print("*********************************************")
                    break
                if self.phone_list == "":
                    continue
                
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Telefon nomresi standarta (evvelinde '+994') uygun olmadigi ucun sisteme elave olunmadi!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    continue
            ##################### input phone ###############################

            self.m+=1
######## Search for student name ###########################################################################
    def AdinaUygunAxtar(self):
        self.student_name=input("Melumati axtarilan telebe adi:")

        for self.student in self.student_name_list:
            if self.student==self.student_name:
                self.name_index=self.student_name_list.index(self.student)

                print("{}-adli telebenin, telebe kodu {}, soyadi: {}, email unvani: {}, telefon nomresi: {}".format(self.student_name,self.student_code_list[self.name_index],
                                                                                                             self.student_surname_list[self.name_index],self.student_email_list[self.name_index],
                                                                                                             self.student_phone_list[self.name_index]))


######## Search for student name ###########################################################################

############ Change information for student code #########################################################
    def Koda_Gore_Melumat_Deyisdir(self):
        self.input_student_code=int(input("Telebe kodunu daxil edin:"))
        print("----------------------------------------------------------------------------------------------------------")
        print("""Telebenin hansi melumatini deyisdirmek isteyirsinizse onu asagidaki kimi daxil edin:
kodunu deyisdirmek isteyirsinizse =>kod,adini deyisdirmek isteyirsinizse => ad, soyadini deyisdirmek isteyirsinizse => soyad, emailini deyisdirmek isteyirsinizse =>email,
telefon nomresini deyisdirmek isteyirsinizse => telefon --kimi qeyd edin!""")
        print("-----------------------------------------------------------------------------------------------------------")
        self.sayi=int(input("Ne qeder melumati deyisdirmek isteyirsinizse sayini qeyd edin:"))

        self.MelumatlariDeyisdir(self.input_student_code,self.sayi)


    def MelumatlariDeyisdir(self,input_student_code,sayi):

        self.m=1

        while self.m<=self.sayi:
            self.change=input("Deyisdirmek istediyiniz melumatin yuxarida gosterilen formada acar sozunu daxil edin:")
            self.change=self.change.lower()
            if self.change=="kod":
                self.replace_data=input("Yeni kodu daxil edin:")

            if self.change=="ad":
                self.replace_data=input("Yeni adi daxil edin:")

            if self.change=="soyad":
                self.replace_data=input("Yeni soyadi daxil edin:")

            if self.change=="email":
                self.replace_data=input("Yeni email-i daxil edin:")

            if self.change=="telefon":
                self.replace_data=input("Yeni telefonu daxil edin:")
                
                
                
                

            self.m+=1

            for self.s in self.student_code_list:
                if self.s==self.input_student_code:
                    self.info_index=self.student_code_list.index(self.s)

                    if self.change=="kod":
                        if self.replace_data not in self.student_code_list:
                            self.student_code_list.remove(self.student_code_list[self.info_index])
                            self.student_code_list.insert(self.info_index,int(self.replace_data))
                            print("*************************************************************************************************")
                            print("{},{} ile evez edildi".format(self.input_student_code,int(self.replace_data)))
                            print("*************************************************************************************************")

                        else:
                            print("Daxil etdiyiniz 'id' kod unikal olmadigi ucun qebul edilmedi!")
                    
                    if self.change=="ad":
                        print("*************************************************************************************************")
                        print("{},{} ile evez edildi".format(self.student_name_list[self.info_index],self.replace_data))
                        print("*************************************************************************************************")
                        self.student_name_list.remove(self.student_name_list[self.info_index])
                        self.student_name_list.insert(self.info_index,self.replace_data)
                        

                    if self.change=="soyad":
                        print("*************************************************************************************************")
                        print("{},{} ile evez edildi".format(self.student_surname_list[self.info_index],self.replace_data))
                        print("*************************************************************************************************")
                        self.student_surname_list.remove(self.student_surname_list[self.info_index])
                        self.student_surname_list.insert(self.info_index,self.replace_data)

                    if self.change=="email":
                        if "@" in self.replace_data:
                            print("*********************************************************************************************************")
                            print("{},{} ile evez edildi".format(self.student_email_list[self.info_index],self.replace_data))
                            print("*********************************************************************************************************")
                            self.student_email_list.remove(self.student_email_list[self.info_index])
                            self.student_email_list.insert(self.info_index,self.replace_data)


                        else:
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Daxil etdiyiniz melumat email olmadigi  ucun sisteme elave olunmadi!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            

                    if self.change=="telefon":
                        
                        
                        self.replace_data_list=str(self.replace_data)
                        if self.replace_data_list[0]=="+" and self.replace_data_list[1]=="9" and self.replace_data_list[2]=="9" and self.replace_data_list[3]=="4":
                            print("*********************************************************************************************************")
                            print("{},{} ile evez edildi".format(self.student_phone_list[self.info_index],self.replace_data))
                            print("*********************************************************************************************************")
                            self.student_phone_list.remove(self.student_phone_list[self.info_index])
                            self.student_phone_list.insert(self.info_index,self.replace_data)
                            
                        else:
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Telefon nomresi standarta (evvelinde '+994') uygun olmadigi ucun sisteme elave olunmadi!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
############ Change information for student code #########################################################

############## Delete Information ######################################################################
    def Melumati_Sil(self):
        self.student_code=int(input("Telebe kodunu daxil edin:"))

        for self.s in self.student_code_list:
            if self.s==self.student_code:
                self.info_index=self.student_code_list.index(self.s)

                self.student_code_list.remove(self.student_code_list[self.info_index])
                self.student_name_list.remove(self.student_name_list[self.info_index])
                self.student_surname_list.remove(self.student_surname_list[self.info_index])
                self.student_email_list.remove(self.student_email_list[self.info_index])
                self.student_phone_list.remove(self.student_phone_list[self.info_index])
        print("{} nomreli telebenin butun melumatlari silindi".format(self.student_code))

############## Delete Information ######################################################################

############## Show all Student ############################################################
    def Butun_Telebeleri_Goster(self):
        for self.s in self.student_name_list:
            self.info_index=self.student_name_list.index(self.s)
            print("Kodu: {}, Adi: {}, Soyadi: {}, Email: {}, Telefon: {}".format(self.student_code_list[self.info_index],self.student_name_list[self.info_index],
                                                                             self.student_surname_list[self.info_index],self.student_email_list[self.info_index],
                                                                             self.student_phone_list[self.info_index]))
############## Show all Student ############################################################


##################### Add Email and Phone ##################################################
    def Email_Telefon_Elave_Et(self):
        self.input_student_name=input("Telebe adini daxil edin:")
        print("-------------------------------------------------------------------------------------------")
        print("""Telebenin hansi melumatini elave etmek isteyirsinizse onu asagidaki kimi daxil edin:
emailini elave etmek isteyirsinizse =>email,
telefon nomresini elave etmek isteyirsinizse => telefon --kimi qeyd edin!""")
        print("-------------------------------------------------------------------------------------------")
        self.sayi=int(input("Ne qeder melumat elave etmek isteyirsinizse sayini qeyd edin:"))

        self.m=1

        while self.m<=self.sayi:
            self.insert=input("Elave etmek istediyiniz melumatin yuxarida gosterilen formada acar sozunu daxil edin:")
            self.insert=self.insert.lower()

            if self.insert=="email":                
                self.insert_data=input("email-i daxil edin::")
            else:
                self.insert_data=input("Telefonu daxil edin:")

            self.m+=1

            for self.s in self.student_name_list:
                if self.s==self.input_student_name:
                    self.info_index=self.student_name_list.index(self.s)


                    if self.insert=="email":
                        self.insert_data_list=list(self.insert_data)
                        if "@" in self.insert_data_list:
                            if len(self.student_code_list)!=len(self.student_email_list):
                                self.student_email_list.insert(self.info_index,self.insert_data)
                                print("{} adli telebe ucun {} emaili elave edildi".format(self.input_student_name,self.insert_data))

                            else:
                                print("********************************************************************************************************************************************")
                                print("{} adli telebenin {} email-i artiq movcuddur. Bir telebe ucun yalniz bir email daxil ede bilersiz".format(self.input_student_name,
                                                                                                                                                 self.student_email_list[self.info_index]))
                                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("Telebelerin melumatlarinda deyisiklik etmek isteyirsinizse 'Koda_Gore_Melumat_Deyisdir()' funksiyasini cagirin!")
                                print("********************************************************************************************************************************************")

                        else:
                            print("*****************************************************************")
                            print("Email daxil etmediyiniz ucun melumat sisteme elave olunmadi!")
                            print("*****************************************************************")

                    if self.insert=="telefon":
                        self.insert_data_list=list(self.insert_data)
                        if self.insert_data_list[0]=="+" and self.insert_data_list[1]=="9" and self.insert_data_list[2]=="9" and self.insert_data_list[3]=="4":
                            if len(self.student_code_list)!=len(self.student_phone_list):
                                self.student_phone_list.insert(self.info_index,self.insert_data)
                                print("*********************************************************************************************************")
                                print("{} adli telebe üçün {} nömreli telefon elave edildi".format(self.input_student_name,self.insert_data))
                                print("*********************************************************************************************************")

                            else:
                                print("********************************************************************************************************************************************")
                                print("{} adli telebenin {} telefonu artiq movcuddur. Bir telebe ucun yalniz bir email daxil ede bilersiz".format(self.input_student_name,
                                                                                                                                                  self.student_phone_list[self.info_index]))
                                print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("Telebelerin melumatlarinda deyisiklik etmek isteyirsinizse 'Koda_Gore_Melumat_Deyisdir()' funksiyasini cagirin!")
                                print("********************************************************************************************************************************************")
                                

                        else:
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Telefon nomresini qaydalara uygun daxil etmediyiniz ucun sisteme elave olunmadi!(evveline '+994' yazilmalidir)")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


##################### Add Email and Phone ##################################################
                            
        

                

        
        
        
############ Show Information in list ######################################

    def goster(self):
        print(self.student_code_list)
        print(self.student_name_list)
        print(self.student_surname_list)
        print(self.student_email_list)
        print(self.student_phone_list)
############ Show Information in list ######################################


telebe=telebe_melumatlari()

            
            
        

        

        
