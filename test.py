from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("test")

@task
def taskf():
    ab = string_block.value
    return(ab)
    
@flow
def subf():
    xy = 10
    return(xy)
    
@flow
def res():
    sub = subf()
    task = taskf()
    new = task + str(sub)
    print(new)
    
if __name__ == "__main__":
    res()