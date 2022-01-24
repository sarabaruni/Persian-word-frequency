import pickle
from parsivar import FindStems


my_stemmer = FindStems()


a_file = open("dataset/frequency_log_set.pkl", "rb")

freq = pickle.load(a_file)
def frequency(word):
    """Get the frequency of word's root
    """
    try:
        try:
            return freq[word]
        except:
            return freq[my_stemmer.convert_to_stem(word)]
    except:
        return 1


if __name__ == "__main__":
    word = input('please enter your word: ')
    # your_word = 'کتاب'
    try:
        print(frequency(word))
    except:
        print("this is a number or is'nt appropriate word")


