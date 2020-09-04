def class_list_swap(file_name):
    '''
    This Function takes in a file that contains names that are in alphabetical order
    with the last name first.
    ie. Last_Name, First_Name (Middle_Initial is optional)
    Reads the names from a file and saves them to a string variable.  After this it
    immediately closes the file because the work inside the file is complete.
    It then splits the names at the comma and saves them to splitlist[]. This creates a
    2 dimensional list.  It then iterates through that list swapping the order of the names
    and saving them to the swaplist still in alphabetical order according to last name, however
    the names are now listed First_Name Last_Name.
    '''
    period = open(file_name)
    studentNames = period.read()
    period.close()
    namesList = studentNames.split('\n')
    splitlist = []
    swaplist = []
    for word in namesList:
        splitlist.append(word.split(', '))
    x=0
    while x<len(splitlist):
        swaplist.append(splitlist[x][1] + ' ' + splitlist[x][0])
        x+=1
    return swaplist

def list_file_maker(file_name, students):
    '''
    This Function takes the swapped list of students or names and writes them to a file
    separating each name with a new line. It does this by iterating through the list of names
    and writing each name to the file and using string concatenation adding the '\n'
    special character
    '''
    with open(file_name, mode = 'w') as myFile:
        for word in students:
            myFile.write(word + '\n')
# These will have to be renamed to access whatever file lists that you are trying to rearrange
fileOne = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodOne.txt'
fileTwo = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodTwo.txt'
fileThree = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodThree.txt'
fileFour = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodFour.txt'
fileSix = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodSix.txt'
fileRam = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\Ram.txt'
periodOneList = class_list_swap(fileOne)
periodTwoList = class_list_swap(fileTwo)
periodThreeList = class_list_swap(fileThree)
periodFourList = class_list_swap(fileFour)
periodSixList = class_list_swap(fileSix)
periodRamList = class_list_swap(fileRam)
# Change the first parameter to the file location of the file you would like the reversed list to be saved to
# You could even overwrite the existing file, careful doing this though cause the old information will be lost
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodOneCorrected.txt', periodOneList)
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodTwoCorrected.txt', periodTwoList)
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodThreeCorrected.txt', periodThreeList)
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodFourCorrected.txt', periodFourList)
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodSixCorrected.txt', periodSixList)
list_file_maker('C:\\Users\\vein8\\Desktop\\Coding\\Python\\Name_Swapper\\PeriodRamCorrected.txt', periodRamList)
