# ---------------------------------------------------------------------------------------------------------------------------------------------
# Assignment 1    Chinese Reminder Theorem
# Author:         Shengqian Wang
# Date:           09/18/2018
# Description:    Finds the value of x that satisfies a system of congruencies.The most part of the code is copied form the internet, some 
#				  parts are modified to meet the requirements. 
# ---------------------------------------------------------------------------------------------------------------------------------------------

# gcd and exclid code from the reference starts--------------------------------------------------
def _g_c_d(a,b):
  if 0==b:
    return a
  return gcd(b,a%b)
def Ex_Euclid(a,b):
  if 0==b:
    x=1;y=0;q=a
    return x,y,q
  xyq=Ex_Euclid(b,a%b)
  x=xyq[0];y=xyq[1];q=xyq[2]
  temp=x;x=y;y=temp-a//b*y
  return x,y,q
def Get_Inverse(a,b):
  return Ex_Euclid(a,b)[0]
def gcd(a,b):
  return Ex_Euclid(a,b)[2]
# gcd and exclid code from the reference ends---------------------------------------------------
# determine whether r, s, t are pairwise relatively prime positive integers
def Is_Coprime(m_list):
  for i in range(len(m_list)):
    for j in range(i+1,len(m_list)):
      if 1!=gcd(m_list[i],m_list[j]):
        return 0  # not pairwise relatively prime
  return 1  # is pairwise relatively prime
def Get_Mi(m_list,M):
  Mi_list=[]
  for mi in m_list:
    Mi_list.append(M//mi)
  return Mi_list
def Get_Mi_inverse(Mi_list,m_list):
  Mi_inverse=[]
  for i in range(len(Mi_list)):
    Mi_inverse.append(Get_Inverse(Mi_list[i],m_list[i]))
  return Mi_inverse
# This function of Chinese Reminder Theorem returns x as the result
def C_R_T():
  while True:
    # Create two empty lists to store values.
    m_list=[]
    b_list=[] 
    
    for x in range(0, 3): 
      b_i=input("Please input the a, b, and c :")
      if False==b_i.isnumeric():
        print("Oops! That was no valid number.  Try again: ")
        b_i=input()
        continue
      else:
        b_list.append(int(b_i))
    
    for x in range(0,3): 
      m_i=input("Please input the r, s, and t :")
      if False==m_i.isnumeric():
        print("Oops! That was no valid number.  Try again: ")
        m_i=input()
        continue
      else:
        m_list.append(int(m_i)) 
    if 0==Is_Coprime(m_list):
      print("Oops! r, s,and t are not pair wise relatively prime positive integers.  Try again: \n")
    else:
      break
  M=1
  for mi in m_list:
    M*=mi
  Mi_list=Get_Mi(m_list,M)
  Mi_inverse=Get_Mi_inverse(Mi_list,m_list)
  x=0
  for i in range(len(b_list)):
    x+=Mi_list[i]*Mi_inverse[i]*b_list[i]
    x%=M
  return x
if __name__=='__main__':
	print("The Answer is：x=%d" % C_R_T())
