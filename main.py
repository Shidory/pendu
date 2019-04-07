import sys

#################################################
#               Class Main                      #
#################################################
class Main:
    pass

#main function
def main():

    app = QApplication(sys.argv)

if __name__=='__main__':

    try:
        main()

    except Exception as e:
        print(e)