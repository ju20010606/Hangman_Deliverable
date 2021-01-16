class Word():
  def __init__(self, chosen_word):
         self.chosen_word = chosen_word
         
         
         word = []
         guesses = []
         turn = 10
         while turn > 0: 
            # print(''.join(word))
            user_guess = input('Guess a character: ')
            turn -1
            for letter in chosen_word:
                guesses.append(user_guess)
                if letter in guesses:
                    print(letter)
                else: 
                    print('_')
            
random_word = Word('lolipop')
















        #  word = []
        #  turns = 12
        #  while '_ ' in word or not word:
        #     user_input = input ('Guess a letter: ')
        #     for letter in chosen_word:
        #                 dict = {'letter':letter, 'has_been_guessed':False}
        #                 if user_input in chosen_word:  
        #                     dict['has_been_guessed'] = True 
        #                     if dict['has_been_guessed'] == True:
        #                         word.append(letter)
        #                     elif dict['has_been_guessed'] == False:
        #                         word.append('_ ')
        #                 else:
        #                     if dict['has_been_guessed'] == True:
        #                         word.append(letter)
        #                     elif dict['has_been_guessed'] == False:
        #                         word.append('_ ')    
        
         
        #  joined_word = ''.join(word)    
        #  print(joined_word) 
         
                
                   
                
         

         
         
        #  while '_' in word or not word: 
        #     user_guess = input('Guess a letter: ')
            
        #     if letter in chosen_word:
        #             dict = {'letter':letter, 'has_been_guessed':False}
        #             if user_guess == letter:
        #                 dict['has_been_guessed'] = True
            
        #             if dict['has_been_guessed'] == False:
        #                     word.append('_')
            
        #             elif dict['has_been_guessed'] == True: 
        #                     word.append(letter)
                
        #             print(' '.join(word))   

        


# random_word = Word('lolipop')
