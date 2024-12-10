import re

INPUT_FILE = "input.txt"

def part1(replacements: list[str], molecule: str):
    
    new_molecules = set()

    for orig_part, new_part in replacements:
        
        for m in re.finditer(orig_part, molecule):
            new_mol = molecule[:m.start()] + new_part + molecule[m.end():]
            new_molecules.add(new_mol)

    print(f"Part 1: {len(new_molecules)}")


def _step(replacements: list[str], ans_mol: str, mol: str, step: int, least_steps: set):
    if mol == ans_mol:
        print("Found answer")
        least_steps.add(step)
        return
    
    if least_steps and step >= min(least_steps):
        print("Too many steps")
        return
    
    if len(mol) > len(ans_mol):
        # print("Too long")
        return

    for orig_part, new_part in replacements:
        for m in re.finditer(orig_part, mol):
            new_mol = mol[:m.start()] + new_part + mol[m.end():]
            _step(replacements, ans_mol, new_mol, step+1, least_steps)



def part2(replacements: list[str], molecule: str):
    
    least_steps = set()
    print(f"len={len(molecule)}")

    _step(replacements, molecule, "e", 0, least_steps)

    if least_steps:
        print(f"\nPart 2: {min(least_steps)}")

        


def main():
    
    with open(INPUT_FILE, "r") as f:
        replacements, molecule = f.read().split("\n\n")
        replacements = [r.strip().split(" => ") for r in replacements.split("\n")]
        molecule = molecule.strip()

    part1(replacements, molecule)
    part2(replacements, molecule)

if __name__ == '__main__':
    main()