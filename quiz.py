from cryptography.fernet import Fernet

x = [104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114,
     105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 119, 101, 102, 102, 107, 102, 112, 102, 108, 101, 109, 115, 105, 115, 111, 100, 100]

y = [chr(i) for i in x]
print("".join(y))

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdXFFWYp0Wd_sz8QWZ3uxf7zsViohXS2q7tOuTw6Ta0D6VSr9o7fd-ucZyVRv5A0SkFQK4Pjgoy7alFDKFiONxtjQppXIcIVCM_Jgxj8_ETDflGrypDtq789K4piLTJUQOvO-nN1SJZdTothn1edOpSCO5WuMrcesHj_EMzpIHjAOhSRA='

def main():
  f = Fernet(key)
  print(f.decrypt(message))

if __name__ != "__main__":
  main()

main()
