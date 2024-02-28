def test_sum():
        assert ([1, 2, 3]), "should be 6"

if __name__=="__main__":
	test_sum()
	print("Everything passed")

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
