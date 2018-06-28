# Maplestory2_Wizard.py
# Weapon * Magic Attack

Cur_Weapon = input("Your current Weapon:")
Cur_Magic_Attack = input("Your current Magic Attack without Penguin's buff:")
Cur_Force = input("Your current Force:")
Add_INT = input("How much INT you would like to add:")
Add_Force = input("How much Force you would like to add:")

Cur_Attack = (eval(Cur_Weapon)+3400+5*eval(Cur_Force))* eval(Cur_Magic_Attack)
Next_Attack = (eval(Cur_Weapon)+3400+5*(eval(Cur_Force)+eval(Add_Force)))* (eval(Cur_Magic_Attack)+0.58*eval(Add_INT))
Increased =100 *(Next_Attack - Cur_Attack)/Cur_Attack
print("Increased:{:.2f}%".format(Increased))

