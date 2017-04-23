# Can I get unique letters?
# Could possible loop through, 

def recoverSecret(triplets):
    secret_list = [*triplets[0]]
    for triplet in triplets:
        for letter in triplet:
            try:
                print("letter", letter)
                # See if a letter is already in secret_list array
                index = secret_list.index(letter)

                # If exists then insert the rest of triplet array into secret_list
                index_of_letter_in_triplet = triplet.index(letter)
                secret_list.insert(index, triplet[index_of_letter_in_triplet:])
            except:
                pass

    print("secret_list", secret_list)
# first pass
['t', 'u', 'p']

# second pass - no match so leave it
['t', 'u', 'p']

# third pass - 2 matches
['t', 's', 'u', 'p']

if __name__ == "__main__":
    triplets = [
      ['t','u','p'],
      ['w','h','i'],
      ['t','s','u'],
      ['a','t','s'],
      ['h','a','p'],
      ['t','i','s'],
      ['w','h','s']
    ]
    recoverSecret(triplets)
