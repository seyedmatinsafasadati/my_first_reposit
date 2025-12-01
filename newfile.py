def get_raw_list():
    raw=input ("enter your num: ")
    part=raw.split(',')
    clean=[]
    for x in part:
        clean.append (x.strip())
    return clean

def convert_and_filter(lst):
    clean=[]
    for item in lst:
        try:
            x=int(item)
            if x>0:
                clean.append (x)
        except ValueError:
                pass  

    return clean
    
def remove_duplicates(lst):
    unique=[]
    for x in lst:
        if x not in unique:
            unique.append (x)
            
    return unique
    
def analyze_numbers(lst):
    if len(lst)==0:
        return None
    lst_sort=sorted(lst)
    totally=sum(lst)
    avg=totally/len(lst)
    max1=max(lst)
    min1=min(lst)
    return {
         "sorted":lst_sort, 
         "sum":totally, 
         "average":avg, 
         "max":max1, 
         "min":min1
   }
   
def save_json(results):
    import json
    with open ("results.json","a",encoding=" utf-8") as f :
        json.dump(results, f, ensure_ascii=False)
        f.write ("\n")

   
def main():
    while True:
         print ("برای وارد کردن اعداد و انالیزشون عدد 1 را وارد کنید:")
         print ("برای خروج عدد 2 را وارد کنید :")
         chose=input ("گزینه خود را وارد کنید:")
         if chose=="1":
             data=get_raw_list() 
             number=convert_and_filter(data)
             unique=remove_duplicates(number)
             results=analyze_numbers(unique)
             print(results)
             save_json(results)
         elif chose=="2":
              print ("خدانگهدار")
              break
         else:
              print ("1 یا 2 این چیه وارد کردی")
              
         
if __name__=="__main__":
      main()
     

      