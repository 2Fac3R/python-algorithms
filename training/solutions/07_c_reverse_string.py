
"""
Solution for: Reverse String with Recursion
"""

def reverse_string(s: str) -> str:
    """
    This function reverses a string using recursion.

    - Base Case: If the string is empty or has only one character, it is its own reverse.
      This stops the recursion.
    - Recursive Step: For a longer string, the reverse is the reverse of the rest of the
      string (from the second character onwards) concatenated with the first character.
      
      Example: reverse("hello")
      = reverse("ello") + "h"
      = (reverse("llo") + "e") + "h"
      = ((reverse("lo") + "l") + "e") + "h"
      = (((reverse("o") + "l") + "l") + "e") + "h"
      = ((("o") + "l") + "l") + "e") + "h"
      = "olleh"
    """
    # Base Case
    if len(s) <= 1:
        return s
    
    # Recursive Step
    return reverse_string(s[1:]) + s[0]
