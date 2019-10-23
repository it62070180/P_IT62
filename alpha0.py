"""Life PS"""
def main():
    """Version A1"""
    print("สวัสดี ยินดีต้อนรับสู่โปรแกรมตอบถามสิ่งที่พบเจอและแนะนำวิธีแก้ไขเบื้องต้นแบบไม่ต้องพึ่งพาระบบอินเตอร์เน็ต")
    lifeps = input("คำถามที่ถูกถามบ่อย \nพิมพ์ 1 เกี่ยวกับอาการป่วยพื้นฐาน \nพิมพ์ 2 สำหรับเรื่องน้ำหนัก \
    (วิธีเพิ่ม, ลดน้ำหนัก, คำนวนดัชณีมวลกาย) \nพิมพ์ 3 ปัญหามือถือต่างๆและวิธีแก้ไขเบื้องต้น \
    \nพิมพ์ เพิ่มเติม เพื่อดูปัญหาหาอื่นๆ\nโปรดระบุปัญหาของท่านตามที่ระบุไว้: ")
    lifeps1 = lifeps.upper()
    if lifeps1 == "1":
        return health()
    elif lifeps1 == "2": #ปัญหาน้ำหนักและคำนวณน้ำหนัก
        return weight()
    elif lifeps1 == "MORE" or lifeps == "เพิ่ม" or lifeps == "เติม":
        return moreps()
    elif lifeps1 == "3":
        return spfix()
def health():
    """โปรแกรมเกี่ยวกับปัญหาสุขภาพเบื้องต้น"""
    print("**เป็นโปรแกรมที่บอกวิธีการแก้ไขอาการเบื่้องต้นเท่านั้น\
    หากท่านไม่รู้สึกดีขึ้นจากการปฏิบัติตามการแก้ไขเบื้องต้น รีบไปปรึกแพทย์ผู้เชี่ยวชาญ**")
    sick = input("สวัสดีวันนี้เป็นอะไรมา \nปวดหัว เป็นไข้ ปวดท้อง ท้องเสีย เป็นต้น หรือ\
    พิมพ์ ออก เพื่อออกจากโปรแกรม\nโปรดระบุอาการของท่าน: ")
    if sick == "ปวดหัว":
        headache1 = input("ปวดหัวข้างเดียว, ปวดที่กระบอกตา เป็นต้น")
        if headache1.count("ข้างเดียว") or headache1.count("เดียว"):
            print("อาการหัวข้างเดียวอาจเกิดจากโรคไมเกรน ซึ่งโดยทั่วไปแล้วยาแก้ปวดธรรมดาแบบพาราเซตามอลมักใช้ไม่ได้ผลกับการปวดหัวแบบไมเกรน\
            \nต้องใช้ยาแก้ปวดที่แรงขึ้น เพราะฉะนั้นควรปรึกษาแพทย์เพื่อสั่งยาให้จะดีกว่า อีกอย่างหนึ่งก็คือ หากมีอาการปวดหัวจากไมเกรนบ่อยๆ\
            แพทย์จะสามารถแนะนำให้กินยาป้องกัน")
        elif headache1.count("กระบอก") or headache1.count("ตา"):
            print("")
def weight():
    """โปรแกรมเกี่ยวกับน้ำหนัก มวลร่างกาย"""
    urproblem = input("วิธีเพิ่มน้ำหนัก, วิธีบดน้ำหนัก, คำนวนดัชณีมวลกาย (BMI), หากไม่มีจากที่กล่าวมาพิมพ์ (ออก) \
    \nโปรดระบุ : ") 
    urproblem1 = urproblem.upper()
    if urproblem1.count("BMI") or urproblem.count("ดัชนี"): #BMI Calculator
main()
