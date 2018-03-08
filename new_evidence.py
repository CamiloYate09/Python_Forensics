	_fields_ = [

	("evidence_int", c_int),
	("evidence_long", c_long),
	("evidence_char", c_char * 4)

	]

value = input("Enter new evidence number:")
new_evidence = case(int(value))
print("Evidence number as a int : %i" % new_evidence.evidence_int)
print("Evidence number as a long: %Ld" % new_evidence.evidence_long) 
print("Evidence number as a char: %s" %  new_evidence.evidence_char)
