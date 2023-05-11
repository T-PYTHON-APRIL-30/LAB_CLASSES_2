# LAB_CLASSES_2

**Exercise:**

Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`) =0, setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

---------

# Bonus

## define a Vehicle class . it has the following structure :

#### properties attrabuite
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 
