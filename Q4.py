def remove_duplicate_and_sort(text):
     for i in text:
         if i not in dictionary:
             dictionary[i]=1
         else:
             dictionary[i]+=1
     sort_dictionary=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
     for i in sort_dictionary:
        result.append(i[0])
     return result
text=['one','two','two','four','four','four','four','three','three','three']
dictionary={}
result=[]
print(remove_duplicate_and_sort(text))