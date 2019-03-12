# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:34:51 2019

@author: Mahe
"""
class Apriori:
    
    def __init__(self,item,min_support,min_confidence,min_length):
        self.item=item
        self.min_support=min_support
        self.min_confidence=min_confidence
        self.controller(item,min_support,min_confidence,len(item),min_length)



        
    def nItemAtTime(self,ans,li,n):
        ans1=[]
        k=[]
        k1=[]
        if(n==0):
            print("This is ans\n",ans)
            return ans
        else:
            for i in range(len(li)):
                
                for j in range(len(ans)):
                    if(li[i] not in ans[j]):
                        k=[lk for lk in ans[j]]
                        k.extend(li[i])
                        if(sorted(k) not in k1):
                            k1.append(sorted(k))
                        k=[]
            ans1.extend(k1)
            #print(ans1,"ACtual................\n")
        return ans1
                    
    
    def nItemAtTimefromThree(self,ans,li,n):
        
        k=[]
        k1=[]
        print(1)
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if(ans[i][:n-2]==ans[j][:n-2]):
                    k.extend(ans[i])
                    k.extend(ans[j])
                    k=set(k)
                    k=list(k)
                    k1.append(sorted(k))
                    k=[]
        return k1
                  
                    
    def countforPattern(self,an,item):
        count=0
        kz=[]
        kz1=[]
        for i in range(0,len(an)):
            count=0
            for j in range(0,len(item)):
                if(set(an[i]) <= set(item[j])):
                    count+=1
            kz.extend(an[i])
            kz.append(count)
            kz1.append(kz)
            kz=[]
            
        return kz1
                    
                
    def getCi(self,ans,min_sup,m):
        li=[]
        li1=[]
        for i in ans:
            if(i[-1]>=min_sup):
                li.append(i[:-1])
                li1.append(i)
        if(m==0):
            return li1,li
        else:
            return li
    
    def checkSub(self,ans,ItemSet,n):
        print(1)
        ans1=[]
        #print(ans,"in check sub")
        
        ans1.extend(ans)
        
        cks=-1
        #print("ans is ",ans,"\n")
        #print("ans1 is ",ans1,"\n")
        for k in range(len(ans)):
            #print("length of answer is ",len(ans))
            
            c=0
            p=0
            cks+=1
            l1=[]
            
            mn=[]
            l=ans[k]
            #print(l)
            #print(k,"the value f k\n")
            while(c<n):
                p1=p
                for i in range(n-1):
                    j=p1%n
                    
                    l1.append(l[j])
                    p1+=1
                    
                mn.append(sorted(l1))
                l1=[]
                c+=1
                p+=1
            f=0
            #print("mn is ",mn)
            for i in range(len(mn)):
               f=0
               if(len(mn)==0):
                   break;
               #print(ItemSet[1],"Itemsssssssssssssss")
               #for j in range(len(ItemSet[n-2])):
                    #f=0
               if(not((mn[i]) in (ItemSet[n-2]))):
                    f=1
                    break;
                
                   
            if(f==1):
                print("prooned",ans[k])
                ind=ans1.index(ans[k])
                ans1.remove(ans1[ind])
                
               
                
          
        
            
        
        return ans1
                
            
            
         
    def conv_dict(self,ItemSet):
        dict1={}
        for i in range(0,len(ItemSet)):
            for j in range(len(ItemSet[i])):
                k=tuple(ItemSet[i][j][:-1])
                dict1[k]=ItemSet[i][j][-1]
        return dict1
        
                
    def makePairs(self,finItemSet):
        mn=[]
        mn1=[]
        for i in range(0,len(finItemSet)):
            
            for jk in range(0,len(finItemSet[i])):
                req=finItemSet[i][jk][:-1]
                ab=req
                c=0
                p=0
                n=len(ab)
                l1=[]
                l2=[]
                
                l3=[]
                
                num_per_iter=0
                l=ab
                
                while(c<n-1):
                     p1=p
                     num_per_iter+=1
                     for ilk in range(n):
                         for nItem in range(num_per_iter):
                             
                             j=(p1)%(n)
                             a=l[j]
                             p1+=1
                             l3.append(a)
                         l1.append(tuple(sorted(l3)))
                         
                         for k in range(n):
                             if(not(set(l[k]) <= set(l3))):
                                 l2.extend(l[k])
                         l1.append(tuple(sorted(l2)))
                         l2=[]
                         l3=[]
                                 
                         
                         
                         
                         mn.append(l1)
                         l1=[]
                     c+=1
                     p+=1
               
        mn1.append(mn)
        
        return mn1
    
    
    def appendConfidence(self,all_combi,sup_dict):
        for i in range(0,len(all_combi[0])):
            lhs=all_combi[0][i][0]
            rhs=all_combi[0][i][1]
            lhs=set(lhs)
            rhs=set(rhs)
            num=tuple(lhs.union(rhs))
            num=tuple(sorted(num))
            den=tuple(lhs)
            den=tuple(sorted(den))
            conf=sup_dict[num]/sup_dict[den]
            #print(conf)
            all_combi[0][i].append(conf)
            
        return all_combi
        
        
    
    def controller(self,item,min_support,min_confidence,n,min_length):


        
        unique_ele=[]
        for i in range(len(item)):
            for j in range(len(item[i])):
                if(len(unique_ele)==0):
                    unique_ele.append(item[i][j])
                else:
                    if(item[i][j] not in unique_ele):
                        unique_ele.append(item[i][j])
        set1=set(unique_ele)
        unique_ele=list(set1)
        print("Unique ele is\n ")
        print(unique_ele)
        unique_ele=sorted(unique_ele)
        
        ItemSet=[]
        ItemSet1=[]
        ItemSet2=[]
        ans=[[] for x in unique_ele]
        for i in range(len(unique_ele)):
            ans[i].append(unique_ele[i])
        
        ans1=self.countforPattern(ans,item)
           # All element combination with their count
            
        ItemSet2.append(ans)     # All elements ,all possible combination
        ans1,ans=self.getCi(ans1,min_support,0)
        ItemSet.append(ans)   # All elements that has support greater than min sup
        ItemSet1.append(ans1) 
        
        if(min_length>=2):
            ans=self.nItemAtTime(ans,unique_ele,2)
            ans1=self.countforPattern(ans,item)
            
            ItemSet2.append(ans)
            #print(ans1,"for l-2")
            ans1,ans=self.getCi(ans1,min_support,0)
            ItemSet.append(ans)
            ItemSet1.append(ans1)
            
        
        for i in range(3,min_length+1):
            ans=self.nItemAtTimefromThree(ans,unique_ele,i)
            ans1=self.countforPattern(ans,item)  # It returns a list with the count of each element of ans
            
            ItemSet2.append(ans)
            ans=self.checkSub(ans,ItemSet,i)
            ans1,ans=self.getCi(ans1,min_support,0)   # Gives the list of items of li whose count grt or eq to min support
            ItemSet1.append(ans1)
            
            #print("Answer After ever Iter",ans)
            if(len(ans)!=0):         
                ItemSet.append(ans)
            print("the list of frequent items are\n",ItemSet1)
        #finItemSet has all element combination with support greater than min support and 
        finItemSet=[]
        for i in range(len(ItemSet)):
            a1=self.countforPattern(ItemSet[i],item)
            finItemSet.append(a1)
        #print("fINiTEMsET\n\n")
        #print(finItemSet)  
        sup_dict={}
        sup_dict=self.conv_dict(finItemSet)
        #print("Dictionary done\n\n")
        #print(list(sup_dict))
        print("\n")
        #all_combi=[]
        all_combi=self.makePairs(finItemSet[1:])
        #print("The pairs done\n\n")
        #print(all_combi)
        #print("\n")
        fin_list=self.appendConfidence(all_combi,sup_dict)
        
        final_list=fin_list[0]
        print("The confidence list\n\n")
        print(final_list)
        print("\n\n")
            
        rules=self.getCi(final_list,min_confidence,1)
        print("The required Rules\n\n")
        print(rules)
        
                
             
def main():
    
    n=int(input("Enter number of transactions\n"))
    min_support=int(input("Minimum support\n"))
    min_confidence=float(input("Minimum Confidence\n"))
    min_length=int(input(" Minimum Length of rules\n"))
    item=[]
        #db=pd.read_csv()
    print("enter one trasaction per line\n")
    for ik in range(n):
        inp=input().split()
        item.append(inp)
    y=Apriori(item,min_support,min_confidence,min_length)
    
    
      
           
if __name__ == "__main__":
    main()
        
       
                 
       
        
    
            


    




    
