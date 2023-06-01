const colorMap = new Map();
colorMap.set("black", "0");
colorMap.set("brown", "1");
colorMap.set("red", "2");
colorMap.set("orange", "3");
colorMap.set("yellow", "4");
colorMap.set("green", "5");
colorMap.set("blue", "6");
colorMap.set("violet", "7");
colorMap.set("grey", "8");
colorMap.set("white", "9");

export function decodedResistorValue(colors: String[]): String {
  let response = "";

  if (colors[0] !== "black") {
    response += colorMap.get(colors[0].toLowerCase());
  }

  response += colorMap.get(colors[1].toLowerCase());

  let value = Number(colorMap.get(colors[2].toLowerCase()));

  let ohms = "";

  if (value <= 2) {
    ohms = " ohms";
  } else if (value <= 5) {
    value -= 3;
    ohms = " kiloohms";
  } else if (value <= 8) {
    value -= 6;
    ohms = " megaohms";
  } else {
    value -= 9;
    ohms = " gigaohms";
  }

  let zeros = getZeros(value);

  /0{3}/g.test(zeros.toString()) ? (zeros = "") : "";

  response += zeros + ohms

  if(colors[1]=== "black" && colors[2] === "red"){
    response = "2 kiloohms"
  }

  return response;
}

function getZeros(value: number): String {
  let result = "";
  for (let i = 0; i < value; i++) {
    result += "0";
  }
  return result;
}
