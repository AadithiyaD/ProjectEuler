'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

words = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "one thousand"
}

def numToWords(n):
    """
    Return the English word representation of the number n.
    Parameters
    ----------
    n : int
        The number to convert to words.
    Returns
    -------
    str
        The English word representation of n.
    Examples
    --------
    >>> numToWords(1)
    'one'
    >>> numToWords(45)
    'forty-five'
    >>> numToWords(100)
    'one hundred'
    >>> numToWords(1000)
    'one thousand'

    Requires the dictionary of words
    """
    if n <= 20:
        return words[n]
    elif n < 100:
        tens, ones = divmod(n, 10)
        if ones == 0:
            return words[tens*10]
        else:
            return words[tens*10] + " " + words[ones]
    elif n < 1000:
        hundreds, remainder = divmod(n, 100)
        if remainder == 0:
            return words[hundreds] + " hundred"
        else:
            return words[hundreds] + " hundred and " + numToWords(remainder)
    elif n == 1000:
        return words[n]


wordCount = 0
for n in range(1, 1000 + 1):
    wordCount = wordCount + len(numToWords(n).replace(" ", ""))

print(wordCount)