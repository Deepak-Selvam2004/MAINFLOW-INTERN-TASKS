#IMPLEMENTATION OF SECOND HALF PART OF THE TASK-1
print("\t","\t","***  LIST MODIFICATIONS   ***", "\t","\t")
print("-------------------------------------------------------")
#original list
list=[0,1,2,3,4,5,6,7,8,9]
print('THE CREATED LIST:',list)

#adding an element to a list
list.append('10')
print('THE LIST AFTER ADDING AN ELEMENT:',list)

#removing an element from a list
list.remove('10')
print('THE LIST AFTER REMOVING AN ELEMENT:',list)

#modifying an element in a list
list[0]=10
print('THE LIST AFTER MODIFYING AN ELEMENT:',list)

#inserting an element in a list
list.insert(2,'11')
print('THE UPDATED LIST:',list)
print("-------------------------------------------------------")
print("\t","\t","***  TUPLE MODIFICATIONS   ***", "\t","\t")
print("-------------------------------------------------------")
#original tuple
tup=(0,1,2,3,4)
print('THE CREATED TUPLE:',tup)

#adding an element to a tuple
add_elem=5
tup_new=tup+(add_elem,)
print('THE TUPLE AFTER ADDING AN ELEMENT:',tup_new)

#removing an element from a tuple
tup_new1=tup[:1]+tup[2:]
print('THE TUPLE AFTER REMOVING AN ELEMENT:',tup_new1)

#modifying an element in a tuple
mod_tup=5
tup_new2=tup[:2]+(mod_tup,)+tup[3:]
print('THE UPDATED TUPLE:',tup_new2)
print("-------------------------------------------------------")
print("\t","\t","***  DICTIONARY MODIFICATIONS   ***", "\t","\t")
print("-------------------------------------------------------")
#original dictionary
my_dict={'first':1,'second':2,'third':3,'fourth':4,'fifth':5}
print('THE CREATED DICTIONARY:',my_dict)

#adding an element to a dictionary
my_dict['sixth']=6
print('THE DICTIONARY AFTER ADDING AN ELEMENT:',my_dict)

#removing an element from a dictionary
del my_dict['fourth']
print('THE DICTIONARY AFTER REMOVING AN ELEMENT:',my_dict)

#modifying an element in a dictionary
my_dict['second']='two'
print('THE DICTIONARY AFTER MODIFYING AN ELEMENT:',my_dict)
print("-------------------------------------------------------")