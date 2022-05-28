while True:
    def f_anagram(main, anagram):

        m_word = sorted(main)
        a_word = sorted(anagram)

        if m_word == a_word:
            return True
        else:
            return False

    main = input("What is your first word:  ")
    anagram = input("what is your anagram?")

    if main == "" or anagram == "":
        break

    print (f_anagram(main, anagram))

    