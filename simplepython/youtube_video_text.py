def plusOne( digits):
        carry=0
        output=[]
        print(len(digits))
        for i in range(len(digits)-1,-1,-1):
            print(i)
            if digits[i]==9 and carry==0:
                carry=1
                output.insert(0,0)
            elif carry==1 and digits[i]==9:
                digits[i]+1
                carry=1
                output.insert(0,0)
            else:
                carry=0
                output.insert(0,digits[i])
        print(output)

# main
plusOne([9,9,9])
        