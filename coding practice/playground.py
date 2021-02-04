
def sml(a):
	print("Will implement this soon")


def test(tavishi, actual, t):
	print("Testing:", t)
	if tavishi(t) != actual(t):
		print("Test Failed: expected", actual(t), "found", tavishi(t))
	else:
		print("Test passed :)")

test(sml, min, [1,2,3,4])
test(sml, min, [2378, 19, 0])
test(sml, min, [])

test(sml, min, [1,2,3,49000])