

with open("simple_shit/sumene.txt",'r') as fh:
  """
  this is a simple test to exteract phone number and address from a text file 
  just using list compressions  
  """
  content=[i.rstrip('\n') for i in fh.readlines() if i!= '\n' and i[:3].isdigit()]
  ph_no=[content[i] for i in range(len(content)) if i%2==0]
  address=[content[i] for i in range(len(content)) if i%2!=0]
  print(ph_no)
  print(address)


  


    
  
    

    
    
   
            
       
 
    
    
   