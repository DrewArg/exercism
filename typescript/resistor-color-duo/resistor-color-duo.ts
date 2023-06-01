let map = new Map();
map.set("black", "0");
map.set("brown", "1");
map.set("red", "2");
map.set("orange", "3");
map.set("yellow", "4");
map.set("green", "5");
map.set("blue", "6");
map.set("violet", "7");
map.set("grey", "8");
map.set("white", "9");

export function decodedValue(colors: string[]): number {
  // throw new Error('Remove this statement and implement this function')
  let response = "";
  for (let i = 0; i < 2; i++) {
    response += map.get(colors[i].toLowerCase());
  }

  return Number(response);
}
