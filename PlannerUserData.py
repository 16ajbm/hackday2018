
class User():
    def __init__(self, user, new_file=True):
        self.user = user

        if new_file = True:
            # create new file
            f = open("%s.txt" % (user))
        else:
            # auto load file
            read_file(self.file)
            
        self.file = "%s.txt" % (user)            
        self.exercises = []
        self.weights = {}
        self.last_routine = []
        self.current_routine = []
        

    def read_file(filename):
        f = open(filename, 'r')
        ex_ind = 0
        w_ind = 0
        first_line = True
        for line in f:
            if first_line = True:
                #last_routine line
                if line != "":
                    #split into list of strings
                    self.last_routine = line.split(',')
                else:
                    #no last routine
                    self.last_routine = []
            else:
                #split line into list of elements
                elements = line.split(',')
                #first element is exercise name
                self.exercises[ex_ind] = elements[0]
                #greater than one set
                if len(elements) > 4:
                    sets = []
                    #iterate line to make list of each set
                    for i in range(1,len(elements)-1,3):
                        j = i+1
                        k = i+2
                        set_i = [elements[j],elements[k]]
                        sets.append(set_i)
                    self.weights[self.exercises[ex_ind]]=sets
                else:
                    single_set = [elements[2],elements[3]]
                    self.weights[self.exercises[ex_ind]]=sets
                ex_ind += 1
                w_ind += 1
        f.close()
        return "user loaded"

    def write_file(filename):
        f = open(filename,'w')
        #concatenate list via ','
        for ex in self.exercises:
            line = [ex]
            for element in self.weights[ex]:
                line.append(element)
            f.write(str(line) + "\n")
        return "user saved"

    def add_exercise(exercise,weight):
        self.exercise.append(exercise)
        self.weights[exercise] = weight

    def remove_exercise(exercise):
        self.exercise.remove(exercise)
        self.weights.pop(exercise)

    
        

            
