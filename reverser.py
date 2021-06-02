def reverse(sentence):
    # Get words: 
    words = sentence.split() #create array of each word

    # Remove trailing period if necessary: 
    period = False
    if(words[len(words)-1][-1] == "."): #if last word ends with a period
        period = True
        last = list(words[len(words)-1]) #get last word of string
        last[-1] = "" #remove period
        words[len(words)-1] = "".join(last) #replace last word with modified version
    
    # Reverse the words: 
    words.reverse() #reverse array of words

    # Create string of reversed words: 
    reversed = ""
    for w in words: #for each word in the words array
        reversed += w 
        # Put space between each word except last; add period at end if originally was one
        if(w == words[len(words)-1]):
            if(period): #if original sentence ended with a period
                reversed += "."  #append period
        else: #if not the last word
            reversed += " " #append a space, between each word

    # Return reversed string
    return reversed

print(reverse("My name is V Tadimeti."))