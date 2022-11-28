### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # The equality operator has two '=' i.e. '=='.
      return True
    else  # A colon (:) is missing after the else statement.
      return False
   

  dif highest_card(self, card1 card2):  # 'dif' should be spelled 'def' and a comma is missing between 'card1' and 'card2'.
  if card1.value > card2.value: # The code within the highest_card function needs to be indented.
    return card   # The 'card' variable does not exist in this method and should be changed to 'card1'.
  else:
    return card2
  


def cards_total(self, cards):
  total   # total is not declared and should be set to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # The return needs to be de-indented as it needs to return after all the card items are looped through
    # Strings and integers cannot be combined without either using the str() function on total i.e. str(total) or changing the return statement to an f string and surrounding total by curly brackets i.e. f"You have a total of {total}"
  
```
