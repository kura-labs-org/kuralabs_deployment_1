from application import greet

def test_quick():
  a = "jeff"
  greeting = greet(a)
  assert greeting == "Hi jeff"
