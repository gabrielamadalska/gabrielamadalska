
def are_anagrams(s1, s2, s3):

    #The TRY block lets us test a block of code for errors.
    #The condition is fulfilled when s1, s2 and s3 are strings.
    try:

        #The IF statement allows us to check if strings consist of letters only.
        if s1.isalpha() and s2.isalpha() and s3.isalpha():

            # Defining s1, s2, s3 using the STRING.LOWER() method which returns the lowecasted strings.
            # This action lets us to compare strings later.
            s1 = s1.lower()
            s2 = s2.lower()
            s3 = s3.lower()

            #The LEN(STRING) function returns the number od letters in the string.
            #The IF statement allows us to check if strings is not longer than 5.
            if len(s1) and len(s2) and len(s3) <= 5:

                #The method SORTED(string) sorts the string alphabetically.
                #The function returns TRUE if the condition is true - if strings are anagrams.
                #The function returns FALSE if the condition is not true - if strings are not anagrams.
                return sorted(s1) == sorted(s2) == sorted(s3)

            else:

                #The function PRINT() gives us information that minimum one string is too long.
                print("Strings longer than 5.")

        else:
            #The function PRINT() gives us information that minimum one string doesn't contain just letters.
            print("Strings are not just letters.")


    #The EXCEPT block indicates an exception without breaking the code.
    except AttributeError:

        #The function PRINT() gives us information that s1 or s2 or s3 isn't the string.
        print("Use strings only.")


are_anagrams(s1, s2, s3)