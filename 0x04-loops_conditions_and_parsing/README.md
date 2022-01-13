# Bash Loops, Conditions and Parsing
## General
* How to create SSH keys
* What  is the advantage of using `#!/usr/bin/env` bash `over #!/bin/bash`
* How to use `while` `until` and `for` loops
* How to use `if`, `else`, `elif`, and `case` condition statements
* How to use the `cut` command
* What are files and other command operators and how to use them

## Tasks
* 0. Create a SSH RSA Key
Create a RSA key using ssh-keygen command and share the public key in `[0-RSA_public_key.pub](./RSA_public_key.pub)`

* 1. For Best School loop
Write a Bash script that displays "Best School" 10 times using the `for` loop `[1-for_best_school](./1-for_best_school)`

* 2. While Best School loop
Write a Bash script that displays "Best School" 10 times using the `while` loop `[2-while_best_school](./2-while_best_school)`

* 3. Until Best School loop
Write a Bash script that displays "Best School" 10 times using the `until` loop `[3-until_best_school](./3-until_best_school)`

* 4. If 9, say Hi
Write a Bash script that displays "Best School" 10 times using the `while` loop `[4-9_say_hi](./4-9_say_hi)`, but for the 9th iteration display `Hi`.

* 5. 4 bad luck, 8 is your chance
Write a Bash script that loops from 1 to 10 and:
- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for other iterations
`[5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance)`

* 6. Superstitious numbers
Write a Bash script that loops from 1 to 20 and:
- displays `"4" and then "bad luck from China"` for the 4th loop iteration
- displays `"9" and then "bad luck from Japan` for the 9th loop iteration
- displays `"17" and then "bad luck from Italy"` for the 17th loop iterations
`[6-superstitious_numbers](./6-superstitious_numbers)`

* 7. Clock
Write a bash script that displays time for 12 hours and 59 minutes:
- display hours from 0 to 12
- display minutes from 1 to 59
`[7-clock](./7-clock)`

* 8. For ls
Write a bash script that displays:
- The contents of the current directory
- in a list
- Where only the name after the first dash is displayed
