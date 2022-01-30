

file_name = 'names.txt'

with open(file_name,'r') as file:
    for names in file:
        first_name,last_name = names.strip().lower().split(' ')
        generated_file_name = './named_files/'+last_name+ '_'+first_name +'_01_hw_117.txt'
        open(generated_file_name,'w')