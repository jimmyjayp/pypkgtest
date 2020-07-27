
import parentpkg.parentA


def funcB():
	print("parentpkg.childpkg.childB.funcB")


def funcB2():
	print("calling parentA funcA")
	parentpkg.parentA.funcA()
