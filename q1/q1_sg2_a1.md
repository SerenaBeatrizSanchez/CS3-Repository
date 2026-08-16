Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9-Samat___________________________ Score:____________
C# / Name: 28 / Sanchez, 29 / Santos, 30 / Sibal   Date: 08/16/2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The PSHS school canteen’s inefficient way of handling transactions causes students to get stuck in long queues.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Some students take too long to order which overall affects the already delayed process of the canteen.

2. No merchandise tracking system makes the transaction processes of the canteen experience a setback.

3. The cashiers have to manually calculate the total and change for each student. 

4. Not all students get to eat due to limited time and long queues.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem 1: Some students take too long to order.
CT Skill: Pattern Recognition
Example Solution: Identify which products students like best and label them like “Popular” to spark their interest and to fasten the ordering process.

Sub-Problem 2: Lack of tracking system
CT Skill: Algorithm Design
Example Solution: Break inventory information into smaller pieces by creating spreadsheets to track, update, record and check the stocks.

Sub-Problem 3: Manual Calculation
CT Skill: Deposition
Example Solution: Provide a calculator for the cashier to speed up calculation process.

Sub-Problem 4: Limited time and long queues
CT Skill: Deposition
Example Solution: Break down the entire process by implementing two cashier stations and equally dividing the queues for faster production.

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
 start


Create spreadsheet for recording orders
Display popular products and prices
Display products and prices


While there are students in the queue


    if queue ≥ 10:
        Divide one long queue into two queues
    else:
        Assign student to an available cashier station
    end if


    Student selects product
    Student selects quantity


    Calculate total price
    Display total price


    Receive payment
    Calculate change
    Display change
    If change > 0:
       Give student change
       Give student product/s
    Else: 
       Give student product/s
 
    Record the following in the spreadsheet:
        Product
        Quantity
        Total price
        Payment
        Change
        Cashier station


    Move on to the next student


exit()

