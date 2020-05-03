'''
url: https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Descprition:

Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1
foobar23 -> foobar24
fo123ee456 -> fo123ee457
f1oo9 -> f1oo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''
# Solution:

def increment_string(strng):
    global feed

    if strng == '': return '1'
    
    # split Data
    nums = ''
    let = ''

    for i in strng:
        if i.isdigit() is True:
            nums += i
        else:
            let += i
    
    if len(nums) == 0:
        return strng+'1'
    
    # get last number
    for i, c in enumerate(reversed(strng)):
        if c.isdigit() is False:
            index = i
            nums = nums[-index:]
            break

    n = len(nums)
    
    # Add 1 to last number
    nums1 = int(nums) + 1
    
    # Check if number have leading zeros
    nums1 = str(nums1).zfill(len(nums))
    
    #return result
    return strng[:-n]+str(nums1)
