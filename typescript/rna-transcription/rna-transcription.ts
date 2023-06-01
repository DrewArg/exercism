const map = new Map();
map.set("G", "C");
map.set("C", "G");
map.set("T", "A");
map.set("A", "U");

export function toRna(string: String): String {
  let response = "";
  for (let i = 0; i < string.length; i++) {
    let letter = map.get(string.charAt(i));
    if (letter === undefined) {
      throw "Invalid input DNA.";
    } else {
      response += letter;
    }
  }
  return response;
}
