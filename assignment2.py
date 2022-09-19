"""
ไฮเวย์เป็นเด็กนักเรียนชั้นมัธยมศึกษาปีที่ 6 ไฮเวย์ได้ทำาการพัฒนาโปรแกรมใช้งานการส่งงานออนไลน์เพื่อ
ส่งเข้าแข่งขันในงานวิชาการ แต่โปรแกรมของไฮเวย์ยังขาดความปลอดภัยในการ login เข้าใช้งาน เนื่องจาก
โปรแกรมสามารถตั้งรหัสผ่านง่าย ๆ ได้ทำให้เกิดการเดารหัสผ่านของเพื่อนคนอื่น คุณครูจึงมอบหมายให้ไฮเวย์
เขียนค าสั่งเช็ครหัสผ่าน โดยให้เช็คจ านวนตัวอักษรพิมพ์ใหญ่ พิมพ์เล็ก ตัวเลข และสัญลักษณ์ของโปรแกรมที่สร้าง
ขึ้น ในฐานะที่นักเรียนมีความรู้ความสามารถด้านการแก้ปัญหาการเขียนโปรแกรม จงช่วยไฮเวย์พัฒนาระบบ
ดังกล่าว ตามประเด็นดังต่อไปนี้
"""


import getpass
def register():
    def error():  #on error
        print("your password is not safe try agian")
        register()

    countup = 0
    countlow = 0
    countdigit = 0
    countother = 0
    password = getpass.getpass("\n\n\n\nregister your password    ")
    try:
        for i in password:
            if i.isupper():
                countup +=1
            elif i.islower():
                countlow +=1
            elif i.isdigit():
                countdigit +=1
            else:
                countother +=1
        print(("number of {} is:    {}").format("upperletter",(countup)))
        print(("number of {} is:    {}").format("lowerletter",(countlow)))
        print(("number of {} is:    {}").format("diget",(countdigit)))
        print(("number of {} is:    {}").format("other",(countother)))

        if (countup and countlow and countdigit and countother) <1:
            error()
            if len(password) < 8:
                error()
        else:
            def login():
                loginpass = getpass.getpass("\n\n\n\nenter password    ")
                if loginpass == password:
                    print("\n\nwelcome back")
                else:
                    print("\n\npass incorrect")
                    login()
            login()

    except:
        print(("number of {} is:    {}").format("everything","None becuase there is a bug for no reason"))

register()
