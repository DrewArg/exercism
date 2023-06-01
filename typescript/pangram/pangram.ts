const alphabet = new Array<String>();
alphabet.push("a");
alphabet.push("b");
alphabet.push("c");
alphabet.push("d");
alphabet.push("e");
alphabet.push("f");
alphabet.push("g");
alphabet.push("h");
alphabet.push("i");
alphabet.push("j");
alphabet.push("k");
alphabet.push("l");
alphabet.push("m");
alphabet.push("n");
alphabet.push("o");
alphabet.push("p");
alphabet.push("q");
alphabet.push("r");
alphabet.push("s");
alphabet.push("t");
alphabet.push("u");
alphabet.push("v");
alphabet.push("w");
alphabet.push("x");
alphabet.push("y");
alphabet.push("z");

export function isPangram(string: String): boolean {
  const stringSet = new Set<String>();

  for (let i = 0; i < string.length; i++) {
    let currChar = string.charAt(i).toLowerCase();
    stringSet.add(currChar);
  }

  const setArray = Array.from(stringSet);

  return alphabet.every((letter) => setArray.includes(letter));
}
