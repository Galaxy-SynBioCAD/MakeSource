from rdkit.Chem import MolFromInchi
inchi = 'InChI=1S/C6H6O4/c7-5(8)3-1-2-4-6(9)10/h1-4H,(H,7,8)(H,9,10)/b3-1+,4-2+'
mol = MolFromInchi(inchi)
assert mol
