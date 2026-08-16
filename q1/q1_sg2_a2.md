Annex C
Code Quality Assessment Worksheet

Section: 9-Samat Score:____________

C# / Name: 28 / Sanchez, 29 / Santos 30 / Sibal Date: 08/16/2026


1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
Pseudocode number 1 will work faster when the list of numbers is large, because instead of using nested loops that compares every single element against every other element, it uses a single loop that checks the array once.

PseudoCode 1
PseudoCode 2
Uses one loop.
No
Pseudocode 1
Uses nested loops.
Yes
Pseudocode 1

Checklist to guide your answer:
2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
The first algorithm is easier to understand at first glance. It’s straight to the point, and does not contain unnecessary code.
Checklist to guide your answer:
PseudoCode 1
PseudoCode 2
Yes
Simple
Yes (~10 lines of code)
No
Simple
No (~15 lines of code)

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
The first one. Instead of creating a new set of nested loops (which you would need to do to add the new feature to Pseudocode 2) which would disrupt the original flow of the code , you’d simply be extending the code in Pseudocode 1.
Checklist to guide your answer:
PseudoCode 1
PseudoCode 2
Yes
No
Yes 
No
Yes
No

4. Testability
Which algorithm is easier to test with different inputs? Why?
The first algorithm is easier to test with different inputs. Not only can you easily test it with small lists, but it checks to see if an inputted value follows fewer conditions (again, making the whole method more straightforward in general). Finally, the produced output is predictable and clear (although algorithm 2 provides a clear and predictable result as well)
Checklist to guide your answer:

PseudoCode 1
PseudoCode 2
Yes
Yes
Yes
Yes (but algorithm 2 takes more effort)
No
Yes (however algorithm 1’s execution path is clear and linear compared to algorithm 2)


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
Unfortunately, none of the algorithms check for errors in inputted values. Neither of them check to see if there are invalid inputs (like letters), empty lists, or other inputs that could crash the code. Similarly, none of the pseudocodes have a built in code or system to avoid crashing if those inputs are inputted.
Checklist to guide your answer:
PseudoCode 1
PseudoCode 2
No
No
No
No
No
No

 
6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
We think that algorithm 1 is the way to go. Algorithm 1 is faster and straight to the point compared to algorithm 2, as it (algorithm 1) uses one loop instead of nested loops, which is also why it uses less lines of code (~10) compared to the second option (~15). Not only that, but if a person was to add a new feature to the current code, it’d be easier to do so with the first pseudocode (adding new code to the second algorithm could easily break the current code). Finally, if a user wanted to test the code with different inputs, algorithm 1’s path is clearer compared to algorithm 2.
