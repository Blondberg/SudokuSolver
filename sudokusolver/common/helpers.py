# An arsenal of different helping methods

# Check if all elements in a list are unique
def all_unique(seq):
    if not seq:
        return True

    if seq[0] in seq[1:]:
        return False
    else:
        return all_unique(seq[1:])


# Test if helpers work
if __name__ == '__main__':
    assert all_unique([1,2,3,4])
    assert not all_unique([1,2,34,1])
